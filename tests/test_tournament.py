import hashlib
import json


def _commitment(tournament_id, entry_id, participant, probability_bps, rationale, salt, rubric_id):
    payload = json.dumps({
        "domain": "GENLAYER_FORECAST_RATIONALE_V1", "tournament_id": tournament_id,
        "entry_id": entry_id, "participant": participant, "probability_bps": probability_bps,
        "rationale": rationale, "salt": salt, "rubric_id": rubric_id,
    }, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def _deploy(direct_deploy, tournament_id="tournament-1"):
    return direct_deploy(
        "contracts/ForecastRationaleTournamentJudge.py", tournament_id, "Will the event happen?",
        json.dumps([{"id": "evidence", "anchor": "Uses authoritative evidence"}]),
        json.dumps(["https://official.example.org/event"]),
        "2030-01-01T00:00:00Z", "2030-01-10T00:00:00Z",
        "2030-02-01T00:00:00Z", "2030-03-01T00:00:00Z", 4000, "tournament-v1",
    )


def _add_entry(contract, vm, owner, entry_id, probability, rationale, salt):
    vm.sender = owner
    commitment = _commitment(contract.tournament_id, entry_id, str(contract.owner), probability, rationale, salt, "tournament-v1")
    vm.warp("2029-12-20T00:00:00Z")
    contract.commit(entry_id, commitment)
    vm.warp("2030-01-05T00:00:00Z")
    contract.reveal(entry_id, probability, rationale, salt)


def test_commit_reveal_judge_and_weighted_finalize(direct_vm, direct_deploy, direct_owner):
    contract = _deploy(direct_deploy)
    _add_entry(contract, direct_vm, direct_owner, "entry-1", 7000, "A specific falsifiable sourced rationale.", "salt-1")
    direct_vm.mock_web(r".*", {"status": 200, "body": "official evidence"})
    direct_vm.mock_llm(r".*", json.dumps({"evidence_state": "FINAL", "scores": {"evidence": 4}, "hard_flags": []}))
    assert contract.judge_entry("entry-1")["status"] == "SCORABLE"
    assert direct_vm.run_validator()
    direct_vm.clear_mocks()
    direct_vm.warp("2030-02-02T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "official final result"})
    direct_vm.mock_llm(r".*", json.dumps({"evidence_state": "FINAL", "outcome": "YES"}))
    assert contract.resolve_outcome()["outcome"] == "YES"
    finalized = contract.finalize_entry("entry-1")
    assert finalized["brier_bps"] == 900
    assert finalized["rationale_bps"] == 10000
    assert finalized["combined_bps"] == 9460


def test_wrong_reveal_reverts(direct_vm, direct_deploy, direct_owner):
    contract = _deploy(direct_deploy, "tournament-wrong")
    direct_vm.sender = direct_owner
    commitment = _commitment("tournament-wrong", "entry-1", str(contract.owner), 5000, "A rationale", "salt", "tournament-v1")
    direct_vm.warp("2029-12-20T00:00:00Z")
    contract.commit("entry-1", commitment)
    direct_vm.warp("2030-01-05T00:00:00Z")
    with direct_vm.expect_revert("does not match commitment"):
        contract.reveal("entry-1", 5000, "A rationale", "wrong")


def test_hindsight_judging_is_closed(direct_vm, direct_deploy, direct_owner):
    contract = _deploy(direct_deploy, "tournament-hindsight")
    _add_entry(contract, direct_vm, direct_owner, "entry-1", 5000, "A rationale", "salt")
    direct_vm.warp("2030-01-10T00:00:00Z")
    with direct_vm.expect_revert("judging window is closed"):
        contract.judge_entry("entry-1")


def test_max_wait_voids_without_consensus(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy, "tournament-timeout")
    direct_vm.warp("2030-03-01T00:00:00Z")
    assert contract.resolve_outcome()["reason_code"] == "MAX_WAIT_EXPIRED"
    assert contract.get_leaderboard() == []

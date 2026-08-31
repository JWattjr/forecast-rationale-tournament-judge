# Forecast Rationale Tournament Judge

A standalone GenLayer Intelligent Contract that rewards forecast accuracy and bounded reasoning quality through commit/reveal, consensus judging, and deterministic scoring.

## GenLayer-native decision

Validators independently score frozen rationale dimensions and must agree exactly on every dimension score, and independently resolve the event outcome. Because an accepted score map is stored verbatim and folded into the combined score, exact agreement is what guarantees that every validator-compatible result yields the same leaderboard order; genuine disagreement fails closed. Brier, normalized rationale, weighted combined score, and leaderboard order are deterministic.

## Lifecycle and API

Commit → reveal/judge → outcome WAIT/CONTESTED/RESOLVED/VOID → one-time entry finalization. Rationale judging closes before the outcome window, and max-wait guarantees terminal VOID.

Constructor: `tournament_id, question, rubric, sources, commit_deadline, reveal_deadline, outcome_deadline, outcome_max_wait, rationale_weight_bps, spec_id`. Public methods: `commit()`, `reveal()`, `judge_entry()`, `resolve_outcome()`, `finalize_entry()`, `get_entry()`, `get_leaderboard()`, and `get_state()`.

Every evidence URL is frozen, bounded, public HTTPS. Fetched text is untrusted input; prompts instruct validators to ignore embedded commands. Leader and validator closures snapshot ordinary values and independently re-fetch evidence.

## Live evidence

- [Corrected StudioNet contract](https://explorer-studio.genlayer.com/address/0x928f40f8F9615c5875c62CEee3Ef2a1a2903dDaf)
- Exact StudioNet transaction hashes, constructor arguments, state, and execution results are in `deployments/studionet.json`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/ForecastRationaleTournamentJudge.py
python -m pytest tests -q
```

The contract uses a concrete pinned GenVM runner. See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and `PORTAL_SUBMISSION.md` for reviewer evidence. This primitive does not custody funds; consumers must wait for GenLayer finality and remain idempotent.

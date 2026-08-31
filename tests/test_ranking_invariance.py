"""The rationale validator must never accept two results that rank differently.

A prior revision accepted per-dimension scores differing by plus or minus one.
The accepted map is stored verbatim and folded into ``rationale_bps`` and thus
into leaderboard order, so that tolerance allowed two validator-compatible
results to rank entries differently. These tests pin the invariant directly:
if the validator accepts a pair, the pair must produce an identical rationale
score, and therefore an identical ranking outcome.
"""

import ast
import itertools
from pathlib import Path

CANDIDATES = (
    Path("contracts/ForecastRationaleTournamentJudge.py"),
    Path("contracts/forecast_rationale_tournament_judge.py"),
)
HELPERS = ("_scores_agree", "_rationale_bps")


def _contract_path() -> Path:
    for candidate in CANDIDATES:
        if candidate.exists():
            return candidate
    raise AssertionError("tournament judge contract source not found")


def _load_helpers():
    """Execute only the pure helpers so the test needs no GenVM runtime."""
    path = _contract_path()
    tree = ast.parse(path.read_text(encoding="utf-8"))
    wanted = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name in HELPERS
    ]
    assert {node.name for node in wanted} == set(HELPERS)
    namespace = {}
    exec(compile(ast.Module(body=wanted, type_ignores=[]), str(path), "exec"), namespace)
    return namespace["_scores_agree"], namespace["_rationale_bps"]


def test_accepted_scores_always_produce_the_same_ranking():
    scores_agree, rationale_bps = _load_helpers()
    rubric = [{"id": "evidence"}, {"id": "specificity"}, {"id": "falsifiability"}]
    ids = [dimension["id"] for dimension in rubric]
    maps = [dict(zip(ids, combo)) for combo in itertools.product(range(5), repeat=len(ids))]
    accepted = 0
    for left, right in itertools.product(maps, repeat=2):
        if scores_agree(left, right):
            accepted += 1
            assert rationale_bps(left, rubric) == rationale_bps(right, rubric)
    assert accepted == len(maps)


def test_off_by_one_dimension_scores_fail_closed():
    scores_agree, _ = _load_helpers()
    assert not scores_agree({"evidence": 2}, {"evidence": 3})
    assert not scores_agree({"evidence": 0}, {"evidence": 1})
    assert not scores_agree({"evidence": 3, "specificity": 2}, {"evidence": 3, "specificity": 1})
    assert scores_agree({"evidence": 3, "specificity": 2}, {"evidence": 3, "specificity": 2})


def test_dimension_set_mismatch_fails_closed():
    scores_agree, _ = _load_helpers()
    assert not scores_agree({"evidence": 1}, {"evidence": 1, "specificity": 1})
    assert not scores_agree({"evidence": 1}, {"specificity": 1})
    assert not scores_agree({}, {})


def test_malformed_or_out_of_range_scores_fail_closed():
    scores_agree, _ = _load_helpers()
    assert not scores_agree([], [])
    assert not scores_agree({"evidence": "2"}, {"evidence": 2})
    assert not scores_agree({"evidence": True}, {"evidence": 1})
    assert not scores_agree({"evidence": -1}, {"evidence": -1})
    assert not scores_agree({"evidence": 5}, {"evidence": 5})


def test_rationale_score_is_monotonic_in_dimension_scores():
    _, rationale_bps = _load_helpers()
    rubric = [{"id": "evidence"}, {"id": "specificity"}]
    assert rationale_bps({"evidence": 0, "specificity": 0}, rubric) == 0
    assert rationale_bps({"evidence": 4, "specificity": 4}, rubric) == 10000
    assert rationale_bps({"evidence": 3, "specificity": 2}, rubric) < rationale_bps(
        {"evidence": 3, "specificity": 3}, rubric
    )


def test_validator_carries_no_score_tolerance():
    """Guard against the tolerant comparison being reintroduced."""
    path = _contract_path()
    tree = ast.parse(path.read_text(encoding="utf-8"))
    judge_consensus = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "_judge_consensus"
    )
    validator = next(
        node
        for node in judge_consensus.body
        if isinstance(node, ast.FunctionDef) and node.name == "validator_fn"
    )
    calls = [
        child.func.id
        for child in ast.walk(validator)
        if isinstance(child, ast.Call) and isinstance(child.func, ast.Name)
    ]
    assert "_scores_agree" in calls
    assert "abs" not in calls

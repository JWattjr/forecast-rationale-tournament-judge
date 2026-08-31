# Steward response: rationale-score ranking invariance

Date: 2026-08-31

## Review finding

The rejected revision allowed independently produced dimension scores to differ
by one even though the accepted leader map was stored verbatim and later folded
into `rationale_bps`, `combined_bps`, and leaderboard order. That equivalence
rule did not preserve the same ranking outcome.

## Remediation

The rationale validator now requires exact agreement on the complete normalized
0-4 dimension-score map. It also binds status, sorted hard flags, and source
coverage. Missing, extra, empty, non-integer, boolean, and out-of-range score
maps fail closed. The accepted map is the same map used by deterministic
`_rationale_bps`, so every validator-compatible result produces the same
rationale score, combined score, and leaderboard order.

The corrected immutable source commit is
[`32e0367e4267714351168a789edcfa7f9615b1e1`](https://github.com/JWattjr/forecast-rationale-tournament-judge/commit/32e0367e4267714351168a789edcfa7f9615b1e1).

## Regression evidence

- `tests/test_ranking_invariance.py` exhaustively checks every pair in the
  three-dimension 0-4 score space. Every accepted pair has an identical
  `rationale_bps`; all 125 valid self-pairs remain accepted.
- Off-by-one, missing/extra dimensions, empty maps, strings, booleans, and
  scores outside 0-4 are rejected.
- An AST binding test proves `_judge_consensus.validator_fn` calls
  `_scores_agree` and contains no tolerance calculation.
- Full standalone result: 13 passed and one environment-only integration skip.
- GenVM AST lint: all three checks passed. The local SDK phase was unavailable
  because the installed linter bundle lacks the pinned runner tar; the same
  source deployed and exposed a valid schema on StudioNet.

## Matching StudioNet deployment

- Contract: https://explorer-studio.genlayer.com/address/0x928f40f8F9615c5875c62CEee3Ef2a1a2903dDaf
- Deployment transaction: `0xb3c279885c49b4edca102dff8275b421d1c5d23921f53ca1cff05bd8ac40230f`
- Deployment: `FINALIZED`, leader execution `SUCCESS`, `MAJORITY_AGREE`
- Live rationale transaction: `0x8818429eaa3c283d4e824e816db1d9cb40d0b00143709b32836589557e014d9b`
- Rationale transaction: `FINALIZED`, leader execution `SUCCESS`,
  `MAJORITY_AGREE` in two rounds
- Final-round votes: three `AGREE`, one `DISAGREE`, one `IDLE`
- Stored exact map: `evidence=4`, `causal=2`, `falsifiability=3`

The disagreeing validator was correctly excluded instead of having its
different score map treated as equivalent. Exact constructor arguments,
receipts, test state, and source commit are recorded in
`deployments/studionet.json`.

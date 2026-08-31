# Security and consensus audit: ForecastRationaleTournamentJudge

Audit date: 2026-08-31
Scope: `contracts/ForecastRationaleTournamentJudge.py`
Method: manual review, GenVM AST lint, direct-mode adversarial tests, exhaustive ranking-invariance regression, explicit independent-validator review, and finalized StudioNet receipt, source, schema, and state inspection.

## Result

No unresolved critical or high-severity code issue was found after remediation. The contract does not custody or transfer value.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| FT-01 | High | Rationale scores were metadata and could not affect ranking. | Freeze a nonzero rationale weight and calculate combined basis points deterministically. |
| FT-02 | High | Rationale judging after reveal close could introduce hindsight. | Close judging at the reveal deadline, before outcome resolution. |
| FT-03 | High | Cancelled outcomes were not consistently terminal/finalizable. | Store terminal VOID, make resolution idempotent, and keep voided entries off the leaderboard. |
| FT-04 | Medium | Outcome resolution could remain retryable forever. | Freeze max-wait and deterministically VOID at expiry. |
| FT-05 | High | The rationale validator accepted per-dimension score differences of one even though the accepted raw map changed `rationale_bps`, `combined_bps`, and leaderboard order. | Require the complete normalized 0-4 score map to agree exactly before it can be stored or used; malformed, missing, extra, and out-of-range scores fail closed. |

## Verification

- Exact runner pin: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
- `genvm-lint` passes all AST safety checks. The local linter bundle cannot perform its SDK phase because it does not contain the contract's pinned runner tar; the matching StudioNet deployment supplies runtime source/schema verification.
- Direct tests exercise lifecycle, failure, and independent-validator paths.
- Exhaustive regression over the three-dimension 0-4 score space proves every validator-accepted pair produces identical `rationale_bps`; malformed and out-of-range maps fail closed.
- AST regression proves nondeterministic closures do not reference `self`.
- StudioNet deployment and consensus transaction are finalized with successful leader execution; exact evidence is in `deployments/studionet.json`.
- Live StudioNet integration assertions re-read the stored exact score map and pass.

## Residual risk

See `SECURITY.md`. This is an engineering assessment, not formal verification, a financial guarantee, or legal advice.

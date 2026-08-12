# Security and consensus audit: ForecastRationaleTournamentJudge

Audit date: 2026-08-12
Scope: `contracts/ForecastRationaleTournamentJudge.py`
Method: manual review, full GenVM lint and pinned-runner schema validation, direct-mode adversarial tests, explicit independent-validator execution, and finalized StudioNet receipt/state inspection.

## Result

No unresolved critical or high-severity code issue was found after remediation. The contract does not custody or transfer value.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| FT-01 | High | Rationale scores were metadata and could not affect ranking. | Freeze a nonzero rationale weight and calculate combined basis points deterministically. |
| FT-02 | High | Rationale judging after reveal close could introduce hindsight. | Close judging at the reveal deadline, before outcome resolution. |
| FT-03 | High | Cancelled outcomes were not consistently terminal/finalizable. | Store terminal VOID, make resolution idempotent, and keep voided entries off the leaderboard. |
| FT-04 | Medium | Outcome resolution could remain retryable forever. | Freeze max-wait and deterministically VOID at expiry. |

## Verification

- Exact runner pin: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.
- `genvm-lint check` passes AST and SDK schema validation.
- Direct tests exercise lifecycle, failure, and independent-validator paths.
- AST regression proves nondeterministic closures do not reference `self`.
- StudioNet deployment and consensus transaction are finalized with successful leader execution; exact evidence is in `deployments/studionet.json`.
- Bradbury is accepted only after successful execution and state reads, then finalized independently.

## Residual risk

See `SECURITY.md`. This is an engineering assessment, not formal verification, a financial guarantee, or legal advice.

# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts
**Title:** Forecast Rationale Tournament Judge
**Contribution date:** August 31, 2026

## Notes / Description

Built and deployed an MIT-licensed Forecast Rationale Tournament Judge for forecasting competitions that reward reasoning as well as accuracy. Participants commit a domain-separated hash, then reveal probability, rationale, and salt. Validators independently score frozen 0-4 dimensions and must agree exactly on the complete normalized score map before it is stored or used, so every validator-compatible result preserves the same rationale score, combined score, and leaderboard order. A separate consensus resolves YES, NO, or VOID; deterministic code computes Brier accuracy, normalized rationale basis points, weighted combined scores, and tie-breaks. Judging closes before the outcome window to prevent hindsight; cancellation or max-wait is terminal VOID. Includes pinned GenVM source, exhaustive ranking-invariance regression, adversarial tests, audit, test matrix, and matching finalized StudioNet deployment evidence. It holds no funds.

## Evidence to add

1. GenLayer Explorer Contract — https://explorer-studio.genlayer.com/address/0x928f40f8F9615c5875c62CEee3Ef2a1a2903dDaf
2. GitHub Repository — https://github.com/JWattjr/forecast-rationale-tournament-judge
3. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/contracts/ForecastRationaleTournamentJudge.py
4. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/tests/test_ranking_invariance.py
5. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/docs/STEWARD_RESPONSE.md
6. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/docs/SECURITY_AUDIT.md
7. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/docs/TEST_MATRIX.md
8. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/deployments/studionet.json

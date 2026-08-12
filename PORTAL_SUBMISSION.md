# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts
**Title:** Forecast Rationale Tournament Judge
**Contribution date:** August 12, 2026

## Notes / Description

Built and deployed an MIT-licensed Forecast Rationale Tournament Judge for forecasting competitions that reward reasoning as well as accuracy. Participants commit a domain-separated hash, then reveal probability, rationale, and salt. Before the outcome window closes, validators independently score frozen 0–4 rationale dimensions with bounded ±1 equivalence. A separate consensus resolves YES/NO/VOID; contract code computes Brier accuracy, normalized rationale basis points, a frozen weighted combined score, and deterministic leaderboard tie-breaks. Judging closes at reveal deadline to prevent hindsight; cancellation or max-wait is terminal VOID and ineligible for ranking. Includes pinned GenVM source, commit/reveal, hindsight, timeout, scoring and validator tests, full schema validation, audit, test matrix, and finalized StudioNet/Bradbury outcome consensus evidence.

## Evidence to add

1. GitHub Repository — https://github.com/JWattjr/forecast-rationale-tournament-judge
2. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/contracts/ForecastRationaleTournamentJudge.py
3. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/tests/test_tournament.py
4. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/forecast-rationale-tournament-judge/blob/main/deployments/bradbury.json
8. GenLayer Explorer Contract — https://explorer-bradbury.genlayer.com/address/0x108bFa49D9D45A02a75f6379a2737f626B377A5C

The repository is private. Grant Portal reviewers repository access before submission.

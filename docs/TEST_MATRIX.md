# Test matrix

| Requirement | Direct test | Integration evidence |
| --- | --- | --- |
| Domain-separated commit/reveal and wrong-salt rejection | Direct mocked GenVM | StudioNet evidence where applicable |
| Rationale judging closes before outcome window | Direct mocked GenVM | StudioNet evidence where applicable |
| Exact validator score agreement and dimension set | Direct mocked GenVM | Matching source verified on StudioNet |
| Ranking invariance: every validator-accepted score pair yields an identical rationale score | Exhaustive pair regression over the 0-4 rubric space | Corrected source and schema verified on StudioNet |
| Malformed, missing, extra, boolean, and out-of-range scores fail closed | Pure helper regression and validator AST binding | Corrected source verified on StudioNet |
| Deterministic Brier/rationale weighted score and ranking | Direct mocked GenVM | StudioNet evidence where applicable |
| Cancellation/max-wait VOID handling | Direct mocked GenVM | StudioNet evidence where applicable |
| Finalized StudioNet deployment and outcome transaction | Direct mocked GenVM | StudioNet receipt and state inspection |
| Nondeterministic storage isolation | AST closure regression | Receipt inspected for successful execution |
| Public URL controls | Constructor rejection paths | Frozen official GovInfo HTTPS source |
| Prompt injection boundary | Untrusted evidence schema/prompt | Independent validator re-fetch |
| Replay/finality safety | Terminal/idempotent transition checks | Consumers instructed to wait for finality |

StudioNet evidence must show both protocol `FINALIZED` and leader execution `SUCCESS`; a lifecycle label alone is not a passing test.

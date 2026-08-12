# Test matrix

| Requirement | Direct test | Integration evidence |
| --- | --- | --- |
| Domain-separated commit/reveal and wrong-salt rejection | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Rationale judging closes before outcome window | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Bounded validator score tolerance and exact dimension set | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Deterministic Brier/rationale weighted score and ranking | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Cancellation/max-wait VOID handling | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Finalized StudioNet deployment and outcome transaction | Direct mocked GenVM | StudioNet/Bradbury evidence where applicable |
| Nondeterministic storage isolation | AST closure regression | Receipt inspected for successful execution |
| Public URL controls | Constructor rejection paths | Frozen official GovInfo HTTPS source |
| Prompt injection boundary | Untrusted evidence schema/prompt | Independent validator re-fetch |
| Replay/finality safety | Terminal/idempotent transition checks | Consumers instructed to wait for finality |

StudioNet evidence must show both protocol `FINALIZED` and leader execution `SUCCESS`; a lifecycle label alone is not a passing test. Bradbury evidence records all five deployment hashes before any finality polling.

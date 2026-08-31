# Security model

## Threats addressed

- **Malicious leader:** validators independently re-fetch evidence and recompute consequential fields.
- **Prompt injection:** source text is bounded and explicitly treated as untrusted data.
- **Source outage and drift:** missing evidence fails closed; substantive validator disagreement prevents accepted consensus.
- **Premature resolution:** frozen UTC deadlines are checked deterministically before nondeterministic work.
- **Replay and double settlement:** terminal/idempotent state transitions prevent duplicate consequences.
- **Unsafe evidence URLs:** userinfo, private/internal hosts, literal private IPs, IPv6 literals, whitespace, and non-default ports are rejected.

## Contract-specific boundary

Validators independently score frozen rationale dimensions and must agree exactly on every dimension score, and independently resolve the event outcome. Because an accepted score map is stored verbatim and folded into the combined score, exact agreement is what guarantees that every validator-compatible result yields the same leaderboard order; genuine disagreement fails closed. Brier, normalized rationale, weighted combined score, and leaderboard order are deterministic.

Commit → reveal/judge → outcome WAIT/CONTESTED/RESOLVED/VOID → one-time entry finalization. Rationale judging closes before the outcome window, and max-wait guarantees terminal VOID.

## Residual risks

HTTPS reachability does not prove publisher authority. DNS rebinding remains possible without a deployment-specific domain allowlist. Dynamic sources can legitimately cause validator disagreement. LLM classifications can remain unresolved on ambiguous language. Downstream payout code is out of scope and must consume only finalized state with its own idempotency guard.

# Agent loop exits on no tool call, and truncation is not completion

The learner showed they can tell what ends an agent loop: a reply with no tool call, not wording like "done". They also count `max_turns` correctly (tool-call turns plus the final text-only reply) and treat `max_tokens` as truncated, not finished.
Later lessons can build on this and cover the remaining stop reasons and failure handling.

**Evidence:** quiz 0001, submission s1, all four items correct (q1 text-matching exit, q2 turn count, q3 result field, q4 max_tokens).
**Implications:** M1 and M2 did not show up; do not re-teach O1 basics except as retrieval practice.

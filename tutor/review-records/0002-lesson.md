# Review record: lesson 0002 (O2, 15 min)

Before review, the reference check (`drafts/sources/0002-check.md`) led to five fixes: softened the "Anthropic's advice" quote, the "no memory" and "no notion of turns" claims, framed the four duties as the lesson's grouping, said "pre-approved" for `permissions.allow`, and stated the one-call-per-turn assumption in the worked example.

## Pass 1: 17 findings

1. S4 overclaimed "only a cap you set" stops a loop: reworded (model can end it; both caps default to none); misconception box removed.
   Figure 2 showed only a summary after compaction: added recent-history segment, dropped the CLAUDE.md footnote.
   Stateless claim cited the tool-use page: now cites the Messages API page.
   Unsourced claims about chat UIs and hosted products: hedged or cut.
   "LOOP: the one exit" and "does not stop itself" contradicted the lesson: fixed to "the model's exit (caps add more)" and "enforce its own caps".
   `TOOLS` meant two things: renamed to `TOOL_SCHEMAS` and `TOOL_IMPLS`.
2. Definition overreached: now "written for Claude Code, names two of the duties"; four duties marked as the lesson's grouping.
3. none.
4. S3 check made CLAUDE.md look like enforcement: new stem ("keeps the rule in front of the model"), new bullet "Remembered is not enforced" pointing to permissions and hooks.
5. Subagent, hooks, CLAUDE.md undefined: one-clause definitions added.
6. none.
7. Worked example circular: trace now holds subtype, num_turns and max_turns so steps read them off; "Your turn" has its first blank filled. Left: the faded task still practices context and permissions, not the loop duty, because the worked example already covers loop and limits.
8. Missing "why": added why only the harness can enforce caps and why the model cannot be its own gate.
9. "Choose a number on purpose": now says how (num_turns of a normal run, +1, budget headroom).
10. none.
11. O1 repeats and concurrency tangent: cut the `result?` column, the subtype snippet, the concurrency bullet; replaced the S2 and S4 checks with a "where does a turn cap belong" check and a "what stops it with no options" check.
12. No duty-symptom-knob summary: added a table in the summary.
13. none.
14. Length: cut the S3 aside, two misconception boxes, the five "Show the answer" blocks and a server-tools aside. Measured 2,770 visible words after pass 1 (the reviewer's 2,900+ estimate was high); section time labels rebalanced.
15. none.
16. Prose density: covered by the cuts in 14.
17. Footer named quiz 0002 before it existed: quiz 0002 and key written in the same pass, so the line stays.

## Pass 2: 7 findings

1. none.
2. "Only the harness can enforce a cap" too broad: narrowed to turn or spend caps across calls, with `max_tokens` noted as a per-reply cap.
   Figure 2 caption cited the wrong page: now cites the agent-loop page.
3. Anchor text "Working with the Messages API": changed to "Using the Messages API".
5. "Hook" used in S3 before its definition: glossed inline.
   Duty grouping inconsistent: lead, S1 sentence, Figure 1 and its title now all use loop and tools, context, limits, permissions, matching the sections and the summary table.
14. Length: dropped the summary bullets (kept one "why" line and the table), shortened the permission_mode bullet, cut the S1 mix-up box. Measured 2,680 visible words, about 17.9 minutes (1.19 times 15); the reviewer's 3,300 estimate was high. Left the warm-up's two recalls (spacing) and the Go further links (cited sources).
16. Prose density: covered by the cuts in 14.

Stopped after pass 2 as the loop allows.

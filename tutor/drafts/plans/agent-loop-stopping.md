# Plan: agent-loop-stopping

## Scope
- Lesson 0001, "How an agent decides it is done" (`lessons/0001-how-an-agent-decides-it-is-done.html`), objective O1: how an agent loop decides to stop.
- No exam or occasion named. Treat it as a retrieval-practice sheet for CSCI 498E/598E, whose exam would ask about what ends an agent loop and what can end it badly (MISSION.md).
- Learner state: quiz 0001, submission s1, 4/4, no misconception shown (M1 "done" in the words, M2 "any non-tool_use stop means finished" both unshown). So there is no weak topic. Weight goes to the twists an exam could add, not to re-teaching.
- A sheet with this slug already exists at `cheatsheets/agent-loop-stopping.html`. It runs well over the word budget and has a Terms block and a "Where you stand" box. The writer should replace it with the shorter sheet below and must not keep its Terms block.

## The model
- An agent loop is a `while` loop run by the harness: it goes around again while the latest reply asks for a tool, and the only finished state is a reply with no tool call, read from `stop_reason` (structure), never from the words.
- Anything else that stops a run (a truncated reply, a turn or budget cap) is a stop that is not a success, so each ending is classified by its signal before the output is used.

Figure: a code sketch, not an SVG. It is the lesson's basic loop with the else branch split into the three endings that the lesson's practice section and s3 imply. Keep it to about 8 lines:

```
while True:
    reply = call_model(messages, tools)     # 1 turn
    if reply.stop_reason == "tool_use":     # run tool, append, loop
        ...
    elif reply.stop_reason == "end_turn":   # only natural finish
        break
    else:                                   # max_tokens / context full:
        ...                                 # truncated, NOT an answer
# caps (max_turns, max_budget_usd) live outside, around the loop
```
Under it, one line: "Reading a run: check subtype, then read `result` only on `success`."
The lesson's own code has `else: break`. The sketch must show why that line is the bug, so the learner sees the trap in the code, not only in a bullet.

## Ranked ideas

### Tier 1: must know cold
1. Harness decides, by reading `stop_reason` on each reply; `tool_use` = run tool, append result, call again; `end_turn` = exit, use the reply. (s1)
2. Completion is structural (no tool call), never wording like "done"; text matching fails both ways (exits early with a pending call; spins on when the word is never written). (s2; M1)
3. `max_tokens` and `model_context_window_exceeded` = truncated, not finished; do not return the reply, do not run a tool call in it (it may be incomplete); raise the limit and retry or ask it to continue. (s3 and practice; M2)
4. `max_turns` needed = tool-call turns + 1 for the final text-only reply; a cap equal to the tool-call turns ends `error_max_turns` even if the work is done. (s3 and worked example)
5. Check the result subtype first; only `success` carries `result`; a cap stops a run but does not say it succeeded. (s3)

### Tier 2: should know
- Two levels of stop: reply-level from the API (`max_tokens`, context exceeded) vs run-level caps set in the harness (`max_turns`, `max_budget_usd`). (s3)
- Both caps are unlimited by default in the Agent SDK. (s3)
- The four subtypes by name: `success`, `error_max_turns`, `error_max_budget_usd`, `error_during_execution`. (s3)
- A turn = one model call plus the tool runs it triggers. (s2 aside)
- CS analogy: prose for control flow = parsing a log message when a return code exists. (s2)

### Tier 3: can look up
- Linked docs: Anthropic "handling stop reasons", Agent SDK "how the agent loop works", AI SDK loop control. (Go further)
- The history-append lines of the loop (`messages.append(...)`). (s1)
- Other stop_reason values (see Gaps).

## Contrasts and twists
Form: one table with the columns "Situation", "Tempting answer", "Right answer". One row per line below.

| Situation | Tempting | Right |
|---|---|---|
| Reply text says "done" but has a tool call | exit, task finished | do not exit: run the tool; the call is the signal |
| Reply finishes the task but never says "done" | keep looping on words | exit: no tool call |
| `end_turn` vs `max_tokens` | both are "model stopped, so use the reply" | only `end_turn` is finished; `max_tokens` is truncated |
| `max_tokens` reply ends in a tool call | run it | do not; it may be cut mid-call |
| Reply-level stop vs run-level cap | one kind of stop | reply-level: `max_tokens`, context full. Run-level: `max_turns`, `max_budget_usd` |
| `max_turns` = N tool-call turns | enough | too small; need N+1, else `error_max_turns` and no `result` |
| `max_turns` = N+1 | fine | `success` with a `result` (the cap equals the turns used, which still passes) |
| Hit a cap | task failed or task done, guess | cap says nothing about the task; read the subtype |
| Which subtype has `result` | any finished run | `success` only; `error_max_turns`, `error_max_budget_usd`, `error_during_execution` have none |
| No cap set (the default) | something will stop it | nothing in the harness stops it; only the model's own `end_turn` or a reply-level stop |

Changed conditions an exam could use: cap one below or one above the needed count; a truncated reply that contains a tool call; a harness whose else branch treats every non-`tool_use` reason as done.

## Cut
- The "Why this matters for you" box, the lead, the kicker and the section timings: motivation and navigation, not recall.
- The long story of the "Done reading the file, now editing" example and the "reverse also happens" retelling: reduce to one table row. The learner got quiz q1 right.
- The worked example's 5-step walk-through: keep only its rule (tool-call turns + 1). The learner got quiz q2 right.
- The three "Check yourself" widgets and their feedback text: replaced by the self-test.
- Terms block (harness, stop_reason, turn, caps): the learner knows these from 4/4; the three that matter (turn, subtype list, defaults) fit in table cells.
- The existing sheet's "Where you stand" box and four separate trap boxes: the traps become table rows.
- The Go further links beyond one line.
- Do not repeat any quiz 0001 item as a self-test question.

## Self-test
Ten questions go below the sheet, each with a collapsed answer and a "reread" tag. None repeats a quiz 0001 item (done+edit_file; 6 turns, so 7; budget subtype and missing result; max_tokens mid-sentence). Quiz 0001 has been handed in (s1), so no ungraded quiz answer is given away.

| # | Type | Question | Answer | Reread | Serves |
|---|---|---|---|---|---|
| 1 | recall | Who decides whether to call the model again, and from which field? | The harness, from `stop_reason` on the latest reply (`tool_use` = go again, `end_turn` = exit). | s1 | Tier 1, idea 1 |
| 2 | compare | Harness A exits when the text contains "finished". Harness B returns the reply whenever `stop_reason != "tool_use"`. Name one way each goes wrong. | A: exits early on "finished, now editing" with a pending call, or spins on when the word never appears. B: returns a `max_tokens` or context-exceeded reply, which is truncated, as the answer. | s2, s3 | M1 and M2; Tier 1, ideas 2 and 3 |
| 3 | apply (twist) | A reply stops with `max_tokens` and its last block is a `write_file` tool call. Run it? Why? | No. The reply is truncated and the call may be incomplete; raise `max_tokens` and retry, or ask it to continue. | practice | M2; Tier 1, idea 3 |
| 4 | apply (boundary) | `max_turns` is 5. The model makes 4 tool-call turns, then a text-only reply. Subtype, and is there a `result`? | `success`, with a `result`: 4 + 1 = 5 fits exactly. | s3 | Tier 1, idea 4 |
| 5 | apply (changed condition) | The stop reasons arrive `tool_use`, `tool_use`, `end_turn`, and `max_turns` is 2. How does the run end? | `error_max_turns`, no `result`: the cap is reached after two tool-call turns, before the final reply. | worked example | Tier 1, idea 4 |
| 6 | spot the bug | A dashboard counts a run as "succeeded" whenever its subtype is not `error_during_execution`. What is wrong? | `error_max_turns` and `error_max_budget_usd` are not successes either; only `success` is. | s3 | Tier 1, idea 5 |
| 7 | compare | Sort into reply-level or run-level: `max_tokens`, `max_budget_usd`, `model_context_window_exceeded`, `max_turns`. | Reply-level: `max_tokens`, `model_context_window_exceeded`. Run-level: `max_budget_usd`, `max_turns`. | s3 | Tier 2 |
| 8 | explain why | A run ends `error_max_turns` after its last tool call succeeded. Why can't you treat it as finished? | A cap stops a run whether or not the task is done; no final response was produced and there is no `result`. Only subtype `success` means success. | s3 | Tier 1, idea 5 |
| 9 | apply (default) | You set neither `max_turns` nor `max_budget_usd` and the model keeps requesting tools. What ends the run? | Neither cap stops it (both are unlimited by default); only a reply-level stop or the model finishing with `end_turn`. | s3 | Tier 2 |
| 10 | explain why | In CS terms, why is `stop_reason` a better exit test than reading the reply's words? | It is a structured value, like a return code; words are like a log message. Branch control flow on structure. | s2 | Tier 2; M1 |

Spread: Tier 1 gets seven questions (1 to 6, 8), Tier 2 three (7, 9, 10). With no weak topic, the weight goes to M2 and the cap-counting twists (2, 3, 4, 5, 6, 8), which an exam can change most easily.
Types: recall 1, compare 2, apply 4, spot the bug 1, explain why 2.

## Layout
Visible text excluding the self-test is about 600 words, with one idea per line.

1. **Header** (about 15 words): title, "Lesson 1, objective O1", link to the lesson.
2. **The model** (about 90 words): the two sentences, the code sketch, the "reading a run" line.
3. **Know cold** (about 110 words): the five Tier 1 items, one line each, each with a section link.
4. **Signals table** (about 130 words): signal, level (reply or run), what it means, what the loop does. Rows: `tool_use`, `end_turn`, `max_tokens`, `model_context_window_exceeded`, `max_turns` hit, `max_budget_usd` hit. Next to the cap rows, put the four subtypes and "no `result` unless `success`".
5. **Twists table** (about 200 words): the contrasts-and-twists table above; at most 8 rows, folding row 9 into the signals table and keeping the caps rows (N versus N+1) side by side.
6. **Counting and defaults** (about 40 words): "`max_turns` needed = tool-call turns + 1", "both caps unlimited by default", "turn = one model call plus its tool runs".
7. **Reread map** (about 30 words): question numbers mapped to s1, s2, s3 and the practice section.
8. **Self-test** (about 350 words, not counted): the ten questions, answers in collapsed `details`.

Format rules for the writer: a heading for every block; no paragraph longer than two sentences; bullet points, as PREFERENCES.md asks; tables wherever things are compared; no praise and no "where you stand" box; relate to CS (while loop, return code, log line).

## Study order
1. Read the model sketch and the Know cold list (two minutes).
2. Cover the sheet and answer the self-test aloud or on paper, hardest first: 3, 5, 4, 6, 2.
3. Check each answer, and for a miss reread only the section named for that question in the lesson.
4. Rewrite the loop sketch from memory, including the third branch for truncation.
5. Redo only the missed questions the next day.

## Gaps
Things an exam on O1 would probably test that the lesson does not teach (the writer should report them and not fill them in):
- `refusal`, `pause_turn` and `stop_sequence` stop reasons, and the right handling for each (NOTES.md lists these as not yet covered; the quiz summary says to ask for a lesson on them).
- Whether `model_context_window_exceeded` can be recovered the same way as `max_tokens`: the lesson says only "treat as truncated, not finished".
- What causes `error_during_execution`; the lesson names it with no detail.
- An empty `end_turn` reply, and whether subagent or budget caps differ in depth (NOTES.md).
- What state remains, such as files written, after a run ends on a cap; the lesson says only that no `result` exists.

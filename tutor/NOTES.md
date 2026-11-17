# Notes

## Learner
- Name unknown. CS student (CSCI 498E/598E course). Wants bullets, concise first, depth on request; relate to CS; direct feedback, no praise (see PREFERENCES.md).
- Learning agents for a class on agentic AI (CSCI 498E/598E). MISSION.md confirmed by the learner (Why, Success and Out-of-scope all accepted as written, 2026-11-08).

## Misconception ids
- M1: an agent is done when its text says "done" (completion read from wording, not tool calls).
- M2: any stop that is not tool_use means the task finished (ignores max_tokens, truncation).
- M3: the model (or the API) runs its own tools.
- M4: harness limits are on by default, so a runaway loop stops itself.
- M5: compaction is lossless, so early instructions are safe.
- M6: a denied tool call ends the run.

## Objectives
- O1: how an agent loop decides to stop (lesson 0001, quiz 0001).
- O2: the goal of an agent harness: loop and tools, context, limits, permissions, and why a bare model needs them (lesson 0002, quiz 0002).

## Working notes
- 2026-11-08: lesson 0001 written (8 min, requested "short"). Quiz 0001 taken in chat (submission s1): 4/4 correct, no misconception shown.
- Knows: loop exit on no tool call, max_turns counting, max_tokens = truncated, result only on success.
- Not yet covered: refusal, pause_turn, model_context_window_exceeded handling; empty end_turn; subagent/budget caps in depth.
- 2026-11-16: cheat sheet `cheatsheets/agent-loop-stopping.html` made (scope: lesson 0001, O1). No weak topic yet, so it stresses M1/M2 traps, max_turns counting (+1 for final reply) and result subtypes. grades/0001-s1.json is present again (4/4).
- 2026-11-16: cheat sheet `cheatsheets/agent-loop-stopping.html` rebuilt from planner plan `drafts/plans/agent-loop-stopping.md`: shorter, Terms and trap boxes replaced by a signals table and a twists table; stresses truncation (M2), max_turns N vs N+1 and subtype-first. Gaps reported: refusal/pause_turn/stop_sequence, context-exceeded recovery, error_during_execution cause, empty end_turn, state left after a capped run.
- 2026-11-15: learner pasted quiz 0001's "done" item (q1) with no question. grades/ is empty (0001-s1 grade removed), so treated quiz 0001 as possibly being retaken: no answer given, item-specific hints only.
- 2026-11-16: progress review given. Weak topics named: none (only graded quiz is 0001, 4/4). Flagged as untested: refusal, pause_turn, stop_sequence, context-window-exceeded handling, empty end_turn, subagent/budget caps; mission goals 2 and 3 (predicting skill/subagent changes, reading bench results) not yet taught. Suggested next: /teach on the remaining stop reasons and their handling.
- 2026-11-17: lesson 0002 (O2, 15 min requested, about 18 by word count) written: what an agent harness does. Quiz 0002 (5 items) and key written, not yet taken. Ties to mission goal 2: duty -> symptom -> knob table for predicting config changes. Not covered: concurrency of read-only vs state-changing tools, permission modes in detail, long-running-agent harness design.

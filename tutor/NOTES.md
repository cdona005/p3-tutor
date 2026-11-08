# Notes

## Learner
- Name unknown. CS student (CSCI 498E/598E course). Wants bullets, concise first, depth on request; relate to CS; direct feedback, no praise (see PREFERENCES.md).
- Learning agents for a class on agentic AI (CSCI 498E/598E). MISSION.md confirmed by the learner (Why, Success and Out-of-scope all accepted as written, 2026-11-08).

## Misconception ids
- M1: an agent is done when its text says "done" (completion read from wording, not tool calls).
- M2: any stop that is not tool_use means the task finished (ignores max_tokens, truncation).

## Objectives
- O1: how an agent loop decides to stop (lesson 0001, quiz 0001).

## Working notes
- 2026-11-08: lesson 0001 written (8 min, requested "short"). Quiz 0001 taken in chat (submission s1): 4/4 correct, no misconception shown.
- Knows: loop exit on no tool call, max_turns counting, max_tokens = truncated, result only on success.
- Not yet covered: refusal, pause_turn, model_context_window_exceeded handling; empty end_turn; subagent/budget caps in depth.

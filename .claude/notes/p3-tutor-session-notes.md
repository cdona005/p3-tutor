# P3 tutor: session notes for other agents

Updated 2026-11-16. Written by the Builder session.

## State
- Step: c3-split, quick rounds. c1-skills and c2-review are snapshotted (configs/) and their major reviews written.
- Skills in tutor/.claude/skills/: teach, tutor, quiz, grade (all built in c1-skills rounds 1-7).
- tutor/CLAUDE.md routes questions to /tutor, quizzes to /quiz, grading to /grade, lessons to /teach.
- c2-review Round 1: built subagent grade-reviewer (tutor/.claude/agents/grade-reviewer.md); grade skill runs a review loop (draft in drafts/grades/, at most 2 passes, record in review-records/).

- c2-review Round 2: built subagent quiz-reviewer (tutor/.claude/agents/quiz-reviewer.md); quiz skill runs a review loop (drafts/quizzes + drafts/keys, at most 2 passes, record review-records/NNNN-quiz.md). Checks that items test ideas a lesson teaches in its main text (student's ask); in the bench quiz workspace there is no lesson, so it falls back to the objective's core.

- c2-review Round 3: built subagent lesson-reviewer (tutor/.claude/agents/lesson-reviewer.md, one reviewer with four sections, has WebSearch/WebFetch for fact-checks); teach skill runs a review loop (drafts/lessons/, at most 2 passes, record review-records/NNNN-lesson.md). Teach scenario limit is 45 min / 200 turns: check run.json for timeout after the next teach run.

- c3-split Round 1: built subagent lesson-planner (tutor/.claude/agents/lesson-planner.md, tools Read/Glob/Grep/Write); teach step 3 starts it after sources are chosen, plan goes to drafts/plans/NNNN.md, teach writes the draft from the plan to each section's word budget. Reviewers from c2-review unchanged. c2 major review asked next for more quiz items, mostly mcq (not yet acted on).

- c3-split Round 2: built skill cheatsheet (tutor/.claude/skills/cheatsheet/SKILL.md), a new SKILL not a subagent, at the student's request; tutor/CLAUDE.md routes study-sheet requests to /cheatsheet. The bench never starts it, so only live tries show it; its With and without needs a live try, not a bench run. Student said the planner-made lesson was well written, more detailed, a little harder to read.

- c3-split, second "Round 2" (duplicate heading, the student's): built subagent cheatsheet-planner (tutor/.claude/agents/cheatsheet-planner.md); cheatsheet skill step 4 starts it, plan at drafts/plans/<slug>.md. Student said the cheat sheet was hard to read and only restated the lesson. Live-try only; the bench never runs /cheatsheet.

- c3-split Round 4: built subagent lesson-designer (tutor/.claude/agents/lesson-designer.md, tools Read/Glob/Grep/Edit/Write, edits the draft in place); teach step 4 leaves figure placeholders, step 5 starts the designer, then review loop (step 6). Pipeline order: lesson-planner -> teach writes draft -> lesson-designer -> lesson-reviewer loop -> final. Student said the planner-built cheat sheet is much better. Check run.json for time/turn limits after the next teach run (45 min / 200 turns).

- c3-split Round 5: built skill progress-review (tutor/.claude/skills/progress-review/SKILL.md) at the student's request; routed from tutor/CLAUDE.md and the tutor skill's redirect line. Chat-only output, never opens keys/. Bench never runs it, live tries only. Student said the lesson-designer's figures are better than without it.

- c3-split Round 6: built subagent lesson-writer (tutor/.claude/agents/lesson-writer.md, tools Read/Glob/Grep/Write/WebSearch/WebFetch). The 'voice of a lesson' rules moved from teach/SKILL.md into the writer. Teach pipeline now: lesson-planner -> lesson-writer (draft, figure placeholders) -> lesson-designer -> lesson-reviewer loop -> final lesson. Student said progress-review needs more course material to be useful.

- c3-split Round 7: built subagent references-finder (tutor/.claude/agents/references-finder.md), two modes: find (teach step 2, before the planner; writes drafts/sources/NNNN.md and RESOURCES.md) and check (teach step 6, after the designer; writes drafts/sources/NNNN-check.md, teach fixes the draft). Teach pipeline now: finder(find) -> planner -> writer -> designer -> finder(check) -> reviewer loop -> final. Student unsure the writer step was worth its cost; the full pipeline cost is ~3M tokens, 10.6 min in the last run (before the finder).

## Open points
- The student's PREFERENCES.md asks for concise feedback; their c1 review says short feedback on missed items was not enough. The checklist in grade-reviewer.md (check 11) encodes the c1 review's wish. PREFERENCES.md is the student's to edit.
- reviews/components.md: the grade entry says Round 8 (with) but c1-skills.md has only Round 7; the student owns that line.
- reviews/c1-skills.md heading "### Round  7" has two spaces; p3 check may miss it.
- Student-reported: Claude Code predicts the learner's typed answer during quizzes (shows answers); not a tutor issue.

## Rules in force
- Do not write the student's parts of reviews/ (thoughts, ratings, Purpose/Review/Kept in final).
- Ask before any p3 bench run (cost) and before committing or pushing.
- Never credit Claude in files or commits.

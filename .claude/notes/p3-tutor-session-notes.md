# P3 tutor: session notes for other agents

Updated 2026-11-13. Written by the Builder session.

## State
- Step: c2-review, quick rounds. c1-skills is snapshotted (configs/c1-skills) and its major review is written.
- Skills in tutor/.claude/skills/: teach, tutor, quiz, grade (all built in c1-skills rounds 1-7).
- tutor/CLAUDE.md routes questions to /tutor, quizzes to /quiz, grading to /grade, lessons to /teach.
- c2-review Round 1: built subagent grade-reviewer (tutor/.claude/agents/grade-reviewer.md); grade skill runs a review loop (draft in drafts/grades/, at most 2 passes, record in review-records/).

- c2-review Round 2: built subagent quiz-reviewer (tutor/.claude/agents/quiz-reviewer.md); quiz skill runs a review loop (drafts/quizzes + drafts/keys, at most 2 passes, record review-records/NNNN-quiz.md). Checks that items test ideas a lesson teaches in its main text (student's ask); in the bench quiz workspace there is no lesson, so it falls back to the objective's core.

- c2-review Round 3: built subagent lesson-reviewer (tutor/.claude/agents/lesson-reviewer.md, one reviewer with four sections, has WebSearch/WebFetch for fact-checks); teach skill runs a review loop (drafts/lessons/, at most 2 passes, record review-records/NNNN-lesson.md). Teach scenario limit is 45 min / 200 turns: check run.json for timeout after the next teach run.

## Open points
- The student's PREFERENCES.md asks for concise feedback; their c1 review says short feedback on missed items was not enough. The checklist in grade-reviewer.md (check 11) encodes the c1 review's wish. PREFERENCES.md is the student's to edit.
- reviews/components.md: the grade entry says Round 8 (with) but c1-skills.md has only Round 7; the student owns that line.
- reviews/c1-skills.md heading "### Round  7" has two spaces; p3 check may miss it.
- Student-reported: Claude Code predicts the learner's typed answer during quizzes (shows answers); not a tutor issue.

## Rules in force
- Do not write the student's parts of reviews/ (thoughts, ratings, Purpose/Review/Kept in final).
- Ask before any p3 bench run (cost) and before committing or pushing.
- Never credit Claude in files or commits.

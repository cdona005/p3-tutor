---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict and feedback for every answer, a summary, learning records for what the answers show - and offer a practice quiz on the topics they got wrong. Use it for every request to grade or mark a submission, and when the learner hands in answers to a quiz.
argument-hint: "Which submission should I grade?"
---

# Grade

You grade the learner's answers in this workspace, over many sessions.
You do one job: a verdict and feedback on every answer of one submission, written for this learner, and an offer to practice what they missed.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.

When the learner hands in a complete set of answers to a quiz you gave them in the chat, record the answers first as `submissions/sN.json` with the next number, exactly as `FORMATS.md` shows, and grade that submission.
A learner who offers one answer to check before handing the quiz in is not asking for a grade: do not write a submission or grade it, and do not confirm or rule out the answer; say that you will give feedback on every answer once they hand the quiz in.

A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## The workspace

The current directory is the workspace root, and every workspace path below is relative to it.
This skill reads the grading guide kept with the teach skill, at `.claude/skills/teach/references/GRADING.md`; never write anything under `.claude/`.

| Path | What it is | Who writes it |
|---|---|---|
| `FORMATS.md` | the contract for every file a script reads | no one; follow it exactly |
| `MISSION.md` | why the learner is learning this | you, with the learner's agreement |
| `PREFERENCES.md` | how the learner likes to learn and to get feedback | the learner only |
| `NOTES.md` | what the learner knows and does not, and your working notes | you |
| `learning-records/` | what the learner has shown they learned | you |
| `lessons/` | the lessons the learner has been given | you |
| `quizzes/`, `keys/` | the quiz and its answer key | the quiz skill |
| `submissions/` | the learner's answers to a quiz | the bench, or you from the chat |
| `grades/` | your verdicts and feedback on a submission | you |

Any of these may be missing; create a folder the first time you need it.

## Read first, every time

Before you grade, read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short), then `.claude/skills/teach/references/GRADING.md`.
Then read the quiz, its key, the submission, and the lesson on the quiz's objective if there is one.
Use Read, Glob and Grep to look around and Write to create files; no part of this job needs the shell.

## Grade

1. Grade every item, including those left unanswered: a verdict judged on what the answer means and not on its wording, the misconception it shows if any (never an id you invented), and feedback written for this learner in the way `PREFERENCES.md` asks.
2. Write `grades/NNNN-sN.json` exactly as `FORMATS.md` shows, with a summary that says what the learner has down, the one thing to work on next, and a concrete next step.
3. Write a learning record for what the grades show, an understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and update `NOTES.md`.
4. Finish with a short message: the summary and the one next step.

## Offer a practice quiz

If any answer was `partial` or `wrong`, end your final message by offering a short practice quiz on those topics: name the topics, in the learner's words as far as you can, and ask if they want it.
The offer is a question and not an action: do not write the quiz yourself; when they say yes, it is made by `/quiz`, on those topics, with fresh items that do not repeat the graded ones.
If every answer was correct, offer nothing of the kind; name the next idea worth learning instead.
Never put an answer to a quiz item that is still open in the message.

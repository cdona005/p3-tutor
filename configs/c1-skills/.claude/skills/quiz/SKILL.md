---
name: quiz
description: Write a quiz and its answer key for the learner in this workspace, on an objective, at the learner's level and tied to their mission; also show a quiz to the learner in the chat when they want to take it. Use it for every request for a quiz or to be tested.
argument-hint: "What should the quiz cover, and how many questions?"
---

# Quiz

You write quizzes for the learner in this workspace, over many sessions.
You do one job: a quiz of the requested number of items on an objective, with its answer key, that shows the learner and you where they stand.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.

A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## The workspace

The current directory is the workspace root, and every workspace path below is relative to it.
This skill reads the quiz guide kept with the teach skill, at `.claude/skills/teach/references/QUIZZES.md`; never write anything under `.claude/`.

| Path | What it is | Who writes it |
|---|---|---|
| `FORMATS.md` | the contract for every file a script reads | no one; follow it exactly |
| `MISSION.md` | why the learner is learning this | you, with the learner's agreement |
| `PREFERENCES.md` | how the learner likes to learn | the learner only |
| `NOTES.md` | what the learner knows and does not, and your working notes | you |
| `learning-records/` | what the learner has shown they learned | you |
| `lessons/` | the lessons the learner has been given | you |
| `quizzes/`, `keys/` | quizzes, and their answer keys | you |
| `grades/` | verdicts and feedback on earlier submissions | you |

Any of these may be missing; create a folder the first time you need it.

## Read first, every time

Before you write, read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short), then `.claude/skills/teach/references/QUIZZES.md`.
Then read the lessons on the objective, and the earlier quizzes, keys and grades, to see what has been asked and which misconceptions the learner has shown.
Use Read, Glob and Grep to look around, Write to create files and web search to read a source; no part of this job needs the shell.

## Write the quiz

1. Pin down the objective, its id and the number of items asked for; use the id the workspace already has for it.
2. Find the objective's core: in its lessons or, when there are none, in a high-trust source you search for and read, never in your own memory.
3. Choose the item types and write the items as `references/QUIZZES.md` describes: one tested idea per item, mostly application in a new case, difficulty spread through the quiz, and every distractor a misconception that someone would really hold.
4. Write the quiz to `quizzes/NNNN.json` and its key to `keys/NNNN.json` with the next number, exactly as `FORMATS.md` shows.
5. Answer every item yourself from its stem alone, without looking at your key, and rewrite any item that lacks a single defensible answer, that can be read two ways, or whose correct option repeats words from its stem.
6. Note in `NOTES.md` anything new you learned about the learner.
7. Finish with a short message: the quiz's path, its objective, and how many items; say if it is ahead of the lessons.
   Never put an answer in the message.

## Giving a quiz in the chat

When the learner wants to take a quiz now, show its title and each item's stem and options, and never anything from `keys/`.
Collect their answers; for grading them, ask for it by name (`/grade`).

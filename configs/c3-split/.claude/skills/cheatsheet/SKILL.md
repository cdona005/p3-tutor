---
name: cheatsheet
description: Make a study document for an exam from the lessons the learner has been given - the core ideas, terms, procedures and comparisons, the traps they have fallen into, and fresh self-test questions - as a self-contained HTML cheat sheet in cheatsheets/. Use it when the learner asks for a cheat sheet, a study guide, a review sheet or something to study for an exam.
argument-hint: "What should the cheat sheet cover (a lesson, an objective, an exam)?"
---

# Cheat sheet

You make study documents for the learner in this workspace, over many sessions.
You do one job: one cheat sheet that compresses what the learner has been taught into something they can study from before an exam, and that tests them as they go.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.

A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## The workspace

The current directory is the workspace root, and every workspace path below is relative to it.
Never write anything under `.claude/`.

| Path | What it is | Who writes it |
|---|---|---|
| `FORMATS.md` | the contract for every file a script reads | no one; follow it exactly |
| `MISSION.md` | why the learner is learning this | you, with the learner's agreement |
| `PREFERENCES.md` | how the learner likes to learn | the learner only |
| `NOTES.md` | what the learner knows and does not, and your working notes | you |
| `learning-records/` | what the learner has shown they learned, and the misconceptions they have shown | you |
| `lessons/` | the lessons the learner has been given: the source of every fact on the sheet | you |
| `quizzes/`, `grades/` | the quizzes the learner has taken, and the feedback on their answers | you |
| `cheatsheets/` | study documents and one-page references | you |
| `keys/` | the answer keys | no one in this job: leave it closed |

Any of these may be missing.

## Read first, every time

Read `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short), then `FORMATS.md` for what a script reads and the lesson template's look at `.claude/skills/teach/references/lesson-template.html`.
Then read the lessons the request covers, in full: the lesson the learner names, the lessons on the objective they name, or, when the request names neither, every lesson in `lessons/`.
Read the grades in `grades/` and the quizzes in `quizzes/` that go with those lessons, and the files already in `cheatsheets/`.
Never open `keys/`: the sheet's questions come from the lessons, and a sheet that has read a key can hand out a quiz answer without meaning to.
Use Read, Glob, Grep and Write; no part of this job needs the shell.

## Make the sheet

1. **Pin down the scope:** which lessons and objectives the sheet covers, and what the exam or the occasion is, if the request says.
   If there are no lessons on the scope, make no sheet: say so in your message and offer a lesson on it.
2. **Gather the content from the lessons only:** never add a claim, figure or example that the lessons do not make.
   If the scope has a gap that an exam would probably test, say so in your message and offer a lesson, and do not fill it from memory.
3. **Find where the learner is weak:** from the learning records, the grades and `NOTES.md`, the misconceptions they have shown and the topics they lost points on.
   Those topics get the most room on the sheet.
4. **Plan the study guide:** start the `cheatsheet-planner` subagent with the Agent tool.
   Its task message names the scope (the lessons or objectives), the exam or occasion if the request names one, and the sheet's slug, and nothing else.
   Wait for its report before you do anything else; the plan it writes to `drafts/plans/<slug>.md` ranks the ideas, names the one mental model, the contrasts an exam twists and what to cut, and holds the self-test questions and the layout.
5. **Write the sheet** from the plan to `cheatsheets/<slug>.html` as one self-contained HTML page in the lesson template's look, designed to be read in two minutes at a time and printed on one or two pages.
   Follow the plan where it differs from "What the sheet holds" below: the plan decides what goes on the sheet, in what order, how long each block is and what is left out.
   If a sheet on the same scope already exists, update it in place instead of making a second.
6. **Check it:** every item traces to a lesson, no question repeats a quiz item, nothing on it gives away a quiz answer for a quiz the learner has not yet handed in, and nothing the plan cut crept back in.
7. **Note** in `NOTES.md` that the sheet exists and which topics it stresses.
8. **Finish** with a short message: the sheet's path, the lessons it covers, the topics it stresses and why, and any gap the plan named.

## What the sheet holds

- **Know cold:** one line for each core idea, in the order the lessons teach them, each with a link to the lesson's section that explains it, as a relative link such as `../lessons/NNNN-<slug>.html#<heading-id>`.
- **Terms:** each term the lessons define, with its definition in one line.
- **How it works:** the procedures, formulas, sequences and comparisons, as numbered steps and tables; a small inline SVG figure only where a picture compresses a mechanism better than words, with a `<title>` and a caption.
- **Traps:** each misconception the learner has shown or the lessons name, with the wrong belief, why it is tempting, and the correct idea, in a line or two each.
  Put the learner's own misconceptions first.
- **Self-test:** eight to twelve fresh questions that mix recall, application in a new case and explaining why, each with its answer hidden in a `details` element, so the learner tries before looking.
  Spread them across the scope and weight them toward the weak topics.
- **Where to reread:** for each weak topic, the lesson section to read again.

Follow `PREFERENCES.md`: the kind of example the learner relates to, bullet points where it asks for them, and its tone.
A cheat sheet is a reference and not a lesson: no warm-up, no praise, no story, no paragraph longer than two sentences.
The page is self-contained as `FORMATS.md` says for lessons: no stylesheet, script or image from the web, and it works in light and dark mode and prints well.

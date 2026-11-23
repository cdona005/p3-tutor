# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c2-review/20261113-232251-agent-architecture-m30-r1

**My thoughts:**

I thought the lesson was well written, but try to have a planning subagent to see if it helps the lesson quality

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: You asked for a planning subagent to see if it helps lesson quality; lesson-planner writes drafts/plans/NNNN.md (the win, the objective's ideas, sections in order with a word budget summing to minutes times 150, and each section's example and practice), and the teach skill now starts it after choosing sources and writes the draft section by section from the plan.

### Round 2

**Run:** bench/runs/_live/20261116-191549-agent-architecture-m30-r1

**My thoughts:**

This lesson was written well and seemed to go over all of the main topics in more detail than before, making it a little harder to read but the information was better. Add a cheatsheet skill to make a documnet to study for exams

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/cheatsheet/SKILL.md, tutor/CLAUDE.md
- Why: You asked for a cheat sheet skill to make a study document for exams, so /cheatsheet builds a self-contained sheet from the lessons (core ideas, terms, traps from your learning records and grades, fresh self-test questions, links back to lesson sections), and CLAUDE.md routes study-sheet requests to it.

### Round 3

**Run:** tutor/cheatsheets/agent-loop-stopping.html

**My thoughts:**

The cheatsheet is hard to read and does not do a good job summarizing important points in the lesson, more just restating them. Make a planning agent for cheatsheet to make it more like a study guide that would help a student prepare for a test.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/cheatsheet-planner.md, tutor/.claude/skills/cheatsheet/SKILL.md
- Why: You found the cheat sheet hard to read and mostly a restatement of the lesson, so cheatsheet-planner now ranks the ideas by what an exam asks and where you are weak, names the one mental model and the contrasts an exam twists, decides what to cut, and sets the self-test and a reading budget, and the cheatsheet skill writes the sheet from its plan.

### Round 4

**Run:** tutor/cheatsheets/agent-loop-stopping.html

**My thoughts:**
The cheatsheet is much better and more helpful. Make a design subagent for teach to have better visuals in the lessons.

**What changed:**
- Kind: new subagent
- Files: tutor/.claude/agents/lesson-designer.md, tutor/.claude/skills/teach/SKILL.md
- Why: You asked for a design subagent for better lesson visuals, so lesson-designer now draws the figures as inline SVG and shapes the layout without changing what the lesson says, and the teach skill leaves figure placeholders in the draft and starts the designer before the reviewers read it.


### Round 5

**Run:** bench/runs/_live/20261116-204242-agent-architecture-m30-r1

**My thoughts:**
The figures look good and are better than without the design agent. Make a skill to give the students an update on where they are in the course and what topics they are not good at, call it progress-review.

**What changed:**
- Kind: new skill
- Files: tutor/.claude/skills/progress-review/SKILL.md, tutor/CLAUDE.md, tutor/.claude/skills/tutor/SKILL.md
- Why: You asked for a skill that updates the student on where they are in the course and what they are weak on, so /progress-review builds that from the mission, lessons, grades and learning records only (weakest topics first, with the quiz item that shows each), ends with one next step, and CLAUDE.md and the tutor skill route progress questions to it.

### Round 6

**Run:** tutor/NOTES.md line 21

**My thoughts:**
The progress review would be more helpful I think if there was more course material, right now its only one lesson and quiz so it cannot do much. Add a writer subagent to teach to write the lesson from the plan.

**What changed:**
- Kind: new subagent
- Files: tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: You asked for a writer subagent to write the lesson from the plan, so lesson-writer now writes the draft section by section to each word budget, with the voice rules from your Rounds 1 and 2 moved into it from the teach skill, and teach starts it between the planner and the designer.

### Round 7

**Run:**  bench/runs/_live/20261116-213001-agent-architecture-m30-r1

**My thoughts:**
The lesson seems slightly better, I am not sure if it is worth the cost though. Add a reference finder subagent to teach to find and check references in lessons


**What changed:**
- Kind: new subagent
- Files: tutor/.claude/agents/references-finder.md, tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: You asked for a references subagent to find and check the references in lessons, so references-finder now finds, opens and records the sources with the claims they back before planning, and checks every link in the draft against its page afterward, with the teach skill starting it in both places and the writer citing from its sources file.

### Round 8

**Run:** bench/runs/_live/20261116-223456-agent-architecture-m30-r1

**My Thoughts:**
This skill raised the time from 10.6 to 28.2 minutes and used 20% more tokens. Ensuring the sources are correct is important, but for the cost the subagent is not worth the time.

**What Changed:**
- Kind: other
- Files: tutor/.claude/agents/references-finder.md (deleted), tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: Your c3-split Round 8 found the references finder not worth raising the teach run from 10.6 to 28.2 minutes and its tokens by 20%, so final drops it: teach searches for and chooses its own sources again, the check step is gone, and the writer cites from RESOURCES.md.

## Major review

**Run:** bench/runs/c3-split/20261116-232334-agent-architecture-m30-r1

**Live tries:**

I had the tutor make a lesson about what the harness does. It is similar to the project's lesson and the same quality and writing style. 

### Lesson

#### Technical correctness and facts

Rating: 5

I do not see anything incorrect in the lesson, the review agent did change a few facts, like the quadratic cost claim, but I do not think any of the points the reviewer caught would have caused a major misconception with the learning objective.

#### Pedagogy

Rating: 5

I think the lesson had good pace and order of topics. It starts with the overall description of context, then goes in more depth for different parts of the context and how it grows. It was easy to read and had a lot of important topics, and went into depth more for important topics like clearing and compaction. 

#### Alignment with the learning goal

Rating: 5

The lesson taught everything I can think of related to the lesson's learning goals. It covered in depth how context grows, the context window, how context changes between steps and sessions, and how agents keep notes for important topics that can be read in sessions if the model needs that context.

#### Overall quality

Rating: 5

There is nothing I would change with this lesson, it writes the way I asked it to and has all of the important information to meet the learning goal.

### Compared with the previous step

The lesson is slightly better, but I do not think the cost of having multiple subagents is worth how small of a difference I noticed.

### What the next step should fix

Limit cost while not changing the quality of the tutor enough for a student to notice.

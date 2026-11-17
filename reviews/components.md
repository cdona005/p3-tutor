 # Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: Make lessons for the user based on user feedback and preferences
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: It did well, it followed my instructions for how I wanted it changed and how to write the lessons. It took a few iterations but I can easily read and understand the lessons now.
- Kept in final: TODO

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Answer the users questions without answering a quiz question before the quiz is submitted.
- With and without: reviews/c1-skills.md, Round 5 (without) and Round 6 (with)
- Review: The actual tutor is helpful and answered questions well, but the guardrails are not effective. For quiz 0001.json, I asked question 1 to the agent but change the edit_file to read_file toolcall, which completely bypassed the guardrails and it gave me the answer immediately without even looking at the quiz status or keys.
- Kept in final: TODO

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: Write quizzes and the key for the user.
- With and without: reviews/c1-skills.md, Round 6 (without) and Round 7 (with)
- Review: I thought the quizzes were good, after reading the lesson I could easily answer the questions.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: Grade the quizzes made by the quiz skill and give feedback to the user.
- With and without: reviews/c1-skills.md, Round 7 (without) and Round 8 (with)
- Review: The reviews were not helpful to me, they were short and did not explain well. THey also did not explain everything that was missed. 
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Ensure the grade agent follows my personilaztion and gives accurate and detailed feedback.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: The grade reviewer did well and followed my feedback about wanting more detailed feedback and tried to point to lessons.
- Kept in final: TODO

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Ensure the quiz tests about all important topics and has no errors
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: The quiz reviewer tried to make the questions test about more of the topics in the lesson, but I do not feel like it changed enough to make more than one pass with the reviewer worth the cost.
- Kept in final: TODO

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Ensure the lesson covers all topics in the learning objective and is all accurate.
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: It found some small errors, but nothing about correctness or covering the learning objective. It did add more information about context and compacting, which I asked for in c1.
- Kept in final: TODO

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: Plan the lesson before writing anything
- With and without: reviews/c3-split.md, Round 1 (without) and Round 2 (with)
- Review: It made the lesson slightly harder to read, but it made the lesson go over the most important topic in more detail.
- Kept in final: TODO

### cheatsheet

- Kind: skill
- Step added: c3-split
- Purpose: Make the student a study guide.
- With and without: TODO
- Review: The first pass was bad, it was hard to read and seemed more like a lesson recap than a study guide.
- Kept in final: TODO

### cheatsheet-planner

- Kind: subagent
- Step added: c3-split
- Purpose: TODO
- With and without: reviews/c3-split.md, the second "Round 2" (without) and the round after it (with)
- Review: The second agent made the cheat sheet helpful for studying and has all of the necessary information needed from the lesson. I liked that it adds a most important section to the cheatsheet and how the document is layed out.
- Kept in final: TODO

### lesson-designer

- Kind: subagent
- Step added: c3-split
- Purpose: TODO
- With and without: reviews/c3-split.md, Round 4 (without) and Round 5 (with)
- Review: TODO
- Kept in final: TODO

### progress-review

- Kind: skill
- Step added: c3-split
- Purpose: TODO
- With and without: TODO
- Review: TODO
- Kept in final: TODO

### lesson-writer

- Kind: subagent
- Step added: c3-split
- Purpose: TODO
- With and without: reviews/c3-split.md, Round 6 (without) and Round 7 (with)
- Review: TODO
- Kept in final: TODO

### references-finder

- Kind: subagent
- Step added: c3-split
- Purpose: TODO
- With and without: reviews/c3-split.md, Round 7 (without) and Round 8 (with)
- Review: TODO
- Kept in final: TODO

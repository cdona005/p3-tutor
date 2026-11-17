# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261108-185311-agent-architecture-m30-r1

**My thoughts:**

The grade skill did not give useful feedback and missed giving feedback on some problems. I want the feedback to be more in depth and point to where I could read more about the question's answer, like in a lesson.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: Your c1 review found feedback with no pointer to a lesson, a summary that skipped the partial item q5, and answers that stated the fix without explaining it; a grade-reviewer with those checks reads the draft in drafts/ with a fresh context, and the grade skill now revises at most twice and writes review-records/NNNN-sN-grade.md.

### Round 2

**Run:** bench/runs/_live/20261113-183436-agent-architecture-m30-r1

**My thoughts:**

The grading feedback is much more robust and goes over all of the questions missed. It is a little long, but I do not see that as a problem for test feedback. Make a quiz reviewer to ensure the quiz is written only about topics that are covered in lessons so the grading skill does not say that the lesson does not cover this topic.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: You asked for a quiz reviewer so the quiz tests only what the lessons teach; quiz-reviewer names the lesson heading that teaches each item and flags items whose idea is missing or only in a collapsed dropdown (your c1 q4), and the quiz skill now drafts in drafts/, revises at most twice and writes review-records/NNNN-quiz.md.

### Round 3

**Run:** bench/runs/_live/20261113-211056-agent-architecture-m30-r1

**My thoughts:**
The quiz was easy to read and if you understand the information, you should get a good grade on the quiz. I would not change anything for the quiz, make a reviewer for teach to ensure the lessons are the correct length, meet the learning objectives, and have no false information.

**What changed:**
- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: You asked for a teach reviewer that checks length, the learning objective and false information; lesson-reviewer has four separate sections (facts checked against named sources, pedagogy, alignment with the objective, overall quality with a length estimate), including your c1 findings on thin coverage of compaction and ideas buried in a dropdown, and the teach skill now drafts in drafts/lessons/, revises at most twice and writes review-records/NNNN-lesson.md.

## Major review

**Run:** bench/runs/c2-review/20261113-232251-agent-architecture-m30-r1

**Live tries:**
Below is a chat I had with the tutor, i copied and pasted a quiz question exactly as written and the tutor just gave me the answer without any questioning or hesitation. I am not sure why the guardrails are worse now, but it will give any quiz question's answer now.
I beleive that run did not load the tutor skill for some reason, so I tried again and with the exact copy paste it did not give the answer, but when I copied the question and removed all of the json formatting and '/'s, it answered without questioning the quiz. 

"stem": "A harness exits its loop as soon as the reply text contains the word \"done\". The model replies: \"Done reading the file, now fixing the typo\", and the reply includes an edit_file tool call. What happens?",
      "options": [
        {"id": "a", "text": "The loop raises an error for mixed text and tool call"},
        {"id": "b", "text": "The loop ignores the word and runs until max_turns"},
        {"id": "c", "text": "The loop exits early and the edit never gets run"},
        {"id": "d", "text": "The loop runs the edit and then exits on the next"}]

c. The loop exits early and the edit never runs.
The exit check reads only the reply text. "Done reading the file..." matches, so the harness stops before it runs the edit_file call in that same reply. That's why a harness should decide when to stop from the reply's structure (it ends when there are no tool calls), not from keywords in the text.
Strictly, "Don' s capitalized, so a case-sensitive check for "doe" wouldn't match. The question clearly means a case-insensitive check. Option d's text also looks cut off ("on the


### Lesson

#### Technical correctness and facts

Rating: 5

I did not see any incorrect facts in the lesson. I also checked the sources and the links worked and were correct for the context.The facts were well explained and the use of charts and examples, like explaining how context grows, was useful.

#### Pedagogy

Rating: 5

I liked how the lesson was written and the topics seemed to be ordered well, like starting at what context is, then explaining how and why it grows, then how to reduce the size of the context window. The lesson was easy to read, the quiz questions were placed at the end of each section, and the examples made the topics easier to understand. The python list example makes seeing how context grows and what the model sees more concrete and easier to understand.

#### Alignment with the learning goal

Rating: 5

The lesson covered the learning objective well. It went over what is in the context windon in depth, including why and how context grows quickly and used example token counts to show how each request includes the last request's tokens. The example at the end then a similar question right after is also good to test the student, showing them if they learned from the lesson or if they need to go through it again.

#### Overall quality

Rating: 5

There is nothing I would change about this lesson. It is written well, the topic order makes sense, it is easy to read, and the layout is what I would want.

### Quiz

#### Difficulty

Rating: 4

The quiz was written well and was covered in the lesson, the only thing I would change is less written questions and add more multiple choice, for quizzes from LLM's I would prefer multiple choice so I know the options and what the LLM is looking for.

#### Coverage of the lesson's core

Rating: 4

It went over most of the big topics, but it was very broad and the lesson went into a lot of detail, so I think the quiz should have had more questions that check to see if the student learned all of the important information in the lesson.

#### Wording and possible misreadings

Rating: 4

On q1, I misread the question and did not realize what the question implied when it said Nothing is saved anywhere. I might have read too quickly, but saying nothing is saved meant to me what hte lesson was trying to convey that the servers do not save the chats and the model only knows what is appended to the chat. I did not assume that also meant no notes are saved, and the prompt sounded like a fact the LLM would save in notes about the student.

#### Writing quality

Rating: 5

I would not change anything about how the quiz is written, I did not notice anything about the writing quality.

#### Alignment with the learning goal

Rating: 4

Most of the learning objectives were covered, but I think more questions are needed to cover things like what is kept between steps and sessions, as the quiz only has 2 questions about between sessions and does not really cover between steps besides adding up the token count, which I am not sure is really relevant to the learning objective. 

### Feedback

#### Useful

Rating: 5

The feedback is more useful than c1 was and goes over the topic in more detail. Not having a lesson for the quiz that the feedback is from makes setting up this agent for my preferences much harder, as I want to see how it directs the student to the lesson but it just says that there is not a lesson that covers this topic yet, making that part useless.

#### Explains enough

Rating: 5

This would be better if it could point the student to the lesson, but it tried to and I cannot count that against the agent, that is an issue with the project design. I like how the agent explained simply why the answer was wrong and went over the correct answer, I would not change anything.

#### Personalized to how I like things explained

Rating: 5

The agent tried to get the personalization correct, but it was not able to with the project setup. However, it tried to point to a lesson and used CS comparisons when appropriate. I would not change anything.

### Compared with the previous step

The lesson and feedback were much better. The lesson goes more in depth and important topics and the feedback is more detailed and uses CS comparisons when it can. The quiz was good, I think it should be longer thought to cover all of the topics in the lesson.

### What the next step should fix

Make the quiz more questions with mostly multiple choice to check the student's knowledge on the lesson without making it unnecesarily long.

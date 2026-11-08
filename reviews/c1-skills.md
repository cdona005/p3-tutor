# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261104-191544-agent-architecture-m30-r1

**My thoughts:**

It is ok, I like that it related topics to traditional programming ideas. I could learn from it, but it seems pretty dry and technical, which makes reading all the way through difficult.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md
- Why: You found the lesson dry and technical to read through, so teach now has a "voice of a lesson" section: talk to one person, open each section with a problem, anchor ideas in CS analogies (which you liked), plain words before terms, and short stretches with a practice check.

### Round 2

**Run:** bench/runs/_live/20261104-195244-agent-architecture-m30-r1

**My thoughts:**

 It is noticably easier to read. It reads less technical and more conversation, which is better when trying to read an article and learn. It might have gone a little heavy on the CS comparisons, but i understood it well and the comparisons made sense to me.



**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md
- Why: You found the lesson easier to read but a little heavy on CS comparisons, so the voice section now rations analogies to at most one per idea, used only where they clarify.

### Round 3

**Run:** bench/runs/_live/20261104-221953-agent-architecture-m30-r1

**My thoughts:** 
The tutor for p01 did a good job I think, it did not point to one answer but the way it aasked questions made me know the right answer pretty quickly. The response was a little long, but the information was good.
For po2,  I feel like saying the right answer should align with other questions is too much help, especially if the student knew the answers to those other questions. It did not directly lead the student, but it still could end up leading them to the correct answer relatively easily. The response was a little long but not too bad.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/references/TUTORING.md
- Why: In tutor-p02 the reply said q5 and q6 "touch the same mechanism" so your answers there should agree with q2, which you found too much help; the tutoring guide now forbids pointing to other quiz items and sends the learner to their own notes and reasoning.

### Round 4

**Run:** bench/runs/_live/20261104-224647-agent-architecture-m30-r1

**My thoughts:**
The tutor's response for p01 seems very helpful. It gave ways to test the answers and used the questions wording to point out ways to eliminate other answers without giving any answers or hints outside of what the question says, which I do not think is wrong.
The tutor's response for p02 is fine, it doesnt give hints but doesn't seem as helpful as p01. It does do what it is supposed to do, I just do not think it would help me much.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/references/TUTORING.md
- Why: You found the tutor-p02 reply correct but not very helpful, so the guide now asks a declined quiz-answer reply to be specific to the item (its topic, the lesson section that covers it, the stem's wording, one question about the learner's reasoning) instead of a generic study routine.

### Round 5

**Run:** bench/runs/_live/20261104-225839-agent-architecture-m30-r1

**My thoughts:**
I think this round went well with the answers, I think it would be better if tutor was its own skill, add the skill and chege the CLAUDE.md to use this skill for tutor prompts


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md, tutor/CLAUDE.md
- Why: You asked for tutor to be its own skill with CLAUDE.md routing tutor prompts to it, so /tutor now answers chat messages and follows the same tutoring guide, and CLAUDE.md sends questions to /tutor and lessons, quizzes and grading to /teach.

### Round 6

**Run:** bench/runs/_live/20261104-230654-agent-architecture-m30-r1

**My thoughts:**
The tutor seems better, no changes needed. Make quiz a skill to see if it would output better quizzes

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md, tutor/CLAUDE.md
- Why: You asked for quiz to be its own skill to see if it writes better quizzes, so /quiz now writes the quiz and its key (with a self-check for items that can be read two ways or repeat words from the stem), and CLAUDE.md routes quiz requests to it.


### Round  7

**Run:** bench/runs/_live/20261104-231813-agent-architecture-m30-r1

**My thoughts:**
The quiz seems good, I think the difficulty is very reasonable and if the student understands the material they should get a good grade. Make a grading skill that also offers to make another similar quiz for students to practice with and get the topics they misunderstand down well

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md, tutor/CLAUDE.md, tutor/.claude/skills/quiz/SKILL.md, tutor/.claude/skills/tutor/SKILL.md
- Why: You asked for a grading skill that offers a practice quiz on the topics the learner missed, so /grade now grades every answer and ends by offering that quiz when any answer was partial or wrong; CLAUDE.md and the two skills that named /teach for grading now point to /grade.

## Major review

**Run:** bench/runs/c1-skills/20261108-185311-agent-architecture-m30-r1

**Live tries:**

I had the tutor make a lesson on when the agent loop exits. The lesson was a good length and was easy to read, the quizzes in the lesson seemed to help me remember what the lesson was about. 
When I asked for the lesson, the tutor told me that there was no mission.md written yet and to give me the information needed to write it. It took 3 prompts to get it to tell me what information mission.md wanted. I feel like this should have been an easy task and the tutor made it more difficult then it should have been.
I took the quiz after reading the lesson, and the model tried to predict what I would type in the response, which gave me the answers to the quiz questions (Figure 1). I am not sure how to fix this, my code in terminal started doing this recently and makes quizzes with claude kind of useless now if it is going to tell you the answers immediately. I think this is coming from Claude Code not the tutor, but this program is based on Claude Code so it would be an issue either way in this tutor. I asked claude how to turn it off and it does not know, so I am not sure if this can be changed.

**Figure 1**
![predicted output](/data/predicted.png)

### Lesson

#### Technical correctness and facts

Rating: 5
Live Try:
I did not see anything incorrect in the lesson. The way it explained why agents use no tool call as a reason to exit made sense, especially when comparing it to a while loop. I understood what the lesson wanted me to learn easily.

Run output:
The lesson the run made is much more in depth than the live try lesson, which is both goo and bad. There is more information in it and it seems to go into a little more depth than the live try lesson, but they are on different topics so it is difficult to compare. I did not see any incorrect information in the lesson, and it used a while loop again to explain how the context is appending to the new prompt.

#### Pedagogy

Rating: 4

Live Try:
I think the lesson was good, but not the best it could be. It was easy to read and I liked the questions in the lesson, they were easy but also tested if you understood what you read before the question. I am more likely to do questions like that over hard questions that take time to answer, I would just skip those or look at the correct answer. The examples it gave were good and what I asked for (using CS concepts to explain LLM topics), like comparing when an agent stops by using a while loop with the exit condition being the response not having a tool call.

Run output:
This lesson had a similar format to the live try lesson, and the questions in the lesson were also easy but made sure that you read the lesson to be able to answer the questions easily. It used a while loop comparison to how the prompt is constructed before it is sent to the model, which I found helpful. It made it easy to understand what is passed to the model for every prompt and why more tokens are used on every request.

#### Alignment with the learning goal

Rating: 5

Live Try:
I asked the tutor to make a lesson about when the agent loop stops, and that is what it made. The lesson did not go off-topic and only wrote about what makes the loop stop and why. It seemed like a reasonable level of difficulty, maybe a little easy for me but it did teach what I asked it to well, and the tutor does not know what section I am in, so it only knows 498/598. If i told it I was in 598, it might have made a slightly harder lesson.

Run output:
The lesson did explain what it was supposed to and did not go off-topic, but I think it should have put more emphasis on what compaction and clear do and what you need to ensure is saved when using them. It mentions that a risk of compaction is losing details that may be needed later, but it does not say what you can do to mitigate this and ways to compact without losing many details. I think the lesson should have a longer section about compacting and effective ways to use the tool.

#### Overall quality

Rating: 4

Live Try:
The tutor did a good job and did what it was supposed to do, this just is not really how I learn. To study, I basically only do a lot of practice problems. This is the best way I have found to gain confidence on exams and understand material better, so creating a lesson like this would not help me much. However, the lesson it created did follow my instructions and what I wanted from a lesson, and I could learn from it easily. 

Run output:
The tutor did what it was told to do, and the lesson was easy to read. It followed the instructions I gave it and outputted a lesson that follows that guidance well, but I think that it should have gone into more details about some of the topics in the lesson, like compaction and clearing tool calls.

### Quiz

#### Difficulty

Rating: 4

Live Try:
I do not think the quiz was too dificult, but question 4 I do not remember learning in the lesson at all. I would not have gotten this correct on a quiz, the lesson mentioned budget caps and does mention teh answer to q4, but only in a dropdown under a practice question which is easily missed. It did not go into any detail or explain what happens when one is reached, which is what question 4 was asking.

Run output:
I think this quiz was better than the live try. I immediately recognized all of the questions and either knew the answer or knew how to figure out the correct answer. From reading the objectives, I think it is a reasonable difficulty but without the lesson I cannot reliably say if the lesson covered the topics. 

#### Coverage of the lesson's core

Rating: 3

Live Try:
The questions covered the major points in the lesson, but I think a few more questions would have been helpful. Understanding how agents stop the loop and what can change that is important to using agents effectively, and more questions to ensure the student understands that well would be helpful.

Run output:
Most of the core topics were covered in the quiz, but I again think more questions would be helpful to the students. There are more topics the quiz could have covered, but without the lesson, it is hard to judge how well the quiz covers the lesson.

#### Wording and possible misreadings

Rating: 4

Live try: 
I understood the questions easily and did not see anything I would misread or not understand easily. The wording was consistent with the lesson and used the same topics, like when talking about why the agent saying 'done' does not work for ending the loop.

Run output:
I think the wording was fine, and I did not misread anything, but again without the lesson for this topic I cannot accurately compare the wording to the lesson, which could change this significantly.

#### Writing quality

Rating: 5

Live run:
The writing quality was good, there were no unusual words or typos. I have nothing I would change with how the quiz was written.

Run Output:
The writing was good, I do not have any issues with the writing quality and would not want anything chagned with how the quiz is written.

#### Alignment with the learning goal

Rating: 4

Live Run:
The quiz was mostly good for covering the learning goal. I think q4 was a little out of scope, it is related to the learning objective but I think the agent could have made a better section that was more aligned with the learning goal. I think going into tools in more depth would have been better than talking about max tokens and budget.

Run output:
It seems like the quiz covered the learning goal, but I think having the lesson would be helpful for judging this better. WIthout the lesson, I do not know what the student learned and what the learning goal is actually looking for, so from what I can tell the quiz tests on the learning goal but more specifics would be helpful.

### Feedback

#### Useful

Rating: 3

The feedback says what to look over and where the user struggled on the quiz, but it does not point to where to look to learn about it. 
In 0001-s1.json, it says that the user got q2 and q4 wrong and explains why it is wrong, which is useful, but as a student using this program I would want it to point me to the lesson or textbook to learn why the answer was wrong and refresh on the topic so I do not repeat the same mistakes. 0001-s1.json summary also mentions nothing about getting partial credit on q5, which wouldeasily be missed by a student. 0001-s1.json does better explaining the partial credit questions, but the summary is short for how much was missed.

#### Explains enough

Rating: 3

I think the LLM tried to follow that I want concise answers too much for the feedback. It did not seem to try to explain what was really wrong, and just gave the answer and what should have been including for partial credit questions or just stating the correct answer without explaining in depth why what the user put was wrong. 

#### Personalized to how I like things explained

Rating: 1

It did not seem to try to personalize much other than being short, which is not helpful for the feedback. For a quiz, I would either want a long description of why the answer was wrong or to be pointed to a reference to learn why I was wrong. For the partial credit questions, I would want longer explanations as to why what was missed was needed and how that impacts what the question asks.

### Tutor

#### Guardrails

Rating: 3

The agent seems to output helpful ways to solve problems without giving answers, like it p-01 and p-02 when the student asks for direct quiz answers. However, if the student does not say that they are asking about quiz questions and just restates the question themselves, the agent immediately outputs the answer for them. p03-p06 all are questions the student asked directly what the answer is and the model output the answer. I am not sure the best way to fix this, the LLM explaining answers to students is helpful but it could be misused. This also depends on how the graded quizzes are given and if students have access to the tutor during the quiz. If they do, the agent should check the quizzes and ensure the student is not asking for a quiz answer without telling the agent, but this wouldadd a lot of overhead and context that may not be required.

#### Personalization

Rating: 3

The LLM did not seem to try to personalize the answers to me for this section. I asked for short answers, CS-based comparisons, and only to give long answers if I ask a follow up question. All of the answers are longer than I would want for a first question, and p-06 uses a restaraunt analogy to explain the topic, which would have been a perfect time to follow the 'use CS-based comparisons' personalization I gave.

### Compared with the previous step

I think that the lesson changed the most for what I wanted. It made them easier to read and less like technical writing, used CS topics to explain how the topic works, and did not go too heavy on the CS comparisons. One thing I asked for with the quiz skill is for the agent to ask to make another quiz after I complete one, but it has not follow that at all. The tutor is better than before, I thought it was giving too much help when asking for a quiz answer that easily led the student to the answer, now it asks leading questions that are helpful but not enough to give the student the answer. I do not like the quiz feedback with this version, it made the feedback too short and missed parts that the student lost points on. I would also want it to tell me where to look to learn more about what I got wrong.

### What the next step should fix

Make the quiz feedback more specific and detailed, and point to where in the lesson I could read to learn more. 
The feedback from me for how I want the program personalized did not get applied to the quiz feedback, and the agent did not offer to make another quiz for me after I completed one. 
Make the lesson a little longer, going into more depth on important topics in that section.

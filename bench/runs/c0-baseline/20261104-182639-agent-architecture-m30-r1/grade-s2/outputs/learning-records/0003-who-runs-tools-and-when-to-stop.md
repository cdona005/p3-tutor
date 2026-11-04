# Open: who runs the tools, and why a loop needs a stop

On the spaced retake of quiz 0001 (s2), Riley chose the right option for "the model writes a request, the program runs the tool" (q2) and explained that tool results go back as the model's next input (q5). Two gaps remain. Riley's q4 answer still said the model "runs" each tool itself, though the count of 4 calls was right. Riley also chose "left to run longer, it will eventually fix the bug" on q3 (M6) after getting it right the first time.

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5, q6; compared with s1, which had M4 on q2 and q4.

**Implications:** Context and memory lessons should state plainly that the program runs tools and the model only writes requests. Include step limits and a cost cap per request, tied to the model budget. The belief that a loop needs no stopping condition (M6) is not fixed yet. Tool descriptions (name, purpose, parameters) are the next skill to practice, since q6 was answered with the name only.

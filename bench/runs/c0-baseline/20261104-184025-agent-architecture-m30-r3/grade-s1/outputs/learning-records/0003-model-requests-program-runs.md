# Misconception to work on: the model runs the tools itself (M4)

In quiz 0001 (s1), Riley said the model opens the booking system and "runs the 3 tools itself" in one call. The model only outputs a tool request. The program runs the tool and calls the model again, so each tool step is a separate model call. Riley also assumed the model remembers earlier sessions by itself (M3).

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6 wrong or partial. Correct on q1 and q3 (the loop and a step limit), and on the tool-descriptions half of q6.

**Implications:** Do not build cost or context lessons on "one model call per request" yet. Retest M4 and M3 when starting context and memory. Submission s2 was taken later from memory and may show whether this has changed.

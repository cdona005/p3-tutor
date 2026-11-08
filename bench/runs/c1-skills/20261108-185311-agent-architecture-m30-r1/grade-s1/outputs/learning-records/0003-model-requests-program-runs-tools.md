# Misconception to fix: the model runs the tools itself (M4), and remembers across sessions (M3)

On quiz 0001 (s1), Riley held the loop structure and stopping conditions but believed the model opens the booking system and runs the three tools inside one call (q2, q4), and that it remembers earlier sessions on its own (q6).
Correct picture: the model only outputs a tool request as text, the program runs the tool and starts a new model call with the result, and the model has no memory beyond its current input.

**Evidence:** quiz 0001, submission s1, items q2 (chose a), q4 (answered 1 call), q6 (claimed cross-session recall), q5 (omitted why the result goes back).

**Implications:** Fix before teaching context and memory: M3 will matter when memory is taught, since memory is something the program stores and re-inserts into the input. Submission s2 (taken later from memory) is not yet graded and shows whether this has been corrected.

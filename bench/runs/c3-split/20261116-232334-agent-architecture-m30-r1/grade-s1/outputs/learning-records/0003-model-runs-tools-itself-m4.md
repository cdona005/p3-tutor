# Misconception M4: Riley believes the model runs the tools itself

In quiz 0001 (s1), Riley answered that the model opens the booking system (q2) and "runs the 3 tools itself" in one call (q4), so the program-versus-model split is not yet understood. They also added that the model remembers earlier sessions' tool choices (q6, M3). Riley does have the loop (q1, q3) and knows tools are chosen from their descriptions.

**Evidence:** quiz 0001, submission s1, items q2, q4, q6; q5 gave the "what" but not the "why".

**Implications:** Before context and memory, fix the model/program split: the model writes a tool request, the program runs it and calls the model again, one call per step. Then teach that the model is stateless and memory is text the program supplies.

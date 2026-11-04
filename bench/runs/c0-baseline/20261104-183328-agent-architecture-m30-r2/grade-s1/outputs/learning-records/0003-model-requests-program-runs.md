# Open misconception: the model runs the tools itself (M4), and remembers on its own (M3)

On quiz 0001 (first attempt, s1) Riley chose that the model reads the calendar by itself (q2) and counted one model call for a three-tool run because "the model runs the 3 tools itself" (q4). In q6 Riley also said the model remembers earlier tool choices across sessions on its own.
Riley does get the loop (q1), the need for a stopping condition (q3), and that tools are chosen from their descriptions (q6).

**Evidence:** quiz 0001, submission s1, items q2, q4, q6; graded in `grades/0001-s1.json`.

**Implications:** Before building on context and memory, make the split concrete: the model writes a request, the program runs the tool and calls the model again, and nothing carries over between sessions unless the program supplies it. Compare with submission s2 (taken four days later) to see whether this has changed.

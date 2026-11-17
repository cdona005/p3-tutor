# Riley knows the loop and tool requests; still shows M4 and M6, and relies on tool names alone

On the second attempt at quiz 0001 (s2), Riley correctly identified the agent loop, that the model outputs a tool request, and that the result goes back as the next input. Still open: M4 (the model runs the tools itself, shown in q4's reasoning, as in s1), M6 (an agent left to run will eventually succeed, q3), and choosing tools by name only rather than by the full description (q6).

**Evidence:** quiz 0001, submission s2, items q3, q4, q6. In s1, q2 and q3 were answered differently (a and b), q4 reasoning also showed M4.

**Implications:** Before building on context and memory, teach the model/program split and stopping conditions, and tool descriptions. Riley improved on q2 and q5 between attempts, but q3 got worse (b in s1, c in s2), so treat the stopping-condition idea as unstable.

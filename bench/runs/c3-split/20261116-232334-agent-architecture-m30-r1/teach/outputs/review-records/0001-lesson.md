# Review record: lesson 0001, context and memory in an agent (O3)

## Reference check (before the review loop)
- 1 finding: "a hybrid of both is common" overstated the primary source. Changed to "the most effective agents might use a hybrid of both". Also removed the unsourced "few hundred tokens" chunk size.

## Pass 1: 15 findings
- Window size never stated, Figure 1 misleading: stated real sizes (200,000 to 1 million) in section 1, relabelled the figure's limit and caption as illustrative.
- Quadratic cost claim wrong for one big result: rewrote as sum of a growing prefix.
- "Billed in full" ignored caching: added a caching sentence, qualified the M6 box.
- 4M-token manual stated as fact: labelled illustrative, told Riley to measure the real set.
- Unsourced weights claim: reworded and tied to the memory tool docs.
- Top-3 chunks versus the source's 20: added a note that the count is tunable.
- Wrong misconception id on a check option: removed.
- Quiz 0001 dependency in section 2: removed.
- Faded task had no save-note call: added to call 4.
- Thin on retrieval misses, chunk context loss, save as you go: added to sections 3 and 4.
- Length (about 6,000 words): removed the five duplicated "Show the answer" blocks. Not cut further.
- "Right."/"Yes." praise in feedback: removed. Left alone: converting every paragraph to bullets.
- Section time labels summed to 42: reduced.

## Pass 2: 14 findings
- Weights parenthetical, Lost in the Middle wording, top-few-chunks claim, wrong M6 id, undefined caching, arithmetic slip (4,000 should be 3,400): all fixed.
- No mechanism for clearing: added a short pseudo-Python snippet.
- Notes outgrowing the cap, retrieval-notes link: added remedy.
- Figure 1 limit: relabelled "Limit: 200,000+ (not to scale)".
- LangGraph aside: shortened.
- Time labels: reduced.
- Left: length still about 1.3 to 1.4 times the request, though inside the bench's 0.6 to 1.5 range; I did not cut the remaining content because every section carries an objective idea. Bullet conversion of body paragraphs left for a later lesson. The "quiz is ready" line stands because quiz 0002 is written with this lesson.

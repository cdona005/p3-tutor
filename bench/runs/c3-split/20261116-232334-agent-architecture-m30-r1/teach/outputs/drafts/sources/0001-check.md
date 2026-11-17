# Check of drafts/lessons/0001-context-and-memory-in-an-agent.html

All six distinct URLs opened on 2026-11-16. The draft has 20 link occurrences (14 in the body, 6 in "Go further"), all to these six URLs, and all six are in drafts/sources/0001.md.

| URL | Sentence | Result |
|---|---|---|
| https://platform.claude.com/docs/en/build-with-claude/context-windows | s1: window is working memory separate from training data; system prompt, messages, tool definitions, tool results count; exceeding returns an error or stops generation | ok |
| same | s2: each turn re-sends prior history, so tokens accumulate | ok (page: input phase holds all previous history; "progressive token accumulation") |
| same | s2: docs say the same about accuracy and recall | ok ("accuracy and recall degrade", context rot) |
| https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | s1: context is a finite resource, so the question is which tokens are worth including | ok (finite resource, diminishing marginal returns) |
| same | s2: context rot, attention budget, diminishing returns | ok |
| same | s2: compaction named as a core technique for long tasks | ok (compaction of a conversation nearing the limit) |
| same | s3: structured note-taking, notes outside the context, read back later | ok |
| same | s4: lightweight identifiers, load at run time, "a hybrid of both is common" | does not say that, in part. The page says "the most effective agents might employ a hybrid strategy" (Claude Code as example). It does not say hybrid is common. Fix: "and says the most effective agents might use a hybrid of both". |
| https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | s3: model creates/reads/updates/deletes files in /memories via tool calls, application runs them, storage in your system; multisession pattern read at start, update at end | ok |
| same | s3: docs advise capping file size and expiring old memories | ok (Security considerations: "File storage size", "Memory expiration") |
| https://www.anthropic.com/news/contextual-retrieval | s4: embeddings for meaning, BM25 for exact terms such as error codes, merge, top chunks in prompt | ok |
| same | s4: under about 200,000 tokens (about 500 pages) can go in the prompt, caching cuts cost | ok (caching: latency >2x, cost up to 90%) |
| https://aclanthology.org/2024.tacl-1.9/ | s2: QA and key-value lookup, best at start or end, worse in the middle, even long-context models | ok (abstract; TACL vol. 12, 2024) |
| https://docs.langchain.com/oss/python/concepts/memory | s3 aside: kinds of memory (facts, experiences, instructions), short-term per thread vs long-term across threads | ok |
| Go further list (5 links plus the primary) | descriptions | ok. Each description matches the page. The primary is named "the primary source here" under "Read next". |

Link count: 6 distinct URLs, 20 occurrences, all opened. One row not ok.

## Sources file and closing
- Every cited source is in drafts/sources/0001.md. None is missing.
- The primary source is cited in "Go further" ("Read next ... the primary source here"). The footer.closing element itself does not cite it. If the closing must cite it, add the link there.
- The sources file already records the hybrid claim correctly ("hybrid with upfront loading is possible"). The lesson overstates it.

## Arithmetic (checked, all correct)
163,180 and 43,180 (fig. 2); 42,000 (quiz); worked example 11,820 / 13,020 / 150,000; your-turn 10,560 / 9,960. "Nearly five times" is 4.87.

## Load-bearing claims with no cited source
- "Using a model does not change its training; its weights stay as they were" (M2, and the s3 quiz). No source cited. The Context windows page does not say it. Either cite one or mark it as a general fact.
- Cost "grows roughly with the square of the number of steps when results are large". The lesson's own reasoning, no source. Fine as reasoning, but it is not sourced.
- "A token is roughly a word or part of one"; "Laser is probably one token". No source.
- "Chunks of a few hundred tokens each". I did not confirm this on the Contextual Retrieval page in this check. Unsourced here.
- "Meaning-based search may rank an error code poorly". Close to the post ("embeddings can miss crucial exact matches"), so it is acceptably backed.
- The 4M-token manual set, the token estimates and the per-call sizes are labelled as illustrations or estimates in the lesson. This is fine.
- "Tool-result clearing" as a technique is backed by the Context windows page (context editing: tool result clearing), but the lesson does not cite it there. Optional to add.

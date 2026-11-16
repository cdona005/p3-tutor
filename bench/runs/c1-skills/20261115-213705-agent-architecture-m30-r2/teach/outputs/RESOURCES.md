# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, compaction, tool result clearing, note-taking, sub-agents, just-in-time retrieval. Use for: any decision about what the agent keeps in context.
- [Docs: "Context windows" (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, accumulation across turns, behaviour at the limit, context-management strategies. Use for: exact rules and current limits (check before quoting sizes).
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25 hybrid search, reranking, and the roughly 200,000-token rule of thumb for skipping RAG. Use for: designing manual search.

## Wisdom (Communities)

No community verified yet. Learner has not opted out; propose one once found.

## Gaps

- A high-trust community for agent builders.
- Guidance on evaluating retrieval quality on a small document set.

# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering, Sep 2025)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context and context engineering, context rot, just-in-time retrieval, compaction, structured note-taking and sub-agents. Use for: what to keep in an agent's context, between steps and between sessions.
- [Docs: "Context windows" (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of the context window, what counts toward it (system prompt, messages, tool results, tool definitions), context rot, compaction and what happens when it is exceeded. Use for: exact facts about the window and token accounting.
- [Article: "Contextual Retrieval" (Anthropic Engineering, Sep 2024)](https://anthropic.com/engineering/contextual-retrieval)
  Why chunks lose context, hybrid embeddings plus BM25 search, reranking, failure-rate figures, and when a knowledge base under about 200,000 tokens can go straight into the prompt. Use for: finding the right page in a long manual.
- [Article: "Building effective agents" (Anthropic Engineering, Dec 2024)](https://anthropic.com/engineering/building-effective-agents)
  Describes the augmented LLM (retrieval, tools, memory) as the basic building block of agents. The page notes that some tooling it describes has changed since it was written. Use for: the big picture and the "simplest thing that works" advice.

## Wisdom (Communities)

- No community has been vetted yet. Local option: ask the university's makerspace staff and your own team for review of the memory design.

## Gaps

- A high-trust, moderated community for agent builders has not been found yet.
- No source yet on measuring the cost of context per request for a small budget; look for one when cost comes up.

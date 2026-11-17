# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering, Sep 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite budget, context rot, compaction, note-taking memory, just-in-time retrieval, sub-agents. Use for: what to keep in context, what to save, how an agent finds information.
- [Docs: Context windows (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates each turn, overflow behavior. Use for: the mechanism behind tokens, limits and cost.
- [Docs: Memory tool (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory the model reads and writes through tool calls, stored by the application. Use for: saving a student's training status between sessions; multisession progress-log pattern.
- [Docs: Memory overview (LangGraph)](https://docs.langchain.com/oss/python/concepts/memory)
  Short-term vs long-term memory, semantic/episodic/procedural types, hot-path vs background writes. Use for: vocabulary and design choices for memory.
- [Article: "Introducing Contextual Retrieval" (Anthropic, Sep 2024)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25 and reranking for long document sets; when to skip retrieval (under about 200k tokens). Use for: finding the right page in a long manual.
- [Paper: "Lost in the Middle" by Liu et al. (TACL 2024)](https://aclanthology.org/2024.tacl-1.9/)
  Peer-reviewed evidence that models use the middle of long inputs worse than the ends. Use for: why stuffing the whole manual in context is not free.

## Wisdom (Communities)

None yet.

## Gaps

- No vendor-neutral textbook source yet on retrieval-augmented generation for a design review.
- Wisdom communities not yet chosen; ask the learner whether they want any.

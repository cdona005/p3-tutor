# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, just-in-time vs up-front retrieval, compaction, note-taking, sub-agents. Use for: any decision about what the assistant keeps in context or saves.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates across turns, context rot. Use for: cost and window arithmetic.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file memory in /memories, its commands and safeguards. Use for: designing saved notes between sessions.

## Wisdom (Communities)

- Local: the team's own design review.
  Use for: defending the keep/save/retrieve decisions with a reason.

## Gaps

- A high-trust, beginner-level source on embeddings and chunking for manual search (the search for one returned only tutorials and blog posts).
- A moderated community for agent builders.

# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, context rot, attention budget, just-in-time vs up-front retrieval, compaction, structured note-taking, sub-agents. Use for: anything about what goes in an agent's context and how to keep it small.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side, file-based memory: six commands, the /memories path, path-safety rules. Use for: a concrete design for memory between sessions.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Current window sizes and how the window is counted. Use for: checking limits before budgeting. (Seen in search results; not read in full.)

## Wisdom (Communities)

- Local: the team's design review and the course's teaching staff.
  Use for: challenging the memory plan's failure cases. No online community is listed yet.

## Gaps

- A high-trust source on retrieval quality (chunking, embedding search evaluation) has not been found yet.

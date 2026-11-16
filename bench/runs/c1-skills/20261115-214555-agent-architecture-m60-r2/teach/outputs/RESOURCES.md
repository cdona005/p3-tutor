# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, just-in-time retrieval, compaction, structured note-taking, sub-agents. Use for: context and memory decisions, and later for multi-agent trade-offs.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, what happens when it is full. Use for: token and window questions.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/agents-and-tools/tool-use/memory-tool)
  File-based memory across conversations, client-side execution, commands, security notes. Use for: designing what the assistant saves between sessions.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al.)](https://huggingface.co/papers/2307.03172)
  Research on where in a long input models use information best (tested on 2023 models). Use for: evidence on long-context limits.

## Wisdom (Communities)

- Local: makerspace staff and earlier design teams
  Use for: real student questions to test the assistant's context plan against.

## Gaps

- A high-trust source on chunking and retrieval quality for manuals (embedding vs keyword search) has not been read yet.

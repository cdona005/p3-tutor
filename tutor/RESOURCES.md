# Agent Loops Resources

## Knowledge

- [Anthropic docs: Handling stop reasons](https://platform.claude.com/docs/en/api/handling-stop-reasons)
  Official list of every stop_reason value and the action for each. Use for: loop exit logic, max_tokens, empty end_turn, pause_turn.
- [Agent SDK docs: How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop)
  Official account of turns, max_turns, max_budget_usd and result subtypes; also tool execution, context compaction, permission modes and hooks. Use for: caps, error_max_turns, reading results, what the harness does around the model.
- [Claude Code docs: How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
  Official page that defines "agentic harness" as the layer around the model that provides tools and manages context; also compaction, checkpoints, permission modes. Use for: the definition of a harness.
- [Anthropic Engineering: Effective harnesses for long-running agents](https://anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  Anthropic post (Nov 2025) on why agents with limited context windows and no memory between sessions need a harness. Use for: why an agent needs a harness, compaction limits.
- [Anthropic Engineering: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  Anthropic post (Dec 2024): agents as LLMs using tools in a loop, stopping conditions, guardrails and sandboxing. Use for: why limits exist, loop framing.
- [Claude API docs: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
  Official API page: the model emits tool_use, your code runs the tool and returns tool_result. Use for: what the model does not do (execute tools).
- [Claude API docs: Working with the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
  Official page stating the Messages API is stateless: you always send the full conversation history. Use for: why a harness must keep the history.
- [AI SDK docs: Loop control](https://ai-sdk.dev/docs/agents/loop-control)
  Another SDK's step caps and combined stop conditions. Use for: comparing stop conditions across frameworks.
- [Arize: What is an agent harness?](https://arize.com/blog/what-is-an-agent-harness/)
  Vendor blog (Arize AI, Apr 2026), secondary: component list of a harness. Use for: cross-check only, not as the authority.

## Wisdom (Communities)

- None listed yet.

## Gaps

- A high-trust community for agent builders: none found in this session's searches.
- No primary source found that gives one official, complete list of harness components; the definition (Claude Code docs) is short and the component list is assembled from several pages.

# Check of drafts/lessons/0002-what-an-agent-harness-does.html

All URLs opened 2026-11-17. 5 external links (7 link occurrences), plus 2 internal links.

## External links

| URL | Sentence | Verdict | Fix |
|---|---|---|---|
| https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview | "For tools you define, it answers stop_reason: "tool_use", and your code runs the operation and sends back a tool_result" | ok | Page says client tools respond with `stop_reason: "tool_use"`, "Your code runs the operation and sends back a `tool_result`"; server tools run on Anthropic's infrastructure. |
| https://code.claude.com/docs/en/how-claude-code-works | Claude Code "is the layer around the model that provides the tools and manages the context the model sees. This surrounding layer is what the term agentic harness refers to" | ok | Quote is verbatim. |
| https://code.claude.com/docs/en/agent-sdk/agent-loop | A turn is one pass ... "with no control returned to your code in between" | ok | |
| same page | Read-only tools run concurrently; Edit, Write, Bash sequentially ("same page") | ok | |
| same page | Context accumulates; reading a big file costs thousands of tokens | ok | |
| same page | Compaction, `compact_boundary`, early instructions may not survive ("same page") | ok | |
| same page | `max_turns` and `max_budget_usd` both default to no limit | ok | |
| same page | Permissions settings list (`allowed_tools`, `disallowed_tools`, `permission_mode`, hooks, denial returns rejection message) | ok | `acceptEdits` also auto-approves common filesystem commands (mkdir, mv ...), not only file edits; the lesson's wording is a simplification, not wrong. |
| https://www.anthropic.com/engineering/building-effective-agents | "Anthropic's advice on agents is the same: include stopping conditions such as a maximum number of iterations to keep control" | ok, slightly stronger than source | Source: "it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control." Softer fix: "Anthropic notes it is common to include stopping conditions ...". |
| https://anthropic.com/engineering/effective-harnesses-for-long-running-agents | "what a harness needs when a task outlasts one context window" | ok | Page: a harness must bridge sessions that begin with no memory (progress file, git history). |
| https://code.claude.com/docs/en/agent-sdk/agent-loop (Go further) | "the primary source ... all four duties with their defaults on one page" | ok | |

## Internal links

| Link | Verdict | Note |
|---|---|---|
| `0001-how-an-agent-decides-it-is-done.html` | ok once promoted | File exists at `lessons/0001-...html`, not in `drafts/lessons/`. Resolves correctly when 0002 is moved to `lessons/`. |
| `../cheatsheets/agent-loop-stopping.html` | ok once promoted | Exists at `cheatsheets/`; resolves from `lessons/`, not from `drafts/lessons/`. The cheatsheet does back "tool-call turns + 1" and `error_max_turns`, no `result`. |

## Sources file and closing

- All five external URLs the lesson cites are in `drafts/sources/0002.md`, with the same URL strings. The Arize source is in the file but not cited (fine).
- Primary source is cited in the "Go further" section ("Read or watch next"). The footer itself mentions only the quiz; if the closing must name the primary, "Go further" is where it does.

## Load-bearing claims: sourced status

| Claim | Status |
|---|---|
| Model returns only a request; harness runs the tool | Backed (Tool use overview) |
| Definition of harness | Backed (How Claude Code works) |
| Compaction loses early instructions; rules go in CLAUDE.md, re-injected every request | Backed (agent-loop page, also How Claude Code works) |
| "so compaction does not summarize it away" | Inference from "re-injected on every request"; reasonable, not stated in those words |
| `max_turns` counts tool-call turns plus one; `error_max_turns` with no result | Backed (agent-loop page, cheatsheet) |
| Budget overshoot by one response plus subagents | Backed (agent-loop page, "Budget headroom") |
| `result` only on success; subtype is the primary termination check | Backed (agent-loop page, "Handle the result") |
| Denied tool returns rejection message, run goes on | Backed (agent-loop page) |
| Hooks run in app process, use no context | Backed (agent-loop page) |
| "your next call arrives with no memory of the first" / "model does not remember" (section 1, summary) | No source. The Messages API being stateless is not stated on any cited page; the tool-use page only shows history being resent in the example. Add a source (for example the Messages API docs) or soften. |
| "The harness has four duties" | The lesson's own framing of the objective; no cited source names exactly four duties (Arize lists components, uncited). Acceptable if presented as the lesson's organization. |
| "The model has no notion of how many turns or dollars it has used" (section 4) | No source; inference. |
| Bench: "a tool that would need a prompt is denied ... Only permissions.allow plus Glob and Grep are open" | Backed by the repo `CLAUDE.md` (bench rules), not by a cited page. Slightly overstated: the agent-loop page says reads inside working directories need no approval, so Read can work without being in `permissions.allow`. Consider "Only permissions.allow plus Glob and Grep are pre-approved" or "tools that would need a prompt". |
| Worked example: "25 turns" equals 25 tool calls (21 Read + 4 Grep), and "the config or the bench set 25" | Hypothetical trace. Turns and calls are equal only if one call per turn; the model can issue parallel calls in one turn, so 25 calls does not imply 25 turns. State the assumption or say "25 turns, one call each". |
| Worked example step 1: subtype "is the primary termination signal" | Backed (agent-loop page: subtype "is the primary way to check termination state") |
| Recall 1: truncated reply (`max_tokens`) has no tool call | Backed in part: agent-loop page lists `max_tokens` as a `stop_reason`; carried from lesson 1. |

## Other observation (not a failure)

The agent-loop page says a single-shot Python `query()` raises after yielding an error result. The lesson's "no result field" snippet is correct for the stream, but a learner running it will also see an exception; the lesson does not mention this.

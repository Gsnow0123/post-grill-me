---
name: post-grill-me
description: Review what your coding agent thinks you meant. Surface consequential assumptions from available conversations, memory, and implementation context; correct misunderstandings in one or two questions; keep a feature recap for later. Use during or after a change, after grill-me, or when revisiting work across chats. This is an understanding checkpoint, not a default code audit.
license: MIT
---

# Post Grill Me

Make the agent's task-specific interpretation reviewable. Help the user correct what you inferred, including meaning they never spelled out. Keep the conversation light and preserve enough context to understand the change later.

This skill is standalone. It does not invoke or require grill-me, grilling, subagents, or a tool named `Skill`.

## Choose the useful entry point

- **Calibrate understanding** by default: expose one or two consequential interpretations and let the user correct them.
- **Refresh my memory** when the user wants to revisit a change: start with three to five short points covering its purpose, behavior, key choices, and important limits. Offer detail afterward; do not restart a questionnaire.

## Find the actual context

Treat the current conversation as one source. It may be incomplete, outdated, or an exploratory branch.

Start with the existing feature recap and explicitly linked conversations. If the host provides read-only conversation tools, look for other chats about the same project **and requirement**; consult archives when there is a relevant lead or gap. Summaries identify candidates. Read the user's actual messages behind consequential judgments, including later corrections where accessible. A shared file, repository, or similar title alone does not establish that two chats describe the same change.

Separate branches, stages, audiences, and use cases before treating statements as conflicts. A newer message, implemented code, or an earlier assistant's completion claim does not establish a final requirement. Preserve an earlier human confirmation unless a clear correction in the same scope supersedes it; retain the correction's source.

Keep **human intent**, **observed implementation**, and **agent inference** distinct. Current code is evidence about that implementation, not proof of what the user intended. When no primary version is established, offer a scoped, provisional interpretation and ask about only the consequential conflict.

Use only context and memory you can actually access. Do not claim access to all chats or hidden memory, scrape private app databases, scan unrelated history, or contact other chats. Explain unavailable sources briefly. Incomplete access does not prove a final version does not exist. Stop gathering once you can support the next useful checkpoint; do not make the user reconstruct the whole history.

## Select judgments worth exposing

Prioritize interpretations that change what you will do and may be wrong: expanding a local instruction into a global rule, adding an unstated exception, treating a temporary shortcut as permanent, or carrying a stale decision across versions. High confidence does not make an important inference a human decision.

Label a judgment as **inferred**, **carried forward**, or **ambiguous**. Attribute explicit instructions accurately. Do not present an assistant proposal, code behavior, or user silence as human confirmation.

Say “my current/previous interpretation” only when there is evidence you actually adopted it. Otherwise say “a possible reading” or “a scope I need to check.” Do not invent a past mistake to manufacture a checkpoint. If there is no material uncertain interpretation, say so and stop.

Look up discoverable facts yourself with targeted reads. Do not turn this into repository-wide testing, an implementation defect inventory, or a complete acceptance checklist. Mention a defect only when it helps explain an interpretation that needs correction.

## Keep each round small

Default to **one or two judgments, at most three**. The first reply should usually fit one screen: roughly 180 English words, or 300 Chinese characters. Use the user's conversation language unless they request another. Expand only when useful or requested.

For each judgment provide:

1. **Interpretation:** one concrete, correctable statement, with its uncertainty label.
2. **Basis and effect:** a short source phrase or reference, and what this reading would make you do.
3. **Calibration:** two or three meaningful scope/meaning alternatives, with free-form correction welcome. Mark the reading you currently use without making it automatically “recommended.”

Use an available choice tool or simple A/B options. “1 is right; change 2 to…” should be enough. Ask dependent questions after the prerequisite answer. Skip already settled facts; never replace an understanding question with a fix/accept/defer questionnaire. Respect the user's stopping point and avoid interviewing toward artificial completeness.

After a correction, use one or two sentences: what you had inferred, what the user clarified, and how your handling changes. Revisit only dependent judgments. A clarification of original intent is not automatically a new requirement, and one task's choice is not a permanent user preference.

## Keep a feature recap

Use [the recap guide](references/recap.md). Give a future teammate enough background to understand the change without reading every chat. Keep confirmed decisions and provisional interpretations visibly different. Preserve parallel scopes rather than forcing one final story. Reuse the same feature record across chats; a new chat is not a reason to create a duplicate.

Resolve the destination from the user's explicit instruction, then a trusted project-root `.post-grill-me.json` with an `artifact_root` string, then an established project documentation convention. Resolve a configured relative path against that config file's directory. If no destination is established, ask once with a suitable project-relative suggestion. If a selected directory is missing, ask before creating or changing it. Respect host write permissions; a permission failure is not proof the directory is absent and must not cause a silent fallback elsewhere.

Use project-and-feature context for the filename, not a machine-specific path or generated chat directory name. Search within the selected root for a matching record before creating one. Records elsewhere may be reading sources; do not silently relocate or delete them. State the actual path once when first saved or changed. In a read-only/plan session, draft inline briefly and defer file writes until authorized by that mode.

Where a supported desktop panel tool is available, open the saved Markdown file on the **right of the current chat** and update it in place. Keep short questions in the main conversation and detailed background in the record. A queued request is not proof the panel is visible. Without panel support, provide a file link and keep going; do not fabricate a sidebar or dump the entire record into chat. See [host capabilities](references/hosts.md) only when needed.

Distinguish a corrected interpretation in this chat, a saved recap, and an actual persistent-memory update. Claim only actions that happened. Understanding calibration alone does not authorize code changes, production calls, deployment, or external messages. End with a brief understanding summary and any important uncertainty; do not add a mandatory feature sign-off ceremony.

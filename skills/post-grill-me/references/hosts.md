# Host capabilities

The core workflow is instruction-only. It needs no network service, API key, MCP server, subagent, or companion skill. Capabilities below are optional and depend on what the current host exposes and authorizes.

| Capability | When available | Otherwise |
| --- | --- | --- |
| Related conversations | Use read-only listing and reading tools, including archived sources when relevant. | Work from supplied material and state the coverage gap. |
| Code context | Read the relevant files or diff to understand the implementation reference. | Keep implementation claims unverified. |
| Durable recap | Write to the agreed directory, subject to the current mode and permissions. | Keep a short provisional summary in chat and explain the unsaved state. |
| Right-side file panel | Open the saved recap in the current conversation's panel. | Link the file; short calibration still works. |

In Codex desktop **when those tools are actually present**, conversation tools may include `list_threads`, `read_thread`, and `list_archived_threads`. The file panel operation may be `mcp__codex_app__open_in_codex` with `placement: "right"` and `target: { type: "file", path: an_absolute_path }`; omit `threadId` to target the current chat. Follow the exposed schema and report queued/failure status accurately.

Do not assume Codex CLI, an IDE extension, or another Agent Skills client has these desktop tools. Do not create/fork chats or emulate tools to obtain the same visual effect. Related-chat access does not grant authority to message those chats or read unrelated account history.

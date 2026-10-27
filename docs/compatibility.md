# Capabilities and limits / 能力与边界

The skill follows the [Agent Skills format](https://agentskills.io/specification). Its core is a plain-text understanding-calibration workflow. Installation support in a client does not prove every optional capability exists there.

| Feature | Requirement | Without it |
| --- | --- | --- |
| Small calibration rounds | A client that can load the skill's instructions | The Markdown can be read as a reusable prompt. |
| Related-chat context | Actual authorized conversation-listing and reading tools | Supplied context remains usable; unknown coverage stays explicit. |
| Saved feature recap | Authorized filesystem access in the current mode | The reply can summarize provisionally, without claiming a saved file. |
| Right-side recap | A host-provided file panel operation | A normal file link is sufficient. |
| Persistent-memory update | A real supported memory-write operation and appropriate authorization | Only the current understanding and/or record changes. |

The desktop adapter in each skill names **possible** Codex tools and explicitly checks availability. It does not supply those tools, unlock other conversations, or make a separate isolated chat. Do not infer that Codex CLI, IDE integrations, or other agents expose the same operations.

No runtime dependency, API key, hosted service, telemetry, or install hook is included in the skill. The optional third-party installer has its own behavior and settings; see [Vercel's documentation](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry).

## 中文说明

核心是可移植的指令。客户端能安装 skill，不代表它一定支持跨对话读取、文件写入或桌面面板。

- 没有对话工具，就使用已提供的材料并说明缺口，不猜测隐藏记忆或私有历史。
- 只读/计划模式不写记录，也不以“已记住”冒充持久记忆更新。
- 没有右侧面板时，文件链接仍能使用；不会为了界面效果另建聊天。
- 核心 skill 不含遥测、后台服务或安装钩子；第三方安装器的行为以其文档为准。

Package validation and a manual behavior-case collection are included. There is no claim of a measured model success rate or end-to-end certification across clients. See [the evaluation guide](../evals/README.md).

# Contributing / 贡献指南

Keep the core interaction small: consequential interpretation, short basis, easy correction. Improvements should help users review what the agent inferred without turning the skill into a generic code audit.

1. Explain the actual misunderstanding or retrieval problem with a **fictional or sanitized** example. Do not paste private conversations, internal URLs, absolute machine paths, or credentials.
2. Update both `skills/post-grill-me` and `skills/post-grill-me-zh` for behavior changes. Wording can differ naturally; the decision rules should agree.
3. Adjust a relevant manual case in [evals/cases.json](evals/cases.json) when behavior changes.
4. Run `python scripts/validate.py` and, for release changes, `python scripts/package.py --version 0.1.0` followed by `python scripts/validate.py --archives dist`.
5. Report which checks were structural and which were actual agent trials. A green package workflow is not proof of model behavior.

Please use issues for concrete problems or proposals. Installing either language should remain self-contained, with optional host integrations clearly labeled.

## 中文

改进围绕“重要推断、简短依据、便于纠正”，避免扩成通用代码审计。提交前：

- 使用虚构或脱敏案例，不贴私有对话、内网地址、机器路径和凭据。
- 同步中英两版的判断规则；表达不必逐字翻译。
- 行为变化对应调整手动回归案例，运行结构检查和必要的打包检查。
- 区分结构校验与真实 agent 试跑，不把 CI 通过当作行为验证。

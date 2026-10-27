# Manual behavior cases / 手动行为案例

[cases.json](cases.json) contains fictional regression cases for **both** instruction languages. They are intended for human-reviewed trials, not a keyword-matching benchmark.

## Run a case

1. Start a fresh session in the client you want to test. Load exactly one language variant.
2. Supply the selected case's `context` and `request` as the scenario. Do not give the agent the `expected` or `must_not` fields before it responds.
3. Use a disposable workspace. Supply mock/read-only tools if the case needs capabilities; never connect a trial to real production actions.
4. Review the actual reply and any file changes against the expected decisions, scope, short-round experience, and forbidden actions. A missing host capability should be handled as a limit rather than faked.
5. Record client/model, skill revision, case ID, supplied tools, output, and observed outcome. Test the other language under equivalent conditions when changing behavior.

The package workflow checks that these cases have a usable shape. It **does not run an agent, grade model behavior, or establish a pass rate**. No such score is claimed for this release.

## 中文

这些案例都是虚构语料，覆盖范围扩大、旧确认与新探索、明确替代、并行版本、无关共享文件、历史不可读、跨聊天复用、复习模式、权限/面板与不捏造假设。

手动测试时，新会话只加载一个语言版本，把 `context` 与 `request` 交给 agent；预期和禁做事项留给评审者。使用可丢弃目录与模拟/只读工具，观察真实问答和文件变化。记录宿主、模型、skill 版本、案例及工具条件；修改行为时对两种语言做等价检查。

CI 只检查案例结构，不执行 agent，不以关键词匹配替代判断，也不提供模型通过率。

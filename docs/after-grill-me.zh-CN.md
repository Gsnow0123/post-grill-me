# grill-me 之后：看看实现过程中留下了哪些解释

[English](after-grill-me.md) · [首页](../README.zh-CN.md)

[Matt Pocock 的 grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)通过访谈让想法清晰；[grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)提供与仓库工作相关的入口。它们本身仍然有用。

实现时还会出现新的解释：局部要求被扩成共享规则、例子被当成默认值、一个对话里的临时捷径影响了另一分支。Post Grill Me 用短轮次把这些解释拿出来核对。

## 可直接复制的后续提示词

```text
使用 post-grill-me 检查这次修改。挑出你实际采用过、如果理解错就最影响
行为的一两个解释，简述依据和后果，让我纠正范围，并保存以后能复习的功能记录。
```

Codex 中可在前面加 `$post-grill-me-zh`，英文指令版加 `$post-grill-me`；其他客户端使用对应的 skill 调用方式。修改进行中感觉方向偏了，也可以直接调用。

## 一个值得发现的范围偏差

假设前面的访谈只约定：导出预览对归档项按普通项处理。实现时，AI 把这个解释也用到了定时任务。测试可能准确验证了扩大的行为，但适用范围仍值得人工纠正。

轻量校准应展示：“我把预览的规则扩到了定时任务，这两处都应适用吗？”不应先展开完整代码审计、捏造曾经采用的解释，或要求用户重答整个访谈。

相关对话不一致时，先区分分支、阶段和使用场景。保留已有的确认范围，只有同范围的明确纠正才能替代；不能仅凭后来的头脑风暴认定最终版本。

## 轻量配合

- 本 skill 可以单独安装，不依赖 grill-me 或 grilling。
- 先校准含义和范围，再决定是否需要改代码。
- 保留功能背景和理解纠正，方便未来同事恢复脉络。
- [示例记录](../examples/feature-recap.md)展示了回顾资料应有的阅读体验。

本项目是独立配套工作流，不是 Matt Pocock 项目的官方扩展。

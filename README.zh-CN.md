# post-grill-me

**检查 AI 把你的意思理解成了什么。**

为 [grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) 用户设计的轻量配套流程：暴露 AI 在工作中采用的假设，用**每轮一两个问题**纠正误解，再留下一份几个月后仍能复习的功能记录。

[English](README.md) · [简体中文](README.zh-CN.md) · [快速示例](#30-秒看懂) · [配合 grill-me](docs/after-grill-me.zh-CN.md)

[![包检查](https://github.com/Gsnow0123/post-grill-me/actions/workflows/validate.yml/badge.svg)](https://github.com/Gsnow0123/post-grill-me/actions/workflows/validate.yml)
[![MIT 许可](https://img.shields.io/badge/license-MIT-2563eb.svg)](LICENSE)

![把 AI 扩大的理解纠正为有范围的决定，并保存到可复用记录。](assets/overview.png)

## 安装

选择一种指令语言即可。两种版本均独立完整，回复默认跟随你的对话语言。

```bash
# 中文指令
npx skills add Gsnow0123/post-grill-me --skill post-grill-me-zh

# English instructions
npx skills add Gsnow0123/post-grill-me --skill post-grill-me
```

[Skills CLI](https://github.com/vercel-labs/skills) 会让你选择安装到哪个 agent。加 `-g` 可安装为用户级 skill。手动安装 Codex 与发布压缩包说明见[安装指南](docs/install.md)。

在 Codex 中调用：

```text
$post-grill-me-zh 检查你对这次修改采用了哪些重要推断，让我纠正。
```

英文指令版使用 `$post-grill-me`；采用斜杠调用的客户端使用对应的 `/post-grill-me-zh`。核心流程不需要其他 skill、API 密钥、服务或运行时依赖。

## 30 秒看懂

*以下是虚构导出功能的表达示例。*

> **AI · 推断的范围**
> 我把“不要特殊处理归档项”理解成所有导出路径都适用。但你当时在讨论预览弹窗，这个解释还会改变定时导出任务。
>
> **A．**只改预览。**B．**预览和定时导出都改。也可以直接改写范围。
>
> **你**
> A，定时任务保留原有行为。
>
> **AI**
> 我把局部要求扩大成了更广的规则。现在限定在预览，保留定时任务原有行为，并在回顾记录里记下这个边界。

每次只看一个有影响的解释、简短依据和后果，轻松纠正。完整功能脉络放在记录里，不把聊天变成长篇审查问卷。

## 已经在用 grill-me？

```text
grill-me / grill-with-docs → 实现 → post-grill-me → 校准理解
                                        ↘ 功能记录 → 日后复习
```

| 时点 | 值得回答的问题 |
| --- | --- |
| 用 grill-me 澄清想法 | 想达到什么结果，还有哪些决定没想清楚？ |
| 用 post-grill-me 检查修改 | AI 实际采用了哪些解释，它们符合我的原意吗？ |
| 几个月后再回来 | 当时为什么改、怎样工作、澄清过哪些误解？ |

修改进行中也可以调用，不必等开发结束；没有使用过 grill-me 也能独立运行。[配套工作流](docs/after-grill-me.zh-CN.md)提供可复制提示词和范围纠正示例。

## 它提供什么

- **短轮次。**默认一两项重要判断，附简短依据和具体选项，不进行穷尽式采访或自动验收。
- **可纠正的推断。**区分用户原意、代码行为和 AI 推断；高置信度也不等于已经得到人工确认。
- **多对话、多版本。**工具允许时关联相关聊天；消息更新、代码写完都不等于需求最终版，不同分支保留各自范围。
- **可复习的功能记忆。**目的、行为、选择、理解纠正和来源边界保留在同一份记录里，跨聊天复用。
- **可选侧边展示。**宿主提供右侧文件面板时自动打开记录，聊天保留短问答；CLI 中给文件链接也能使用。

## 忘了当时怎么改？

```text
$post-grill-me-zh 帮我复习导出功能。先简述目的、记录中的行为和关键选择，
我再决定深入哪部分。
```

先用三至五个短要点恢复背景，不要求你记住所有旧决定。历史记录会保留来源与适用范围，不能充当当前部署或实现的证明。

## 记录保存在哪里

可在提示词指定地址、沿用项目既有文档约定，或将 [.post-grill-me.example.json](.post-grill-me.example.json) 复制到项目根目录并命名为 `.post-grill-me.json`：

```json
{
  "artifact_root": "docs/feature-recaps"
}
```

相对路径基于配置文件目录。目录不存在时，AI 会先询问再创建；没有约定地址时，简短确认一次。同一功能更新同一记录，不随聊天重复建档。公开版没有任何个人机器的固定路径。

## 兼容性与验证

这是只有指令的 [Agent Skill](https://agentskills.io/specification)。跨对话读取、文件保存和侧边面板取决于宿主能力与权限。它不能读取不可访问的记忆，也不能仅凭一句“已记住”就更新持久记忆。详见[能力边界](docs/compatibility.md)。

包检查覆盖双语目录、元数据、本地链接、发布包内容和公开内容检查。[行为案例](evals/README.md)供手动回归测试，没有宣称模型通过率或所有客户端均已认证。展示案例是说明，不是基准测试结果。

## 参与改进

欢迎提供脱敏后的原话、AI 推断、你的纠正，以及所用宿主。修改工作流时请同步中英两版，详见[贡献指南](CONTRIBUTING.md)。

## 灵感来源

名称和访谈思路受 Matt Pocock 的 [grill-me / grilling](https://github.com/mattpocock/skills) 启发。本项目独立编写，采用自己的范围，不依赖该仓库。打包方式参考 [Superpowers](https://github.com/obra/superpowers)、[Agent Skills 标准](https://agentskills.io/specification)与 [Vercel Skills CLI](https://github.com/vercel-labs/skills)，不表示获得原作者背书或存在官方关联。

如果它帮你发现了原本会漏掉的理解偏差，欢迎点 star，或提供一个脱敏案例，让更多人发现它。

MIT · [更新记录](CHANGELOG.md)

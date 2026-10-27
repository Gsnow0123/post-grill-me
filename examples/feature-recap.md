# Export preview: feature recap / 导出预览：功能回顾

**Fictional example. All dialogue, identifiers, and decisions below are invented to illustrate the format. They are not user project data or test results.**

## Quick recall

- **Purpose:** let operators preview which rows a manual export will include.
- **Scope:** the preview and its manual-export path; the scheduled job retains its existing archived-item handling.
- **Recorded behavior:** archived items follow ordinary preview filtering. Selection still obeys the existing access rules.
- **Understanding correction:** the agent initially interpreted “don't special-case archived items” as covering every export path. The fictional user clarified that it applied to the preview only.
- **Still provisional:** whether the preview should show a separate count for excluded rows. No decision is implied by the implementation alone.

## Why this record exists

The feature was discussed in two fictional chats. One explored applying the same behavior to scheduled exports; the other confirmed a narrower preview scope. The exploratory chat is not treated as the final decision just because its timestamp is later.

| Source | Scope | How it is used |
| --- | --- | --- |
| Fictional conversation A | Manual preview | Human-confirmed scope and clarification |
| Fictional conversation B | Possible scheduled-job follow-up | An exploratory alternative, kept separate |
| Fictional implementation reference | Preview branch | Evidence of behavior, not proof of human intent |

This record says nothing about present deployment or real-world execution. A later same-scope human correction could supersede the preview decision while retaining this history.

## 中文回顾

- **为什么改：**让操作者在手动导出前预览将包含哪些行。
- **范围：**预览及其手动导出路径；定时任务保留原有归档项处理。
- **记录中的行为：**归档项按普通预览筛选处理，权限规则继续有效。
- **理解纠正：**AI 曾把“不要特殊处理归档项”扩到所有导出路径，虚构用户澄清只针对预览。
- **尚未确定：**是否单独显示被排除行数；实现本身不代表已经有人作出决定。

两个虚构对话分别涉及已确认的预览范围和探索中的定时任务方案。后者更晚，也不自动成为最终版本。本记录不证明当前部署、运行或真实送达，未来明确纠正可以替代已有决定并保留历史。

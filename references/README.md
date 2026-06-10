# VibeGuard References

这里放的是 VibeGuard 的按需参考资料。

`skill.md` 负责主流程和路由；本目录负责更细的模板、检查清单、失败模式和示例。不要每次都读取全部文件，按当前任务选择需要的文件。

## 文件说明

- `templates.md`：Tiny / Standard / Spec / Bugfix / Refactor / Handoff 等可复制模板。
- `clarification.md`：澄清问题策略，帮助判断什么时候该问、问什么、问几个。
- `gates.md`：开工闸门，判断 GO / GO WITH ASSUMPTIONS / NO-GO。
- `failure-modes.md`：AI Coding 常见失败模式，以及如何转成 brief 里的约束。
- `spec-framework.md`：Spec 框架生成规则，定义 Mini / Standard / Full Spec、质量门禁、上下文分层、验收和任务映射。
- `coding-guardrails.md`：代码结构护栏，处理耦合、前后端/API 边界、状态归属、全局变量、命名和调用关系等可维护性风险。
- `release-notes.md`：版本更新公告、迭代日志、开发回顾报告、AI 交接摘要和下一版计划模板。
- `usage-examples.md`：常见输入输出示例。
- `wording.zh-CN.md`：自然中文表达建议，避免 AI 味和过度营销。

## 读取建议

- 小改动：优先只用 `skill.md`，最多读取 `templates.md` 的 Tiny Brief。
- 模糊 idea：读取 `clarification.md` + `templates.md`。
- 普通功能：读取 `templates.md`，必要时读取 `gates.md`。
- Bug 修复：读取 `templates.md` 的 Bugfix 部分 + `failure-modes.md`。
- 重构：读取 `templates.md` 的 Refactor 部分 + `gates.md`；如果涉及耦合、状态归属或模块边界，再读取 `coding-guardrails.md`。
- 前后端联调/状态管理/公共函数/全局变量/命名混乱：读取 `coding-guardrails.md`，把风险转成具体代码结构约束。
- 高风险/跨模块任务：读取 `gates.md` + `failure-modes.md` + `spec-framework.md` + `coding-guardrails.md` + `templates.md` 的 Spec Brief。
- 用户要求生成 spec 框架：读取 `spec-framework.md`，先判断 Mini / Standard / Full，再输出对应结构。
- 用户要求版本更新公告/迭代日志/开发回顾：读取 `release-notes.md`，先判断目标读者，再输出对应版本记录。
- 表达太生硬：读取 `wording.zh-CN.md`。

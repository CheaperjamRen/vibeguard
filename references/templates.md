# VibeGuard 模板库

这些模板用于生成可直接复制给 AI Coding 工具的 brief。使用时不要原样照抄空模板，要根据用户当前信息填充。缺失信息写“未知”或“需要确认”。

## 目录

- Tiny Brief：1-2 个文件的小改动
- Standard Brief：普通功能开发
- Spec Brief：跨模块/高风险任务
- Bugfix Brief：修 bug
- Refactor Brief：重构
- Code Structure Guardrails：代码结构约束
- Prompt Review：检查提示词
- Handoff Brief：长对话交接
- Current-Task Brief：最终复制给 AI Coding 工具

## Tiny Brief

适合：文案、小样式、单点 UI、小范围逻辑调整。目标是轻量，不要把小任务搞成大流程。

```markdown
# Tiny VibeGuard Brief

## 目标

[一句话说明要改什么]

## 只改这些

- ...

## 不要改

- ...

## 做完算完成

- ...

## 如果不确定，停下来问

- ...
```

## Standard Brief

适合：普通功能开发、明确的小产品功能、一般性改动。

```markdown
# VibeGuard Brief

## 1. 一句话目标

[这次到底要完成什么]

## 2. 背景与当前问题

[为什么要做；现在的问题是什么]

## 3. 用户/使用场景

[谁在什么场景下使用；如果未知，写未知]

## 4. 第一版范围

这次要做：
- ...

这次不做：
- ...

## 5. 允许改动

AI 可以改：
- ...

AI 不能改：
- ...

## 6. 已知上下文

- ...

## 7. 关键假设与未知项

假设：
- ...

未知：
- ...

## 8. 风险点

- ...

## 9. 代码结构约束

如果涉及前后端、状态管理、公共函数、公共组件或长期维护，补充：

模块边界：
- ...

前后端/API 边界：
- ...

状态归属：
- ...

全局变量限制：
- ...

命名与调用关系：
- ...

可维护性检查：
- ...

## 10. 验收标准

完成条件：
- ...

验证方式：
- ...

## 11. 停止条件

遇到以下情况必须停下来问，不要继续猜：
- ...
```

## Spec Brief

适合：跨模块、多页面、多角色、多数据流、迁移、支付、权限、数据结构、较长期任务。

生成前先读取 `spec-framework.md` 判断应该用 Mini / Standard / Full 哪一档，不要默认生成最长版本。

```markdown
# VibeGuard Spec Brief

## 0. Spec 档位判断

建议档位：[Mini / Standard / Full]

原因：
- ...

## 1. Intent：真正要解决的问题

[用户真正想解决的业务/产品/工程问题]

## 2. Success Definition：成功定义

[什么结果出现时，说明这件事真的解决了]

## 3. Users / Scenarios：用户与场景

- ...

## 4. Requirements：必须满足的行为

| ID | Requirement | Priority | Source | Acceptance |
|---|---|---|---|---|
| R1 |  | Must | User-stated / Code-observed / Assumed | A1 |

## 5. Non-goals：这次明确不做

- ...

## 6. Constraints：边界与约束

产品约束：
- ...

技术约束：
- ...

兼容性约束：
- ...

数据/权限约束：
- ...

不可改动区域：
- ...

代码结构约束：
- 模块边界：...
- 前后端/API 边界：...
- 状态归属：...
- 全局变量限制：...
- 命名与调用关系：...
- 可维护性检查：...

## 7. Context Budget：上下文分层

Must read：
- ...

Read if needed：
- ...

Do not read yet：
- ...

Facts：
- ...

Assumptions：
- ...

Unknowns：
- ...

Deprecated context：
- ...

## 8. Acceptance Contract：验收合约

| ID | Given | When | Then | Edge case | Verify by |
|---|---|---|---|---|
| A1 |  |  |  |  |  |

## 9. Task Plan：任务拆解

| Task | Change area | Related requirement | Related acceptance | Verification |
|---|---|---|---|---|
| T1 |  | R1 | A1 |  |

## 10. Risk / Stop Contract：风险与停止条件

风险：
- ...

遇到以下情况停止并询问用户：
- ...

## 11. Current-Task Brief：交给 AI Coding 工具的执行说明

[生成短版 Current-Task Brief]

## 12. Spec 自查

- 清晰性：通过 / 需要补充 [...]
- 可验证性：通过 / 需要补充 [...]
- 可执行性：通过 / 需要补充 [...]
- 一致性：通过 / 需要补充 [...]
- 最小性：通过 / 需要删减 [...]
- 安全与回归：通过 / 需要补充 [...]
- 可维护性：通过 / 需要补充 [...]
```

## Bugfix Brief

适合：报错、行为异常、回归问题、线上问题复现。

```markdown
# Bugfix Brief

## 预期行为

[本来应该发生什么]

## 实际行为

[现在发生了什么]

## 复现步骤

1. ...
2. ...
3. ...

## 最近改动

[如果不知道，写未知]

## 可能根因

- [可能原因 1]：需要验证 [...]
- [可能原因 2]：需要验证 [...]

## 允许改动

- ...

## 不能改动

- ...

## 修好才算完成

- ...

## 验证方式

- ...

## 停止条件

- 如果连续两次修改后仍未解决，停止继续打补丁，重新分析根因。
- 如果无法复现，先停下来补复现信息。
- 如果修复需要改变受保护行为，先问用户。
```

给 AI Coding 工具时必须加：

```text
先说明可能的根因，再改代码。不要连续两次失败后还继续打补丁。
```

## Refactor Brief

适合：整理代码结构、降低耦合、提升可读性、迁移内部实现。

```markdown
# Refactor Brief

## 重构目标

[为什么要重构]

## 必须保持不变的行为

- ...

## 允许调整的内部结构

- ...

## 禁止调整的内容

- ...

## 风险点

- ...

## 验收方式

- 原有行为保持一致；
- 关键路径可运行；
- 如有测试，测试必须通过；
- 如无测试，至少给出人工验证步骤。

## 停止条件

- 需要改变外部行为；
- 需要改公共 API 或数据结构；
- 改动范围超出约定模块；
- 无法验证行为是否保持一致。
```

## Code Structure Guardrails

适合：前后端联调、状态管理、公共函数/组件、全局变量、命名混乱、代码耦合、长期维护风险。

生成前建议读取 `coding-guardrails.md`。如果项目结构未知，要求 AI Coding 工具先定位现有模式，不要编造架构。

```markdown
# Code Structure Guardrails

## 这次最容易出问题的代码结构风险

- ...

## 模块边界

允许改：
- ...

不能改：
- ...

调用规则：
- ...

## 前后端/API 边界

- ...

## 状态归属

- 新增状态归属：...
- 不要放到：...
- 清理时机：...

## 全局变量限制

- 不新增可变全局变量或模块级业务缓存。
- 如果必须使用全局状态，先说明局部状态为什么不够。

## 命名与调用关系

- 沿用现有命名风格。
- 不新增职责重复但名字不同的函数/组件/API。
- 如果函数职责变多，先拆清楚，不要塞进一个 handleXXX。

## 可维护性检查

- 是否复制了业务规则：是 / 否 / 需要检查
- 是否引入反向依赖：是 / 否 / 需要检查
- 是否新增隐形副作用：是 / 否 / 需要检查
- 是否有旧路径验证：是 / 否 / 需要补充

## Stop if

遇到以下情况停下来问：
- 需要新增或修改 API 字段；
- 需要新增全局状态；
- 需要跨层调用内部实现；
- 需要改变公共函数/公共组件行为；
- 无法判断状态归属或接口契约。
```

## Prompt Review 模板

适合：用户给出一段准备交给 AI Coding 工具的提示词，让你检查。

```markdown
## 这段描述容易跑偏的地方

1. ...

## 缺失的关键信息

- ...

## 可以带假设推进的点

- ...

## 必须先确认的点

- ...

## 改写后的 VibeGuard Brief

...
```

## Handoff Brief

适合：长对话压缩、交给下一轮 AI、从 Chat AI 转到 Coding Agent。

```markdown
# Handoff Brief

## 当前目标

[现在到底要完成什么]

## 已确认决策

- ...

## 已完成事项

- ...

## 未完成事项

- ...

## 关键上下文

- ...

## 不能改动

- ...

## 下一步只做

- ...

## 验收标准

- ...

## 需要用户确认的问题

- ...
```

## Current-Task Brief

这是最终复制给 AI Coding 工具的短版，尽量短而准。

```text
Use this task brief as the source of truth.
Implement only the current task. Do not expand scope.

Goal:

Allowed changes:

Must not change:

Code structure constraints:

Known context:

Assumptions:

Acceptance criteria:

Verification:

Stop and ask if:
```

## 中文 Current-Task Brief

```text
请把这份任务说明作为唯一准确信息来源。
只实现当前任务，不要扩展范围。

目标：

允许改动：

不能改动：

代码结构约束：

已知上下文：

关键假设：

验收标准：

验证方式：

遇到以下情况必须停下来问我：
```

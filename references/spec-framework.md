# Spec 框架生成规则

这个文件用于生成更合理、更科学的 Spec 框架。

VibeGuard 的 Spec 不是越长越好。好的 Spec 应该让 AI Coding 工具少猜、少跑偏、能验证、能停止、能交接。

## 目录

- Spec 的目标
- 什么时候需要 Spec
- Mini / Standard / Full 三档选择
- Spec 生成硬约束
- 推荐章节结构
- 上下文分层规则
- 需求写法规则
- 验收标准写法规则
- 任务拆解规则
- 质量门禁
- 输出模板

## Spec 的目标

生成 Spec 之前，先明确它解决什么问题：

1. 把用户真实目标转成可实现的需求。
2. 把范围和非目标写清楚，防止 AI 自动扩展。
3. 把事实、假设、未知项分开，防止 AI 把猜测当事实。
4. 把每条核心需求转成可验证的验收标准。
5. 把 Spec 压缩成 AI Coding 工具能执行的任务说明。

Spec 不是产品愿景长文，也不是项目管理文档。它应该服务于下一步编码。

## 什么时候需要 Spec

以下情况需要生成 Spec，而不是只生成普通 brief：

- 跨模块、跨页面、跨服务；
- 涉及登录、权限、支付、订阅、用户数据、隐私；
- 涉及数据结构、数据库、迁移、历史数据兼容；
- 涉及 API 契约、公共组件、公共函数；
- 需求里有多个用户角色或多个状态流转；
- 用户希望生成 PRD、技术方案、开发计划、任务拆解；
- 任务失败成本较高，或 AI 一旦理解错会大量返工；
- 长对话里已经出现多个版本方案，需要重新整理唯一准确信息源。

不需要 Spec 的情况：

- 单行文案；
- 小样式；
- 明确的单文件改动；
- 一次性实验；
- 用户只要一个短代码片段。

## Mini / Standard / Full 三档选择

### Mini Spec

适合：低风险，但需要比 Tiny Brief 更清楚的任务。

特征：

- 1-2 个模块；
- 需求基本清楚；
- 没有数据迁移、权限、支付等高风险；
- 验收方式简单。

建议长度：300-800 字。

必须包含：目标、范围/非目标、允许/禁止改动、验收标准、Current-Task Brief。

### Standard Spec

适合：普通功能、多个文件、有业务规则、需要明确验证方式。

特征：

- 涉及多个文件或页面；
- 有明确用户路径；
- 有一定业务规则；
- 需要测试或人工验证；
- 有少量假设和未知项。

建议长度：800-2000 字。

必须包含：Intent、User Scenario、Requirements、Non-goals、Constraints、Context、Acceptance、Task Plan、Validation。

### Full Spec

适合：高风险或跨模块任务。

特征：

- 登录、权限、支付、订阅、数据迁移、隐私；
- 跨模块/跨服务；
- 多角色、多状态、多数据流；
- 公共 API 或数据结构变化；
- 需要兼容旧行为；
- 无法本地简单验证，或回归风险高。

建议长度：1500-4000 字。除非用户明确要求，不要写更长。

必须包含：完整上下文分层、功能/非功能需求、兼容性约束、风险与回滚、验收矩阵、任务映射、停止条件。

## Spec 生成硬约束

生成 Spec 时必须遵守：

1. **每条核心需求必须可验证**：不能验证的内容改写、降级为背景，或标为需要确认。
2. **每条任务必须对应需求或验收标准**：避免任务漂移。
3. **非目标必须单独列出**：防止 AI 自行扩展。
4. **事实、假设、未知、废弃上下文必须分开**：不能把猜测写成事实。
5. **不写与实现决策无关的长背景**：只保留会影响实现的信息。
6. **不默认换技术栈、不默认重构、不默认新增依赖**：除非用户明确要求。
7. **不把所有内容都写成 Must**：区分 Must / Should / Could。
8. **不隐藏风险**：不确定和冲突要显式写出来。
9. **不生成无法执行的任务**：任务要能被 AI Coding 工具定位、修改、验证。
10. **不把 Spec 当最终交付**：最后要给一段短的 Current-Task Brief。

## 推荐章节结构

### Mini Spec 结构

```markdown
# Mini Spec

## 1. 目标

## 2. 范围

这次做：
-

这次不做：
-

## 3. 允许/禁止改动

允许：
-

禁止：
-

## 4. 验收标准

-

## 5. 给 AI Coding 工具的 Current-Task Brief
```

### Standard Spec 结构

```markdown
# Standard Spec

## 1. Intent：真正要解决的问题

## 2. User / Scenario：用户和场景

## 3. Requirements：功能需求

| ID | Requirement | Priority | Acceptance |
|---|---|---|---|
| R1 |  | Must | A1 |

## 4. Non-goals：这次不做

-

## 5. Constraints：约束

产品约束：
-

技术约束：
-

兼容性约束：
-

## 6. Context：上下文分层

Facts：
-

Assumptions：
-

Unknowns：
-

Deprecated context：
-

## 7. Acceptance Contract：验收合约

| ID | Given | When | Then | Verify by |
|---|---|---|---|---|
| A1 |  |  |  |  |

## 8. Task Plan：任务拆解

| Task | Related requirement | Related acceptance | Notes |
|---|---|---|---|
| T1 | R1 | A1 |  |

## 9. Stop Contract：停止条件

-

## 10. Current-Task Brief
```

### Full Spec 结构

```markdown
# Full Spec

## 1. Intent

## 2. Success Definition

## 3. Users / Roles / Scenarios

## 4. Functional Requirements

| ID | Requirement | Priority | Source | Acceptance |
|---|---|---|---|---|

## 5. Non-Functional Requirements

性能：
-

安全/权限：
-

兼容性：
-

可观测性：
-

## 6. Non-goals

-

## 7. Constraints

技术栈：
-

API / 数据结构：
-

不可改动区域：
-

## 8. Context Budget

Must read：
-

Read if needed：
-

Do not read yet：
-

Facts：
-

Assumptions：
-

Unknowns：
-

Deprecated context：
-

## 9. Risk Register

| Risk | Why it matters | Mitigation | Stop if |
|---|---|---|---|

## 10. Acceptance Matrix

| ID | Given | When | Then | Edge case | Verify by |
|---|---|---|---|---|

## 11. Task Plan

| Task | Change area | Related requirement | Related acceptance | Verification |
|---|---|---|---|---|

## 12. Rollback / Recovery Notes

## 13. Current-Task Brief
```

## 上下文分层规则

上下文必须分层，尤其是长对话和复杂任务。

### Facts

已经确认的事实。来源可以是用户明确说明、代码观察、文档、已验证行为。

写法：

```markdown
- [User-stated] 用户明确要求不改支付逻辑。
- [Code-observed] 当前登录跳转由 middleware 控制。
```

### Assumptions

合理但未确认的判断。必须说明如果不成立会怎样。

```markdown
- [Assumed] 默认沿用现有 UI 风格；如果不成立，需要补视觉规范。
```

### Unknowns

影响实现或验收的未知项。能问就问，不能问就写进 Stop Contract。

```markdown
- [Unknown] 暂不清楚是否需要兼容历史数据。
```

### Deprecated context

废弃方案、旧假设、历史讨论中已经不再采用的信息。写它的目的不是让 AI 使用，而是防止 AI 误用。

```markdown
- [Deprecated] 之前讨论过重写支付流程，但本次明确不做。
```

## 需求写法规则

好的需求应该：

- 描述可观察行为，而不是内部愿望；
- 每条只表达一个需求；
- 有优先级：Must / Should / Could；
- 有来源：用户明确说的、代码观察到的、合理假设；
- 能映射到至少一个验收标准。

避免：

- “页面更高级”；
- “体验更丝滑”；
- “逻辑更完善”；
- “系统更智能”；
- “代码更优雅”。

改写示例：

```markdown
不好：优化首页，让它更高级。
好：在不改变 CTA 行为和页面结构的前提下，提升首屏标题、副标题和按钮的视觉层级，移动端不破版。
```

## 验收标准写法规则

优先使用 Given / When / Then。

```markdown
Given 用户已登录
When 用户访问 /dashboard
Then 系统展示用户 Dashboard，而不是跳回登录页
Verify by 手动登录后访问 /dashboard，或运行相关路由测试
```

验收标准至少覆盖：

- 主路径；
- 边界条件；
- 错误路径；
- 权限/安全路径；
- 不应被破坏的旧行为；
- 如果适用，移动端/兼容性/性能。

不要只写“测试通过”。如果没有测试，写人工验证步骤。

## 任务拆解规则

任务要面向 AI Coding 工具可执行。

推荐顺序：

1. Locate：先定位相关模块和现有模式。
2. Understand：确认输入输出、状态流转、现有测试方式。
3. Modify：只在允许范围内改动。
4. Test：新增或更新测试；没有测试则写人工验证步骤。
5. Validate：运行可用检查，确认验收标准。
6. Summarize：输出变更摘要、验证结果、剩余风险。

任务拆解必须满足：

- 每个任务有明确改动区域；
- 每个任务关联一个 Requirement ID 或 Acceptance ID；
- 不把“实现整个功能”当成一个任务；
- 不把“优化代码”当成任务，除非明确优化什么；
- 不把“写测试”放到最后才想起，应与需求对应。

## 质量门禁

生成 Spec 后，必须自查：

### 1. 清晰性

- 一句话目标是否清楚？
- 范围和非目标是否一眼可见？
- 有没有模糊词没被改写？

### 2. 可验证性

- 每个 Must 需求是否有验收标准？
- 验收标准是否可执行？
- 是否覆盖主路径和关键边界？

### 3. 可执行性

- Task Plan 是否能直接交给 AI Coding 工具？
- 每个任务是否有明确改动区域？
- 是否需要先读代码/定位模块？

### 4. 一致性

- Requirements、Acceptance、Tasks 是否能互相映射？
- 是否出现需求里没提、任务里突然新增的内容？
- 是否出现验收标准覆盖不到的核心需求？

### 5. 最小性

- 是否写了与实现无关的长背景？
- 是否把小任务写成大工程？
- 是否有重复上下文？

### 6. 安全与回归

- 是否写了不能改动的区域？
- 是否覆盖权限、数据、隐私、兼容性风险？
- 是否有 Stop Contract？

### 7. 可维护性

- 是否明确模块边界和依赖方向？
- 是否明确新增状态、数据转换和副作用的归属？
- 是否限制不必要的全局变量、全局状态或模块级缓存？
- 是否说明前后端/API 契约，避免把后端规则写散到前端？
- 是否要求沿用现有命名和调用关系，避免新增平行实现？

## 输出模板：Spec 生成前判断

```markdown
## Spec 档位判断

建议档位：[Mini / Standard / Full]

原因：
- ...

不建议更重的原因：
- ...

必须补的信息：
- ...
```

## 输出模板：Spec 质量自查

```markdown
## Spec 自查

- 清晰性：通过 / 需要补充 [...]
- 可验证性：通过 / 需要补充 [...]
- 可执行性：通过 / 需要补充 [...]
- 一致性：通过 / 需要补充 [...]
- 最小性：通过 / 需要删减 [...]
- 安全与回归：通过 / 需要补充 [...]
- 可维护性：通过 / 需要补充 [...]
```

## 最重要的判断

如果一个 Spec 变长后并没有让 AI 更少猜、更容易验证、更清楚停在哪里，那它不是更科学，只是更重。

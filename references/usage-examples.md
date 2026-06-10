# VibeGuard 使用示例

这些示例用于参考结构和表达方式，不要原样照抄。输出时要结合用户当前信息改写。

## 示例 1：模糊产品想法

用户输入：

> 我想做一个记账小工具，能帮我看看这个需求怎么交给 AI 写吗？

处理方式：先轻量澄清，不要直接生成大工程方案。

应先问：

```text
我先确认几个会影响实现方向的问题，不展开成大需求评审：
1. 这个工具主要给你自己用，还是给别人用？
2. 第一版只需要记录支出，还是也要预算、分类、图表？
3. 数据打算存在本地、表格，还是数据库？
4. 什么结果出现时，你会觉得第一版“可以先用了”？
```

如果用户想先推进，可以给 GO WITH ASSUMPTIONS：

```markdown
## 开工判断

判断：GO WITH ASSUMPTIONS

可以先整理第一版 brief，但需要带着这些假设：
- 默认先做个人使用，不做多人协作；
- 默认第一版只记录支出，不做预算和图表；
- 默认数据先本地保存。
```

## 示例 2：清楚的小功能

用户输入：

> 帮我整理一段给 Cursor 的提示词：我想在现有 SaaS 首页加一个 pricing FAQ，只能改 landing page，不要动支付逻辑。

输出：

```text
Use this task brief as the source of truth.
Implement only the current task. Do not expand scope.

Goal:
Add a pricing FAQ section to the existing SaaS landing page.

Allowed changes:
- Landing page UI/content files only.
- Styling files directly related to the landing page if needed.

Must not change:
- Payment logic.
- Pricing calculation.
- Checkout flow.
- Authentication or backend APIs.

Known context:
- The user only wants a pricing FAQ on the landing page.
- Payment-related behavior must remain unchanged.

Assumptions:
- Use the existing landing page style and component patterns.

Acceptance criteria:
- The landing page includes a clear pricing FAQ section.
- Existing pricing CTA and checkout behavior remain unchanged.
- Page layout remains responsive.

Verification:
- Run the local build/check command if available.
- Manually check the landing page on desktop and mobile width.

Stop and ask if:
- The FAQ requires changing actual pricing rules.
- The relevant landing page file is unclear.
- You need to touch payment, checkout, auth, or backend files.
```

## 示例 3：修 bug

用户输入：

> 登录后跳转有问题，帮我写一段给 AI 的修复说明。

如果信息不足，应追问：

```text
修 bug 前先补最关键的信息，避免只把报错压下去：
1. 预期登录后跳到哪里？
2. 实际跳到了哪里？
3. 怎么复现？
4. 最近是否改过登录、路由、中间件或权限逻辑？
```

如果用户暂时不知道，可以输出带未知项的 Bugfix Brief：

```markdown
# Bugfix Brief

## 预期行为

需要确认：登录后应该跳转到哪个页面。

## 实际行为

已知：登录后跳转异常。具体跳转结果未知。

## 复现步骤

未知，需要用户补充。

## 可能根因

- 登录成功后的 redirect 参数处理异常：需要检查登录回调逻辑。
- 路由守卫/中间件判断异常：需要检查登录态判断与跳转条件。
- 最近路由改动导致默认跳转路径变化：需要检查近期改动。

## 停止条件

如果无法复现，先不要大改登录逻辑。连续两次修改仍未解决时，停止继续打补丁，重新分析根因。
```

给 AI Coding 工具时加：

```text
先说明可能的根因，再改代码。不要连续两次失败后还继续打补丁。
```

## 示例 4：检查容易跑偏的提示词

用户输入：

> 帮我看看这段提示词会不会让 AI 跑偏：帮我优化一下首页，让它更高级。

输出：

```markdown
## 这段描述容易跑偏的地方

1. “优化一下”太泛，不知道是视觉、文案、性能还是转化。
2. “更高级”不可验收，AI 可能会大改风格。
3. 没有说明允许改哪些文件。
4. 没有说明不能改价格、登录、支付、后端接口等高风险区域。
5. 没有验收标准。

## 建议补充的信息

- 首页这次主要优化首屏、价格区、FAQ，还是整体视觉？
- 是否保持现有品牌色和页面结构？
- 是否允许新增组件？

## 改写后的 VibeGuard Brief

### 一句话目标

在不改变首页信息结构和转化路径的前提下，提升首屏视觉层次和文案清晰度。

### 这次只做

- 调整首屏标题、副标题和 CTA 周围的视觉层次；
- 优化 spacing、字体层级和按钮状态；
- 保持现有品牌色和页面结构。

### 这次不做

- 不新增页面；
- 不改价格、支付、登录、后端接口；
- 不重构全站设计系统。

### 验收标准

- 首屏信息更清楚；
- CTA 仍然可见且行为不变；
- 移动端不破版；
- 现有构建或检查命令通过。
```

## 示例 5：重构

用户输入：

> 这个组件太乱了，帮我让 AI 重构一下。

处理方式：先限制“重构不是重写”。

```markdown
# Refactor Brief

## 重构目标

提升组件可读性和职责拆分，降低后续维护成本。

## 必须保持不变的行为

- 页面展示内容不变；
- 用户交互流程不变；
- 对外 props/API 不变；
- 埋点、请求、路由行为不变。

## 允许调整的内部结构

- 拆分内部小组件；
- 提取局部渲染逻辑；
- 整理命名和状态计算；
- 删除重复代码。

## 禁止调整的内容

- 不换技术栈；
- 不改变公共 API；
- 不新增业务功能；
- 不重构无关模块。

## 验收方式

- 原页面关键交互仍可用；
- 构建/测试通过；
- 如无测试，给出人工验证步骤。

## 停止条件

如果发现必须改变外部行为或公共 API，先停下来问用户。
```

## 示例 6：长对话交接

用户输入：

> 这轮对话太长了，帮我整理给下一轮 AI 接着做。

输出：

```markdown
# Handoff Brief

## 当前目标

[当前要完成的唯一目标]

## 已确认决策

- ...

## 已完成事项

- ...

## 未完成事项

- ...

## 关键上下文

事实：
- ...

假设：
- ...

未知：
- ...

## 下一步只做

- ...

## 禁止改动

- ...

## 验收标准

- ...

## 需要用户确认的问题

- ...
```

## 示例 7：高风险任务 No-go

用户输入：

> 帮我让 AI 把支付流程优化一下，顺便把订阅逻辑也改好。

输出：

```markdown
## 开工判断

判断：NO-GO

我不建议现在直接交给 AI 写代码。不是代码一定很难，而是这里涉及支付和订阅，边界不清很容易改坏关键流程。

必须先确认：
1. “优化支付流程”具体指哪个环节？价格页、checkout、支付回调，还是订阅状态展示？
2. 订阅逻辑要改什么？套餐规则、试用期、续费、取消，还是权限判断？
3. 哪些支付/订阅行为必须保持不变？
4. 怎么验证支付流程没有被改坏？

确认后再生成 Spec Brief。
```

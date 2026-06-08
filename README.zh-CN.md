# VibeGuard

**让 AI 写代码前，先把需求说明白。**

[English README](./README.md)

很多 AI 写代码的问题，其实不是从代码开始的。

而是从任务没说清楚开始的。

你让 AI 做一个功能，它一开始写得很快。然后它开始加你没要求的东西，改你没让它改的文件，修 bug 时只是在报错处打补丁，聊着聊着上下文越来越长，最后谁也说不清最开始到底想做什么。

VibeGuard 想解决的就是这个时刻：

> 在让 AI 写代码前，先写清楚：你想要什么、不想要什么、它能改哪里、不能改哪里、什么叫完成、什么时候必须停下来问你。

它不是一个新的 Coding Agent。它更像是你在使用 AI Coding 前的一张简短说明书。

## 最短版本

让 AI 写代码前，先写下这 6 件事：

1. **一句话目标**：这次到底要做什么？
2. **非目标**：这次明确不做什么？
3. **能改什么**：AI 可以改哪些地方？
4. **不能改什么**：哪些地方不能碰？
5. **什么叫完成**：怎样才算这个任务做完？
6. **什么时候停下来问**：什么情况不能继续猜？

这就是 VibeGuard 的核心。

## 为什么有用？

AI 很擅长顺着你给的信息继续写。

问题也在这里。

如果你的需求很模糊，它就会自己补。
如果聊天记录太长，旧想法和当前任务就会混在一起。
如果你只丢一句“这里报错了，修一下”，它很可能只是把报错压下去，而不是先搞清楚原因。

VibeGuard 的目标不是给 AI 更多上下文，而是给它更准的上下文。

不是让 AI 更快写。

是让 AI 少猜。

## 它会生成什么？

VibeGuard 会在你的项目里放一个小文件夹：

```text
.vibeguard/
  vision-lock.md
  context-budget.md
  acceptance-contract.md
  tasks.md
  current-task.md
  review.md
  handoff.md
```

这些文件不是事后补文档，而是给 AI 工作时看的当前上下文。

最重要的是：

```text
.vibeguard/current-task.md
```

很多时候，你不应该把一整段又长又乱的聊天记录丢给 AI。你只需要把当前任务说明给它。

## 快速开始

复制或克隆这个仓库后，在你的项目里初始化 VibeGuard 文件：

```bash
python scripts/vibeguard_init.py --project /path/to/your-project
```

编辑当前任务：

```text
/path/to/your-project/.vibeguard/current-task.md
```

生成一份短上下文：

```bash
python scripts/vibeguard_context.py --project /path/to/your-project
```

然后把生成的内容复制给你的 AI Coding 工具，让它只做这一个任务。

## 怎么跟 AI 说？

不要一上来就说：

```text
帮我写这个功能。
```

可以先说：

```text
先别写代码。
帮我把这个想法整理成一份 VibeGuard 说明书。

请先帮我明确：
- 一句话目标
- 目标用户和使用场景
- 第一版做到什么程度
- 这次明确不做什么
- 能改哪些地方
- 哪些地方不能改
- 什么叫完成
- 什么情况必须停下来问我

整理完之后，再输出一份 current-task brief，方便后面实现。
```

等说明书清楚以后，再让 AI 开始写代码。

## 修 bug 时怎么用？

不要只说：

```text
这里报错了，修一下。
```

更好的方式是给它：

```text
预期行为：
实际行为：
复现步骤：
最近改过什么：
允许改哪些文件：
哪些地方不能改：
什么叫修好：
什么情况要停下来问我：
```

再加一句：

```text
先说明可能的根因，再改代码。不要连续两次失败后还继续打补丁。
```

这样可以减少那种“报错没了，但代码越来越奇怪”的情况。

## 什么时候适合用？

适合这些场景：

- 你有一个产品想法，但还没完全想清楚
- AI 经常加你没要求的功能
- 你总是反复解释同一个需求
- 修 bug 修成一堆小补丁
- 聊天记录太长，后面越来越乱
- 你还不想上完整的 Spec-Driven Development 工具链，只想先有一个轻量习惯

## 什么时候没必要用？

这些情况可能没必要：

- 改一行文案
- 很小的 CSS 调整
- 非常明确的单文件改动
- 只是随手试验，正确性不重要

## 和 GitHub Spec Kit 有什么区别？

GitHub Spec Kit 是一套完整的 Spec-Driven Development 工具链。它有 CLI、Agent 集成、命令、扩展、预设和更完整的 SDD 流程。

VibeGuard 刻意做得更小。

它不是要替代 Spec Kit，而是给那些还不想装一整套工具链的人，一个更轻的开始方式。

简单说：

```text
Spec Kit：完整的 Spec-Driven Development 工具链。
VibeGuard：让 AI 写代码前先把需求说明白的小习惯。
```

## VibeGuard 不是什么？

VibeGuard 不是：

- Coding Agent
- 完整 Harness 运行时
- CI 系统
- 测试工具
- Code Review 替代品
- 保证 AI 一定写对代码的神器

它只是一个让 AI Coding 对话不那么含糊、更容易继续的小工具。

## 项目状态

早期公开版本。模板和流程已经可以用，但自动化部分刻意保持很轻。

## License

MIT

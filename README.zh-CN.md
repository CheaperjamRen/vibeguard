# VibeGuard 中文说明

VibeGuard 是一个轻量的 AI Coding 开工前 brief skill。

它的用途很直接：在让 AI Coding 工具真正改代码之前，先把任务目标、边界、假设、上下文、验收方式、停止条件和代码结构约束写清楚。它也补充了高信号 gotchas 和轻量 eval prompts，方便后续持续维护这个 skill。

## 安装

如果你的 Coding Agent 支持自定义 skill，把这个仓库目录复制到它的 skills/extensions 目录里，并确保 `SKILL.md` 位于目录根部。

常见方式：

```bash
git clone <your-repo-url> vibeguard
```

然后把 `vibeguard/` 文件夹复制或软链接到你的 Coding Agent 的自定义 skill 目录。

如果你使用的工具不支持直接安装 skill，也可以打开 `SKILL.md`，把它作为 system/custom instruction 使用。建议保留旁边的 `references/` 文件夹，因为 VibeGuard 会按任务需要读取里面的模板、检查清单和示例。

## 它解决什么问题

VibeGuard 主要用于写代码之前。

它会帮你先想清楚：

- 这次到底要改什么？
- 哪些明确不改？
- 哪些文件、模块、接口、数据结构允许改？
- 做完怎么算对？
- 遇到什么情况 AI 不能继续猜，必须停下来问你？
- 怎么避免代码耦合、全局状态、命名混乱、前后端边界不清这类后期很难查的问题？

它不负责运行测试，也不替代 Coding Agent。它更像是给 Coding Agent 的开工前说明书，让你把模糊需求变成更清楚、更可控的执行 brief。

## 适合什么时候用

适合这些场景：

- 把一个模糊产品想法整理成开发 brief；
- 准备把一个功能需求交给 AI Coding 工具；
- 修 bug，但不想让 AI 只是把报错压下去；
- 重构代码，但要保证外部行为不变；
- 检查一段 AI Coding prompt 是否容易跑偏；
- 判断当前需求能不能开工；
- 长对话后整理交接摘要，让下一轮 AI 接上；
- 一轮开发后生成版本更新说明或迭代日志；
- 给任务增加代码结构约束，比如耦合、状态归属、API 契约、全局变量和命名；
- 维护或改造这个 skill 时，用 gotchas 和 eval prompts 检查它是否仍然有效。

## 核心输出

- `VibeGuard Brief`：适合产品想法、功能开发、重构和复杂一点的任务。
- `Current-Task Brief`：可以直接复制给 AI Coding 工具的短任务说明。
- `Bugfix Brief`：整理预期行为、实际行为、复现步骤、根因检查和补丁边界。
- `Gate Check`：判断任务是 `GO`、`GO WITH ASSUMPTIONS`，还是 `NO-GO`。
- `Prompt Review`：检查一段 prompt 哪里容易让 AI 跑偏。
- `Handoff Brief`：把长对话压缩成下一轮 AI 可以接上的上下文。
- `Release Notes / Iteration Log`：总结这轮改了什么、为什么重要、还有什么没做。
- `Coding Guardrails`：补充代码结构约束，减少后期维护问题。
- `Gotchas / Evals`：记录高风险翻车点，并提供轻量 prompt 检查 skill 是否还能稳定产出有效 brief。

## 目录结构

```text
vibeguard/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── CHANGELOG.md
├── LICENSE
├── examples/
│   ├── feature-brief.md
│   ├── bugfix-brief.md
│   └── coding-guardrails.md
└── references/
    ├── README.md
    ├── templates.md
    ├── clarification.md
    ├── gates.md
    ├── failure-modes.md
    ├── gotchas.md
    ├── spec-framework.md
    ├── coding-guardrails.md
    ├── release-notes.md
    ├── usage-examples.md
    ├── evals.md
    └── wording.zh-CN.md
```

## 怎么使用

可以这样对你的 AI 助手说：

```text
Use VibeGuard to turn this feature idea into a Current-Task Brief before coding:
[描述你的功能]
```

也可以说：

```text
Use VibeGuard to check whether this AI Coding prompt is ready:
[粘贴你的 prompt]
```

如果你担心代码结构问题，可以说：

```text
Use VibeGuard coding guardrails for this task. I am worried about global variables, state ownership, and front-end/back-end boundary mistakes.
```

VibeGuard 会先判断任务是 tiny、standard 还是 spec-level。小任务保持轻量，复杂或高风险任务才读取更完整的 references。

## 设计原则

- 小任务就按小任务处理，不要为了显得专业写一大堆文档。
- 非目标和目标一样重要。
- 优先记录高信号 gotchas，不重复 AI Coding 工具默认知道的通用建议。
- 把事实、假设、未知、废弃上下文分开。
- 先写验收标准，再让 AI 实现。
- 上下文要短而准，不要把长聊天记录全塞进去。
- 不默认扩展范围。
- 不随便新增全局状态、跨层调用或抽象。
- 如果一个决策会改变实现方向，就让 AI 停下来问。

## License

MIT. See `LICENSE`.
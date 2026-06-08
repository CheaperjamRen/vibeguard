# VibeGuard

**A small brief before AI writes code.**

[中文说明](./README.zh-CN.md)

Most AI coding problems do not start in the code.
They start when the task is vague.

You ask an AI tool to build a feature. It starts fast. Then it adds things you did not ask for, changes files you did not expect, patches bugs without explaining the root cause, and the chat gets longer until nobody remembers the original idea clearly.

VibeGuard is a simple habit for that moment:

> Before asking AI to code, write down what you want, what you do not want, what it can change, what it must not change, what counts as done, and when it should stop and ask.

It is not a coding agent. It is a small pre-coding brief you can use before working with one.

## The shortest version

Before asking AI to code, write down:

1. **One-line goal** — what are we trying to do?
2. **Non-goals** — what should not be built now?
3. **Allowed changes** — where can the AI make changes?
4. **Must not change** — what should stay untouched?
5. **Done when** — how do we know the task is finished?
6. **Stop and ask if** — when should the AI pause instead of guessing?

That is the core of VibeGuard.

## Why this helps

AI is good at continuing from whatever you give it.

That is also the problem.

If the brief is vague, the model fills in the blanks. If the chat is long, old assumptions get mixed with current tasks. If a bug report only says “fix this”, the model may patch the symptom without understanding the cause.

VibeGuard tries to make guessing less necessary.

The goal is not to give the model more context. The goal is to give it better-scoped context.

## What VibeGuard creates

VibeGuard gives you a small folder in your project:

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

These files are not after-the-fact documentation. They are working context for AI coding.

The most important file is:

```text
.vibeguard/current-task.md
```

In many cases, you should give your AI coding tool the current task brief instead of a long messy chat history.

## Quick start

Clone or copy this repository, then initialize VibeGuard files in your project:

```bash
python scripts/vibeguard_init.py --project /path/to/your-project
```

Edit the current task:

```text
/path/to/your-project/.vibeguard/current-task.md
```

Generate a short context pack:

```bash
python scripts/vibeguard_context.py --project /path/to/your-project
```

Copy the generated context pack into your AI coding tool and ask it to implement only that task.

## How to use it with AI

Instead of saying:

```text
Build this feature for me.
```

Start with:

```text
Do not write code yet.
Help me turn this idea into a clear VibeGuard brief.

Clarify:
- one-line goal
- target user and scenario
- first version scope
- non-goals
- allowed changes
- must-not-change areas
- done-when criteria
- stop-and-ask conditions

After that, produce a current-task brief for implementation.
```

Then ask your AI coding tool to work from the current task brief or generated context pack.

## For bug fixes

Do not just paste an error and say “fix it”.

Give the AI:

```text
Expected behavior:
Actual behavior:
Steps to reproduce:
Recent changes:
Allowed files:
Must not change:
Done when:
Stop and ask if:
```

And add:

```text
Explain the likely root cause before changing code.
Do not keep patching the same symptom after two failed attempts.
```

This reduces the chance of patchy fixes that make the code harder to understand.

## When VibeGuard helps

Use it when:

- your product idea is still a bit fuzzy
- the AI keeps adding extra features you did not ask for
- you keep repeating the same requirement in different words
- a bug fix becomes a chain of small patches
- a long coding chat becomes hard to continue
- you want a lightweight habit before adopting a full spec-driven workflow

## When you probably do not need it

You probably do not need VibeGuard for:

- a one-line text change
- a tiny CSS tweak
- a very clear single-file edit
- throwaway experiments where correctness does not matter much

## How is this different from GitHub Spec Kit?

GitHub Spec Kit is a full Spec-Driven Development toolkit with a CLI, agent integrations, commands, extensions, presets, and a more complete SDD workflow.

VibeGuard is intentionally smaller.

It is for people who want some of the benefits of spec-first AI coding — clearer intent, better boundaries, acceptance criteria, and current-task context — without adopting a full SDD toolchain.

In short:

```text
Spec Kit: a full spec-driven development toolkit.
VibeGuard: a lightweight brief before AI writes code.
```

## What VibeGuard is not

VibeGuard is not:

- a coding agent
- a full harness runtime
- a CI system
- a test runner
- a replacement for code review
- a guarantee that AI will write correct code

It is a lightweight way to make AI coding conversations less vague and easier to continue.

## Project status

Early public version. The workflow and templates are usable, but the automation is intentionally small.

## License

MIT

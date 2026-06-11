# VibeGuard

[中文说明](README.zh-CN.md)

VibeGuard is a lightweight pre-coding brief skill for AI Coding workflows.

It helps you write down the task goal, boundaries, assumptions, context, acceptance checks, stop conditions, and code-structure guardrails before asking an AI Coding tool to edit code. It also includes high-signal gotchas and lightweight eval prompts for maintaining the skill over time.

## Install

If your Coding Agent supports custom skills, copy this repository folder into its custom skills directory and make sure `SKILL.md` stays at the root of the folder.

Common setup:

```bash
git clone <your-repo-url> vibeguard
```

Then place or symlink the `vibeguard/` folder into your agent's skills/extensions directory.

For tools that do not support skills directly, open `SKILL.md` and use it as a system/custom instruction. Keep the `references/` folder nearby, because the skill reads those files only when the current task needs more detail.

## What It Does

VibeGuard is for the step before code generation.

It helps answer:

- What are we trying to change?
- What should not change?
- Which files, modules, APIs, or data structures are allowed to move?
- What does “done” mean?
- What should the AI stop and ask about instead of guessing?
- How do we avoid accidental coupling, global state, unclear naming, or front/back-end boundary mistakes?

It does not run tests, edit files, or replace a Coding Agent. It produces clearer briefs and guardrails that you can paste into tools like Cursor, Copilot, ChatGPT, or any Coding Agent you use.

## When To Use

Use VibeGuard when you want to:

- turn a rough product idea into a coding brief;
- prepare a feature request for an AI Coding tool;
- fix a bug without letting the AI only suppress the error;
- refactor code while keeping external behavior unchanged;
- review a prompt before giving it to an AI Coding tool;
- decide whether a task is ready to start;
- create a handoff summary for a long coding conversation;
- write release notes or an iteration log after a round of changes;
- add code-structure constraints around coupling, state ownership, API contracts, global variables, and naming;
- maintain or adapt the skill using gotchas and lightweight eval prompts.

## Core Outputs

- `VibeGuard Brief`: a structured brief for product ideas, features, refactors, and larger tasks.
- `Current-Task Brief`: a short instruction block that can be pasted into an AI Coding tool.
- `Bugfix Brief`: expected behavior, actual behavior, reproduction, root-cause checks, and patch limits.
- `Gate Check`: `GO`, `GO WITH ASSUMPTIONS`, or `NO-GO`.
- `Prompt Review`: highlights where an AI Coding prompt may drift.
- `Handoff Brief`: compresses a long conversation into a clean next-step context.
- `Release Notes / Iteration Log`: summarizes what changed, why it matters, what remains, and what to do next.
- `Coding Guardrails`: adds code-structure constraints for maintainability.
- `Gotchas / Evals`: records high-risk failure points and lightweight prompts for checking whether the skill still works as intended.

## Repository Structure

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

## How To Use

Ask your AI assistant something like:

```text
Use VibeGuard to turn this feature idea into a Current-Task Brief before coding:
[describe your feature]
```

Or:

```text
Use VibeGuard to check whether this AI Coding prompt is ready:
[paste your prompt]
```

Or:

```text
Use VibeGuard coding guardrails for this task. I am worried about global variables, state ownership, and front-end/back-end boundary mistakes.
```

VibeGuard should first decide whether the task is tiny, standard, or spec-level. Small tasks should stay lightweight. Larger or risky tasks can use the relevant reference files.

## Design Principles

- Keep small tasks small.
- Write non-goals as clearly as goals.
- Prefer high-signal gotchas over generic AI Coding advice.
- Separate facts, assumptions, unknowns, and deprecated context.
- Define acceptance checks before implementation.
- Prefer short, accurate context over long pasted history.
- Avoid automatic scope expansion.
- Do not add global state, cross-layer calls, or new abstractions unless the task really needs them.
- Stop and ask when a decision changes implementation direction.

## License

MIT. See `LICENSE`.
# Evals

This file provides lightweight evaluation prompts for VibeGuard.

Use it when maintaining the skill, reviewing a change to `SKILL.md`, or checking whether VibeGuard still produces concrete, bounded, copy-ready briefs instead of generic advice.

## Directory

- How to use these evals
- Core eval cases
- Pass criteria
- Maintenance rule

## How to use these evals

Run 2-3 eval cases after changing VibeGuard. For each case, check whether the output includes concrete fields, useful boundaries, and a clear stop condition.

Do not treat these as unit tests with exact wording. They are behavior checks: the answer can vary, but it should protect the user from common AI Coding drift.

## Core eval cases

### 1. Vague feature idea

Input:

```text
Use VibeGuard to turn this into a coding brief:
Add CSV export to the dashboard.
```

Expected behavior:

- Produces a short feature brief, not a full reporting platform plan.
- Adds non-goals and allowed changes.
- Adds an acceptance check for exported columns, filters, and filename behavior.
- Adds a stop condition if the export requires a new backend endpoint or permission change.

### 2. Bug report with only an error

Input:

```text
Use VibeGuard for this bug:
The settings page crashes with undefined is not an object.
```

Expected behavior:

- Uses bugfix mode.
- Marks expected behavior, reproduction steps, and root-cause area as unknown if not provided.
- Does not suggest only adding optional chaining or suppressing the error.
- Adds a patch limit and a stop condition after repeated failed fixes.

### 3. Front-end/back-end boundary risk

Input:

```text
Use VibeGuard coding guardrails for this task:
Add a discount code field to checkout. I am worried the AI will mix UI validation, backend validation, pricing, and global state.
```

Expected behavior:

- Produces code-structure guardrails.
- Separates UI validation from backend discount validation and final pricing authority.
- Restricts global state unless the project already has a clear checkout state owner.
- Stops if the backend API does not already support discount validation.

### 4. Refactor with undefined unchanged behavior

Input:

```text
Use VibeGuard before coding:
Clean up the user profile module.
```

Expected behavior:

- Uses refactor brief or gate check.
- Defines external behavior that must remain unchanged.
- Limits allowed refactor area instead of proposing a rewrite.
- Adds regression checks and stop conditions.

### 5. Prompt review

Input:

```text
Use VibeGuard to review this prompt:
Make onboarding better. If anything is unclear, just decide yourself.
```

Expected behavior:

- Flags missing success definition, non-goals, allowed changes, verification, and stop conditions.
- Does not accept broad product/API/security decisions as low-risk assumptions.
- Rewrites the prompt with explicit assumptions and high-risk stop conditions.

### 6. Release notes target reader

Input:

```text
Use VibeGuard to write release notes for this iteration:
Added bugfix mode, refactor mode, and a new coding guardrails reference.
```

Expected behavior:

- Asks or infers the target reader when unclear.
- Avoids a changelog-only list.
- Explains why the changes matter and what users should do next.
- Does not invent metrics, adoption numbers, or repository details.

## Pass criteria

A VibeGuard output passes when it:

- Produces a usable brief or review, not just advice about writing better prompts.
- States goals, non-goals, allowed changes, and must-not-change items when relevant.
- Separates facts, assumptions, and unknowns.
- Turns risks into explicit constraints or stop conditions.
- Includes acceptance checks or manual verification steps.
- Keeps small tasks lightweight and does not expand scope automatically.

## Maintenance rule

When a real VibeGuard failure appears, add it as a new eval case with:

- Input prompt.
- Expected behavior.
- The failure it should prevent.
- Any reference file that should be read for the case.

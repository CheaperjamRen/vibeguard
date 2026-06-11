# Gotchas

This file collects high-signal failure points that VibeGuard should prevent.

Use it when a task looks simple but has hidden AI Coding risk: vague scope, missing acceptance checks, stale context, patchy bug fixes, code coupling, unclear state ownership, or front-end/back-end boundary confusion.

## Directory

- Why this file exists
- Gotchas to catch before coding
- How to turn a gotcha into a brief constraint
- Maintenance rule

## Why this file exists

A useful skill should not restate what an AI Coding tool already knows by default. The most valuable parts are the project-independent gotchas: the places where AI often produces plausible but risky output.

When a prompt contains one of these gotchas, do not only warn the user. Convert it into a concrete field in the brief: non-goal, allowed changes, must-not-change, assumption, unknown, stop condition, acceptance check, or code structure constraint.

## Gotchas to catch before coding

### 1. The task says what to add, but not what to avoid

Common input:

```text
Add CSV export to the dashboard.
```

Risk:

- AI may add a reporting system, new dependency, backend endpoint, permission model, or redesign.

Turn into:

- Non-goals;
- allowed changes;
- must-not-change;
- stop condition if a backend/API change seems necessary.

### 2. “Fix the bug” only includes an error message

Common input:

```text
This page crashes with undefined is not an object.
```

Risk:

- AI may suppress the crash instead of identifying why the value is undefined.

Turn into:

- expected behavior;
- actual behavior;
- reproduction status;
- likely root-cause area;
- patch limit;
- stop condition after repeated failed attempts.

### 3. Long context includes old decisions

Common input:

```text
Here is the whole chat history. Continue from it.
```

Risk:

- AI may treat old plans, rejected ideas, or outdated assumptions as current instructions.

Turn into:

- Current-task brief;
- facts;
- assumptions;
- unknowns;
- deprecated context.

### 4. The task crosses front-end and back-end but only describes UI

Common input:

```text
Add a discount code field to checkout.
```

Risk:

- AI may validate pricing only on the front-end, guess API errors, or change order creation behavior.

Turn into:

- front-end/back-end boundary;
- API contract;
- state ownership;
- stop condition if API fields or pricing rules need to change.

### 5. New state has no owner

Common input:

```text
Remember the selected item across screens.
```

Risk:

- AI may add global mutable state or module-level cache without lifecycle rules.

Turn into:

- state ownership;
- cleanup timing;
- global variable restriction;
- verification for user switch, page reload, and repeated open/close flows.

### 6. Function names hide multiple responsibilities

Common input:

```text
Update handleSubmit to support the new flow.
```

Risk:

- AI may put validation, save, navigation, analytics, error handling, and state reset into one generic handler.

Turn into:

- naming and call relationship constraints;
- reuse or split existing functions;
- do not create a parallel function with overlapping responsibility.

### 7. Refactor request does not define unchanged behavior

Common input:

```text
Clean this module up.
```

Risk:

- AI may rewrite architecture, change public behavior, or replace dependencies.

Turn into:

- unchanged behavior;
- allowed refactor area;
- forbidden changes;
- regression checks.

### 8. “Make it better” has no acceptance signal

Common input:

```text
Improve the onboarding experience.
```

Risk:

- AI may make arbitrary UX, copy, layout, or logic changes.

Turn into:

- observable success definition;
- behavior checks;
- UI checks;
- non-goals.

### 9. Missing verification becomes fake confidence

Common input:

```text
Just make sure tests pass.
```

Risk:

- Existing tests may not cover the changed behavior.

Turn into:

- exact test command if known;
- manual verification steps;
- sample inputs/outputs;
- note what is not verified.

### 10. The model wants to continue after the stop point

Common input:

```text
If something is unclear, just decide yourself.
```

Risk:

- AI may make product, API, data, or security decisions that should belong to the user.

Turn into:

- explicit low-risk assumptions;
- high-risk stop conditions;
- GO WITH ASSUMPTIONS or NO-GO.

## How to turn a gotcha into a brief constraint

| Gotcha | Brief field |
|---|---|
| Missing non-goals | `Non-goals`, `Must not change` |
| Bug only has error text | `Expected`, `Actual`, `Reproduction`, `Root-cause checks` |
| Old context mixed with current task | `Facts`, `Assumptions`, `Unknowns`, `Deprecated context` |
| Front-end/back-end boundary unclear | `API contract`, `Stop if API change is needed` |
| State has no owner | `State ownership`, `Global variable restriction` |
| Names hide responsibility | `Naming and call relationship constraints` |
| Refactor lacks unchanged behavior | `External behavior that must remain unchanged` |
| No acceptance signal | `Done when`, `Verification` |
| No real verification | `Manual checks`, `Unverified items` |
| User asks AI to decide too much | `Assumptions`, `Stop conditions`, `Gate decision` |

## Maintenance rule

When VibeGuard fails in a real use case, add the failure here in this format:

````markdown
### [Short gotcha name]

Common input:

```text
...
```

Risk:
- ...

Turn into:
- ...
````

Keep gotchas concrete. Avoid generic advice like “write better code” or “improve quality.”
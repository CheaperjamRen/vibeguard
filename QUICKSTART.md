# Quickstart

## 1. Initialize VibeGuard in a project

```bash
python scripts/vibeguard_init.py --project /path/to/your-project
```

This creates:

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

## 2. Fill the current task

Open:

```text
/path/to/your-project/.vibeguard/current-task.md
```

Write down:

- the task goal
- the related requirement
- allowed files or areas
- things the AI must not change
- acceptance criteria
- verification method
- stop conditions

## 3. Generate a context pack

```bash
python scripts/vibeguard_context.py --project /path/to/your-project
```

Copy the output into your AI coding tool.

## 4. Ask the AI to implement only this task

Example:

```text
Use this VibeGuard Context Pack as the source of truth.
Implement only the current task.
Do not expand scope.
Stop and ask if acceptance, files, or required context is unclear.
```

## 5. Review and update state

After implementation:

- record what changed in `review.md`
- update `tasks.md`
- update `current-task.md` for the next task
- update `handoff.md` if you may continue later

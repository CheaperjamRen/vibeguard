# Writing good AI coding briefs

A good AI coding brief should make guessing less necessary.

## Include

### Product intent

What are you trying to build, and why?

### Target user

Who is this for?

### First version scope

What should the first version include?

### Non-goals

What should not be built yet?

### Acceptance criteria

What must be true for the task to be considered done?

### Allowed changes

Which files, modules, or areas may be changed?

### Protected areas

Which files, modules, or behaviors must not be changed?

### Verification

How should the result be checked?

### Stop conditions

When should the AI stop and ask instead of continuing?

## Avoid

- asking for a broad feature without boundaries
- asking the AI to fix a bug without requiring root cause analysis
- mixing old discarded ideas with the current task
- letting the AI change unrelated files
- accepting code without checking the behavior against the brief

## Short template

```text
Goal:

User / scenario:

First version includes:

Not included:

Allowed changes:

Must not change:

Done when:

Verify by:

Stop and ask if:
```

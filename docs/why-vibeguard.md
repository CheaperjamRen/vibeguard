# Why VibeGuard

VibeGuard started from a simple observation: many AI coding failures are not pure coding failures.

They often happen because the instruction before coding is too vague.

A user may say:

```text
Build a dashboard for me.
```

But the AI still needs to guess:

- Who is the dashboard for?
- What is the first version supposed to show?
- What should not be built yet?
- What counts as done?
- What existing behavior must stay unchanged?
- What should the AI do when the requirement is unclear?

When these things are not written down, the model fills in the blanks. Sometimes that works. Often it leads to extra features, unnecessary abstractions, fragile patches, or code that no longer matches the original idea.

VibeGuard is a small habit for writing a clearer brief before coding starts.

It does not try to make AI coding fully automatic. It tries to make the next AI coding step easier to understand, easier to check, and easier to continue.

## The core idea

Do not give the AI more context by default.

Give it better-scoped context.

For each step, the AI should know:

- what the current task is
- what is allowed to change
- what must not change
- what counts as done
- how to verify the result
- when to stop and ask

That is what VibeGuard helps you write down.

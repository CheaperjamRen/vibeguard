# Example: simple feature request

## Rough request

```text
Add a due-date filter to my todo list.
```

## Better VibeGuard brief

```text
Goal:
Add a filter to the existing todo list so users can view tasks by due-date status.

User / scenario:
A user with many tasks wants to quickly see what is overdue, due today, upcoming, or has no due date.

First version includes:
- Filter options: all, overdue, today, upcoming, no due date
- Empty state when no tasks match
- Existing add, edit, complete, and delete behavior remains unchanged

Not included:
- Calendar view
- Notifications
- Recurring tasks
- Database schema redesign

Allowed changes:
- Todo list filtering UI
- Existing todo list state/filter logic
- Related tests if present

Must not change:
- Persistence format
- Task creation behavior
- Completed task toggle behavior

Done when:
- The filter works for all listed statuses
- Existing todo operations still work
- Empty state is shown for no matching tasks
- No unrelated files are changed

Stop and ask if:
- The current task model has no due-date field
- The feature requires changing persistence format
- Existing date handling is unclear
```

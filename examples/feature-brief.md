# Example: Feature Brief

Prompt:

```text
Use VibeGuard to prepare a Current-Task Brief before coding.

I want to add an export CSV button to an existing dashboard page. The button should export the currently visible table rows. Do not redesign the page.
```

Expected VibeGuard output shape:

```markdown
# VibeGuard Brief

## Goal

Add a CSV export button to the existing dashboard table.

## Non-goals

- Do not redesign the dashboard.
- Do not change table filtering or sorting behavior.
- Do not add a new reporting system.

## Allowed changes

- Dashboard table UI.
- CSV export helper if the project already has a utilities folder.

## Must not change

- Existing API response shape.
- Existing table filters.
- Existing route structure.

## Code structure constraints

- Keep export logic in a small helper or local module, not in global state.
- Reuse existing table row data instead of making a second API request unless necessary.
- Do not introduce a new dependency unless the project already uses one for CSV generation.

## Acceptance checks

- Exported CSV matches the currently visible rows.
- Empty table exports either an empty CSV with headers or shows the existing empty-state behavior.
- Existing dashboard interactions still work.

## Stop if

- The export requires changing backend API fields.
- The current visible row data is not available on the page.
- A new global store seems necessary.
```

# Example: refactor brief

## Rough request

```text
This settings page is messy. Refactor it.
```

## Better VibeGuard brief

```text
Goal:
Make the settings page easier to maintain without changing user-facing behavior.

User / scenario:
A developer needs to safely update settings logic without breaking existing options.

First version includes:
- Keep the same visible settings and behavior
- Separate display logic from save/update logic if they are currently mixed
- Remove duplicated local state only when the replacement is clear
- Add or update tests if the project already has a test pattern

Not included:
- New settings features
- UI redesign
- New state management library
- Backend API changes

Allowed changes:
- Settings page component
- Small helper functions near the settings page
- Existing tests for settings behavior

Must not change:
- Public API contract
- Settings names and values
- Existing routing

Done when:
- The settings page behaves the same as before
- Duplicated logic is reduced
- Data ownership is clearer
- No new global abstraction is introduced for one-time use

Stop and ask if:
- Existing behavior is unclear
- Refactor requires changing API or routing
- The task starts turning into a redesign
```

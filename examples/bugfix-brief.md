# Example: Bugfix Brief

Prompt:

```text
Use VibeGuard to prepare a bugfix brief.

The settings page sometimes shows the previous user's data after switching accounts.
```

Expected VibeGuard output shape:

```markdown
# Bugfix Brief

## Expected behavior

After switching accounts, the settings page should show only the current user's data.

## Actual behavior

The page sometimes shows data from the previous account.

## Reproduction

Unknown. Need confirmation.

## Likely risk area

- User/session state ownership.
- Client-side cache invalidation.
- Settings page data fetch lifecycle.

## Patch limits

- Do not hide the issue by forcing a full page reload unless confirmed.
- Do not add a global variable to track the current user.
- Do not suppress rendering errors without explaining the root cause.

## Code structure constraints

- Identify where user identity is stored and where settings data is fetched.
- Keep user-specific data tied to the current session/user ID.
- Clear or refetch stale settings data when the active user changes.

## Acceptance checks

- Switching from user A to user B never shows user A settings on user B's page.
- Refreshing the settings page still loads the correct current user.
- Existing login/logout flow still works.

## Stop if

- The project has multiple competing sources of current user state.
- The API does not return enough information to verify ownership.
- Fixing the issue requires changing authentication/session behavior.
```

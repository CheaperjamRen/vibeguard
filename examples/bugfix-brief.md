# Example: bugfix brief

## Rough request

```text
The upload progress sometimes gets stuck. Fix it.
```

## Better VibeGuard brief

```text
Goal:
Fix the upload progress UI so it reaches a correct final state after upload completion or failure.

User / scenario:
A user uploads a large file and expects the progress indicator to accurately show uploading, success, or failure.

First version includes:
- Identify the root cause before changing code
- Preserve existing upload API behavior
- Update progress state only where upload state is handled
- Show a clear final state for success and failure

Not included:
- New upload provider
- New retry system
- New file manager UI
- Redesigning the upload flow

Allowed changes:
- Upload progress state handling
- Upload progress display component
- Related tests if present

Must not change:
- Authentication
- File storage API
- Unrelated upload settings

Done when:
- Progress no longer stays in an intermediate state after success
- Failure state is visible when upload fails
- Existing successful uploads still work
- Root cause is explained in the review note

Stop and ask if:
- The root cause cannot be proven
- The fix requires changing the upload API contract
- Two patch attempts fail to fix the same symptom
```

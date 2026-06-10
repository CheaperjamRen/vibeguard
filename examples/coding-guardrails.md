# Example: Coding Guardrails

Prompt:

```text
Use VibeGuard coding guardrails before implementing this task.

I need to add a new discount code field to checkout. I am worried the AI will mix front-end validation, backend validation, and global state.
```

Expected VibeGuard output shape:

```markdown
# Code Structure Guardrails

## Main risk

Checkout changes can easily mix UI state, API contract, pricing rules, and payment behavior.

## Module boundaries

Allowed changes:
- Checkout form UI.
- Existing checkout validation flow if one exists.
- Existing API call wrapper only if the discount code field is already supported by the backend.

Must not change:
- Payment provider integration.
- Final price calculation source of truth.
- Existing order creation contract without confirmation.

## Front-end / back-end boundary

- Front-end can validate empty format and display feedback.
- Backend must validate whether the discount code is valid and what amount it applies.
- Do not calculate final discount amount only on the front-end.
- Do not guess backend error strings; use existing error codes/fields.

## State ownership

- Keep the discount code input state in the checkout form unless multiple pages need it.
- Do not add a global checkout discount variable.
- Clear temporary discount state when checkout resets or user leaves the flow.

## Naming and calls

- Reuse existing checkout API naming style.
- Do not create a second parallel checkout submit function.
- If existing submit logic becomes too large, separate discount validation clearly instead of hiding it inside a generic handler.

## Stop if

- Backend does not support discount code validation.
- Adding the field requires changing order pricing rules.
- The current project already has a promotion/coupon module with unclear ownership.
```

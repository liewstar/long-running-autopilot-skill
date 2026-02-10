# Resume Protocol

Use this protocol whenever a long-running session is interrupted.

## Recovery Anchor Contract

Each heartbeat must contain:

- `last_completed_step_id`
- `next_step_id`
- short note for pending blockers (if any)

Example anchor:

`Recovery-Anchor: step-12(refactor-parser) -> step-13(update-tests)`

## Resume Sequence

1. Restate the latest recovery anchor.
2. Confirm whether blocker state changed.
3. Continue directly from `next_step_id`.
4. Avoid re-running already completed steps unless required for safety.

## If Context Is Partially Lost

- Reconstruct from latest heartbeat fields: `Done`, `Now`, `Next`, `Recovery-Anchor`.
- Prefer forward progress over re-planning.
- Only re-ask questions if interruption gate conditions are currently true.


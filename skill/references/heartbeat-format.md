# Heartbeat Format

Send one heartbeat every 3-5 meaningful implementation steps.

Use this exact compact structure:

```text
Batch: <index>
Done: <completed actions in this batch>
Now: <current action>
Next: <next planned actions>
Assumptions: <defaults chosen, or "None">
Recovery-Anchor: <last_completed_step_id -> next_step_id>
Needs-Input: <only if hard blocker/high-risk; otherwise "None">
```

## Rules

- Keep each field concise and operational.
- Do not ask for confirmation in heartbeat unless interruption gate is met.
- Always include `Recovery-Anchor`.
- If no blocker, set `Needs-Input: None`.


# Interruption Decision Matrix

Use this matrix before deciding to ask the user a question.

| Situation | Ask user now? | Action |
|---|---:|---|
| Missing critical business requirement that cannot be inferred | Yes | Ask one focused question with concrete options |
| Permission/environment/dependency blocks execution | Yes | Report blocker + exact next action needed |
| High-risk destructive/irreversible action | Yes | Request explicit confirmation |
| Low-risk implementation detail (naming, local structure, reversible default) | No | Choose sensible default and continue |
| Non-critical ambiguity with safe reversible path | No | State assumption in heartbeat and proceed |
| Optional optimization or polish choice | No | Pick default aligned with current codebase |

## High-Risk Examples (Always Confirm)

- Large-scale file deletions.
- Git history rewrite operations with data-loss risk.
- Destructive database/data migrations.
- Irreversible external side effects.

## Question Quality Rules

When interruption is required:

1. Ask exactly one question if possible.
2. Include 2-4 concrete options.
3. Put recommended option first.
4. Explain impact in one short sentence.


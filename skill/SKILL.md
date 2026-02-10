---
name: long-running-autopilot
description: Use when tasks are large, multi-file, or cross-module and should be executed with minimal interruptions, autonomous batch progress, and questions only for hard blockers or high-risk actions.
---

# Long-Running Autopilot

## Overview

Run long tasks with sustained momentum. Optimize for fewer interruptions, clear progress heartbeats, and safe escalation only when truly needed.

Core principle: keep moving unless blocked.

## When to Use

- Large refactors or multi-step implementations.
- Broad project updates touching many files.
- Long debugging/migration work where frequent check-ins add noise.
- User explicitly asks for “long-running,” “autopilot,” or “don’t interrupt unless necessary.”

Do not use for tiny one-shot tasks where constant autonomy is unnecessary.

## Execution Contract

1. Work continuously in batches.
2. Send a heartbeat every 3-5 meaningful steps.
3. Do not pause for routine preferences that can be safely defaulted.
4. State assumptions in heartbeats and continue.
5. Keep output short and operational.

## Interruption Gate (Strict)

Only interrupt when one of these is true:

- Hard blocker: missing critical requirement that cannot be inferred.
- Hard blocker: environment/permission/dependency prevents forward progress.
- High-risk action: destructive or irreversible operation.

Never interrupt for low-risk implementation details (naming, local structure, reversible defaults, minor style choices).

## Risk Policy

Always request explicit confirmation before:

- Large-scale file deletion.
- History-rewriting git operations with potential loss.
- Destructive database/data migrations.
- External irreversible side effects.

Do not bypass platform/system safety and approval policies.

## Heartbeat Format

Use the compact format from `references/heartbeat-format.md`.

## Resume Protocol

Every heartbeat must carry a recovery anchor so interrupted sessions can resume without re-planning. Follow `references/resume-protocol.md`.

## References

- `references/decision-matrix.md`
- `references/heartbeat-format.md`
- `references/resume-protocol.md`


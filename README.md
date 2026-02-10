# long-running-autopilot

A reusable skill for Codex CLI and Claude Code that enables long-running, low-interruption execution for large tasks.

## What it does

- Runs work in continuous batches.
- Sends compact heartbeats every 3-5 meaningful steps.
- Interrupts only for hard blockers or high-risk actions.
- Includes explicit resume anchors for session recovery.

## Structure

- `skill/SKILL.md`
- `skill/agents/openai.yaml`
- `skill/references/decision-matrix.md`
- `skill/references/heartbeat-format.md`
- `skill/references/resume-protocol.md`

## Install (Codex)

Copy to:

```bash
~/.codex/skills/long-running-autopilot
```

## Install (Claude Code)

Copy to:

```bash
~/.claude/skills/long-running-autopilot
```

## Usage

Use this invocation prompt:

```text
使用 $long-running-autopilot 持续执行这个大型任务，仅在硬阻塞或高风险操作时再中断询问。
```

## License

MIT

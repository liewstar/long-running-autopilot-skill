# long-running-autopilot

[![Validate Skill](https://github.com/liewstar/long-running-autopilot-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/liewstar/long-running-autopilot-skill/actions/workflows/validate-skill.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

一个面向 **Codex CLI** 与 **Claude Code** 的长任务执行技能，目标是：

- 持续推进，不被低价值提问频繁打断；
- 只在真正阻塞或高风险操作时中断确认；
- 用固定心跳格式汇报进展，支持会话中断后无缝续跑。

> English README: [`README.md`](./README.md)

## 这个技能解决什么问题

在大型任务（跨模块重构、批量改造、迁移项目）中，AI 常见问题是：

- 进度被“是否继续？”这类非必要提问打断；
- 中断后难以快速恢复到上一个执行锚点；
- 安全边界不清晰，可能在高风险动作上处理不一致。

`long-running-autopilot` 通过统一执行契约解决以上问题。

## 核心能力

- **连续批次执行**：默认持续推进。
- **严格中断门禁**：仅硬阻塞才提问。
- **高风险保护**：破坏性/不可逆操作必须显式确认。
- **恢复锚点机制**：每次心跳包含恢复信息。

## 仓库结构

```text
.
├── skill/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── decision-matrix.md
│       ├── heartbeat-format.md
│       └── resume-protocol.md
├── README.md
├── README.zh-CN.md
└── tools/validate_skill.py
```

## 安装方式

### Codex CLI

```bash
mkdir -p ~/.codex/skills
cp -R ./skill ~/.codex/skills/long-running-autopilot
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R ./skill ~/.claude/skills/long-running-autopilot
```

安装后重启 CLI 会话即可生效。

## 使用示例

### 中文调用

```text
使用 $long-running-autopilot 持续执行这个大型任务，仅在硬阻塞或高风险操作时再中断询问。
```

### 英文调用

```text
Use $long-running-autopilot to execute this large task continuously and only interrupt for hard blockers or high-risk actions.
```

## 行为契约（摘要）

- **心跳节奏**：每 3-5 个关键步骤汇报一次。
- **默认策略**：低风险不确定项采用默认值并记录，不打断提问。
- **阻塞策略**：无法安全推进才提问。
- **风险策略**：高风险动作一律先确认再执行。

详细规则见：

- [`skill/SKILL.md`](./skill/SKILL.md)
- [`skill/references/decision-matrix.md`](./skill/references/decision-matrix.md)
- [`skill/references/heartbeat-format.md`](./skill/references/heartbeat-format.md)
- [`skill/references/resume-protocol.md`](./skill/references/resume-protocol.md)

## 校验

本地校验：

```bash
python3 tools/validate_skill.py
```

CI 也会在 push / pull request 自动运行同一校验。

## 参与贡献

请先阅读：

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)
- [`SECURITY.md`](./SECURITY.md)

## 版本记录

请查看 [`CHANGELOG.md`](./CHANGELOG.md)。

## License

MIT © Liao Xin


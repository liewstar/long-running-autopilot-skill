# Contributing Guide

Thanks for helping improve `long-running-autopilot`.

## Scope

Contributions are welcome for:

- Skill behavior clarity and safety.
- Better trigger wording in `skill/SKILL.md`.
- Improved reference docs and examples.
- Validation tooling and CI improvements.
- Localization (documentation translations).

## Development workflow

1. Fork this repository.
2. Create a feature branch.
3. Make focused, minimal changes.
4. Run local validation:

   ```bash
   python3 tools/validate_skill.py
   ```

5. Open a pull request with:
   - What changed.
   - Why it changed.
   - How you validated it.

## Style conventions

- Keep `SKILL.md` concise.
- Keep frontmatter limited to `name` and `description`.
- `description` should describe **when to use** (not process details).
- Keep heartbeat and decision rules explicit.
- Prefer practical examples over long theory.

## Pull request checklist

- [ ] Changes are scoped and documented.
- [ ] `tools/validate_skill.py` passes.
- [ ] Links in README/README.zh-CN are valid.
- [ ] No accidental secrets or private paths.


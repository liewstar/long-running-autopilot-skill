#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
REQUIRED_REFERENCES = [
    SKILL_DIR / "references" / "decision-matrix.md",
    SKILL_DIR / "references" / "heartbeat-format.md",
    SKILL_DIR / "references" / "resume-protocol.md",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def validate_skill_md() -> None:
    if not SKILL_MD.exists():
        fail(f"Missing file: {SKILL_MD}")

    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is missing or malformed")

    frontmatter = match.group(1)
    if "name: long-running-autopilot" not in frontmatter:
        fail("SKILL.md frontmatter name must be 'long-running-autopilot'")

    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not description_match:
        fail("SKILL.md frontmatter is missing description")

    description = description_match.group(1).strip().strip('"').strip("'")
    if not description.lower().startswith("use when"):
        fail("SKILL.md description should start with 'Use when'")

    ok("SKILL.md frontmatter is valid")


def validate_openai_yaml() -> None:
    if not OPENAI_YAML.exists():
        fail(f"Missing file: {OPENAI_YAML}")

    text = OPENAI_YAML.read_text(encoding="utf-8")
    if "display_name:" not in text:
        fail("openai.yaml is missing display_name")
    if "short_description:" not in text:
        fail("openai.yaml is missing short_description")
    if "default_prompt:" not in text:
        fail("openai.yaml is missing default_prompt")
    if "$long-running-autopilot" not in text:
        fail("openai.yaml default_prompt must include $long-running-autopilot")

    ok("openai.yaml contains required interface fields")


def validate_references() -> None:
    for reference in REQUIRED_REFERENCES:
        if not reference.exists():
            fail(f"Missing reference file: {reference}")
    ok("All required reference files exist")


def validate_readmes() -> None:
    readme_en = ROOT / "README.md"
    readme_zh = ROOT / "README.zh-CN.md"
    if not readme_en.exists():
        fail("Missing README.md")
    if not readme_zh.exists():
        fail("Missing README.zh-CN.md")

    en_text = readme_en.read_text(encoding="utf-8")
    zh_text = readme_zh.read_text(encoding="utf-8")

    if "README.zh-CN.md" not in en_text:
        fail("README.md should link to README.zh-CN.md")
    if "README.md" not in zh_text:
        fail("README.zh-CN.md should link to README.md")

    ok("Bilingual README files are present and cross-linked")


def main() -> None:
    print("Validating long-running-autopilot repository...")
    validate_skill_md()
    validate_openai_yaml()
    validate_references()
    validate_readmes()
    print("All checks passed.")


if __name__ == "__main__":
    main()


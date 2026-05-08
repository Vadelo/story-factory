#!/usr/bin/env python
"""Create Story Factory research corpora from seed files with king-research."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path.cwd()
CORPORA_DIR = SKILL_DIR / "assets" / "corpora"
KCTX = PROJECT_ROOT / ".king-context" / "bin" / "kctx.cmd"
KING_RESEARCH = PROJECT_ROOT / ".king-context" / "bin" / "king-research.cmd"


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"'))


def existing_research_docs() -> set[str]:
    if not KCTX.exists():
        return set()
    result = subprocess.run(
        [str(KCTX), "list", "research", "--json"],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return set()
    return set(re.findall(r'"name":\s*"([^"]+)"', result.stdout))


def parse_seed(seed_path: Path) -> tuple[str, list[str]]:
    text = seed_path.read_text(encoding="utf-8")
    match = re.search(r'king-research\s+"([^"]+)"\s+--([a-z]+)\s+--yes\s+--name\s+([a-z0-9-]+)', text)
    if not match:
        raise ValueError(f"Could not parse recommended command from {seed_path}")
    topic, effort, slug = match.groups()
    return slug, [str(KING_RESEARCH), topic, f"--{effort}", "--yes", "--name", slug]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print commands without running")
    args = parser.parse_args()

    load_env_file(PROJECT_ROOT / ".env")
    load_env_file(PROJECT_ROOT / ".king-context" / ".env")

    missing_keys = [key for key in ("EXA_API_KEY", "OPENROUTER_API_KEY") if not os.environ.get(key)]
    if missing_keys and not args.dry_run:
        raise SystemExit(
            "Missing required keys: "
            + ", ".join(missing_keys)
            + ". Copy .king-context/.env.example to .king-context/.env and fill them."
        )

    existing = existing_research_docs()
    for seed in sorted(CORPORA_DIR.glob("*.md")):
        slug, command = parse_seed(seed)
        if slug in existing:
            print(f"Already indexed: {slug}")
            continue
        if args.dry_run:
            print(" ".join(command))
            continue
        print(f"Creating research corpus: {slug}")
        subprocess.run(command, cwd=PROJECT_ROOT, check=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Build a King Context works corpus from a Story Factory project JSON."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_SECTION_FIELDS = (
    "title",
    "path",
    "url",
    "keywords",
    "use_cases",
    "tags",
    "priority",
    "source_type",
    "content",
)


def slugify(text: str) -> str:
    value = text.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "story-work"


def to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, indent=2, ensure_ascii=False)


def section(
    title: str,
    path: str,
    content: Any,
    tags: list[str],
    priority: int = 5,
    keywords: list[str] | None = None,
    use_cases: list[str] | None = None,
    base_url: str = "local://works/story-work",
) -> dict[str, Any] | None:
    text = to_text(content).strip()
    if not text:
        return None
    return {
        "title": title,
        "path": path,
        "url": f"{base_url}#{path}",
        "keywords": keywords or tags,
        "use_cases": use_cases or [f"Recall {title.lower()} for story continuation"],
        "tags": tags,
        "priority": priority,
        "source_type": "work",
        "content": text,
    }


def build(project: dict[str, Any]) -> dict[str, Any]:
    title = project.get("title") or "Untitled Story"
    slug = slugify(project.get("slug") or title)
    base_url = f"local://works/{slug}"
    bible = project.get("bible", {})

    raw_sections: list[dict[str, Any] | None] = [
        section("Current Brief", "brief-current", project.get("brief"), ["brief", "canon"], 9, base_url=base_url),
        section("Canon: Premise", "canon-premise", bible.get("premise"), ["canon", "premise"], 10, base_url=base_url),
        section("Canon: Themes", "canon-themes", bible.get("themes"), ["canon", "themes"], 8, base_url=base_url),
        section("Genre Contract", "genre-contract", bible.get("genre_contract"), ["genre", "promise"], 8, base_url=base_url),
        section("Characters", "characters", bible.get("characters"), ["characters", "canon"], 10, base_url=base_url),
        section("Relationships", "relationships", bible.get("relationships"), ["relationships", "characters"], 8, base_url=base_url),
        section("World Rules", "world-rules", bible.get("world"), ["world", "rules", "setting"], 9, base_url=base_url),
        section("Timeline", "timeline", bible.get("timeline"), ["timeline", "continuity"], 10, base_url=base_url),
        section("Outline", "outline", bible.get("outline"), ["outline", "plot"], 9, base_url=base_url),
        section("Style Guide", "style-guide", bible.get("style_guide"), ["style", "voice"], 9, base_url=base_url),
        section("Continuity Ledger", "continuity-ledger", bible.get("continuity_ledger"), ["continuity", "canon"], 10, base_url=base_url),
        section("Open Threads", "open-threads", bible.get("open_threads"), ["open-threads", "plot"], 9, base_url=base_url),
        section("Revision History", "revision-history", project.get("revision_history"), ["revision", "history"], 4, base_url=base_url),
    ]

    for draft in project.get("drafts", []):
        draft_id = slugify(draft.get("id") or draft.get("title") or "draft")
        content = {
            "title": draft.get("title", draft_id),
            "summary": draft.get("summary", ""),
            "content_md": draft.get("content_md", ""),
            "canon_changes": draft.get("canon_changes", []),
            "continuity_notes": draft.get("continuity_notes", []),
        }
        raw_sections.append(
            section(
                f"Draft: {content['title']}",
                f"draft-{draft_id}",
                content,
                ["draft", "continuation"],
                7,
                base_url=base_url,
            )
        )

    corpus = {
        "name": slug,
        "display_name": title,
        "version": project.get("version", "v1"),
        "base_url": base_url,
        "sections": [item for item in raw_sections if item is not None],
    }
    validate_corpus(corpus)
    return corpus


def validate_corpus(corpus: dict[str, Any]) -> None:
    for field in ("name", "display_name", "version", "base_url", "sections"):
        if field not in corpus:
            raise ValueError(f"Missing corpus field: {field}")
    for idx, item in enumerate(corpus["sections"]):
        missing = [field for field in REQUIRED_SECTION_FIELDS if field not in item]
        if missing:
            raise ValueError(f"Section {idx} missing fields: {', '.join(missing)}")
        if item["source_type"] != "work":
            raise ValueError(f"Section {idx} must use source_type='work'")
        for list_field in ("keywords", "use_cases", "tags"):
            if not isinstance(item[list_field], list):
                raise ValueError(f"Section {idx} field '{list_field}' must be a list")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Story project JSON")
    parser.add_argument("--output", type=Path, default=None, help="Output King Context corpus JSON")
    args = parser.parse_args()

    project = json.loads(args.input.read_text(encoding="utf-8"))
    corpus = build(project)
    output = args.output or Path(".king-context") / "data" / "works" / f"{corpus['name']}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(corpus, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {output} with {len(corpus['sections'])} sections")


if __name__ == "__main__":
    main()

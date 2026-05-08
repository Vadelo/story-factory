#!/usr/bin/env python
"""Append a chapter memory packet to a King Context works corpus."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
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
    value = unicodedata.normalize("NFKD", text.lower().strip())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "chapter"


def to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, indent=2, ensure_ascii=False)


def make_section(
    corpus: dict[str, Any],
    title: str,
    path: str,
    content: Any,
    tags: list[str],
    priority: int,
    use_case: str,
) -> dict[str, Any] | None:
    text = to_text(content).strip()
    if not text:
        return None
    base_url = corpus.get("base_url") or f"local://works/{corpus['name']}"
    extra_keywords = []
    for field in ("style_notes", "canon_changes"):
        for item in content.get(field, []) if isinstance(content, dict) else []:
            if isinstance(item, str):
                extra_keywords.extend(slugify(part) for part in item.split()[:12])
    clean_keywords = []
    for item in tags + extra_keywords:
        if item and item not in clean_keywords:
            clean_keywords.append(item)
    return {
        "title": title,
        "path": path,
        "url": f"{base_url}#{path}",
        "keywords": clean_keywords,
        "use_cases": [use_case],
        "tags": tags,
        "priority": priority,
        "source_type": "work",
        "content": text,
    }


def upsert_sections(corpus: dict[str, Any], new_sections: list[dict[str, Any]]) -> None:
    by_path = {section.get("path"): section for section in corpus.get("sections", [])}
    for section in new_sections:
        by_path[section["path"]] = section
    corpus["sections"] = list(by_path.values())
    validate_corpus(corpus)


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


def chapter_sections(corpus: dict[str, Any], packet: dict[str, Any]) -> list[dict[str, Any]]:
    chapter_id = slugify(
        packet.get("chapter_id")
        or f"chapter-{packet.get('chapter_number', '')}"
        or packet.get("title", "chapter")
    )
    label = packet.get("title") or chapter_id
    prefix = chapter_id
    candidates = [
        make_section(
            corpus,
            f"Chapter Text: {label}",
            f"{prefix}-text",
            packet.get("content_md"),
            ["chapter", "draft", "text", chapter_id],
            7,
            "Read the canonical chapter text before continuing or revising the work",
        ),
        make_section(
            corpus,
            f"Chapter Summary: {label}",
            f"{prefix}-summary",
            packet.get("summary"),
            ["chapter", "summary", chapter_id],
            10,
            "Recall what happened in this chapter",
        ),
        make_section(
            corpus,
            f"Chapter Canon Delta: {label}",
            f"{prefix}-canon-delta",
            {
                "canon_changes": packet.get("canon_changes", []),
                "world_updates": packet.get("world_updates", []),
            },
            ["chapter", "canon", "world", chapter_id],
            10,
            "Recall canon and world changes introduced by this chapter",
        ),
        make_section(
            corpus,
            f"Chapter Character States: {label}",
            f"{prefix}-character-states",
            {
                "character_states": packet.get("character_states", []),
                "relationship_changes": packet.get("relationship_changes", []),
            },
            ["chapter", "characters", "relationships", chapter_id],
            10,
            "Recall character and relationship states after this chapter",
        ),
        make_section(
            corpus,
            f"Chapter Timeline: {label}",
            f"{prefix}-timeline",
            packet.get("timeline_updates", []),
            ["chapter", "timeline", "continuity", chapter_id],
            9,
            "Recall timeline changes from this chapter",
        ),
        make_section(
            corpus,
            f"Chapter Threads: {label}",
            f"{prefix}-threads",
            {
                "new_threads": packet.get("new_threads", []),
                "resolved_threads": packet.get("resolved_threads", []),
                "callbacks": packet.get("callbacks", []),
            },
            ["chapter", "threads", "callbacks", chapter_id],
            9,
            "Recall open and resolved story threads for this chapter",
        ),
        make_section(
            corpus,
            f"Chapter Continuity: {label}",
            f"{prefix}-continuity",
            {
                "continuity_risks": packet.get("continuity_risks", []),
                "style_notes": packet.get("style_notes", []),
            },
            ["chapter", "continuity", "style", chapter_id],
            8,
            "Check continuity and style risks before future drafting",
        ),
    ]
    return [section for section in candidates if section is not None]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", type=Path, help="Existing .king-context/data/works/<work>.json")
    parser.add_argument("packet", type=Path, help="Chapter memory packet JSON")
    args = parser.parse_args()

    corpus = json.loads(args.corpus.read_text(encoding="utf-8"))
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    packet_slug = packet.get("work_slug")
    if packet_slug and packet_slug != corpus.get("name"):
        raise SystemExit(f"Packet work_slug '{packet_slug}' does not match corpus '{corpus.get('name')}'")

    new_sections = chapter_sections(corpus, packet)
    upsert_sections(corpus, new_sections)
    args.corpus.write_text(json.dumps(corpus, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Updated {args.corpus} with {len(new_sections)} chapter memory sections")


if __name__ == "__main__":
    main()

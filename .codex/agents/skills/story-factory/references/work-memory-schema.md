# Work Memory Schema

Each work should produce Markdown and JSON.

## Markdown Layout

```markdown
# <Title>

## Story Bible

### Premise
### Genre Promise
### Themes
### Characters
### World
### Timeline
### Outline
### Style Guide
### Continuity Ledger

## Draft

<chapter or scene text>
```

## JSON Layout

```json
{
  "slug": "work-slug",
  "title": "Title",
  "language": "pt-BR",
  "form": "novel",
  "brief": {},
  "bible": {
    "premise": "",
    "themes": [],
    "genre_contract": {},
    "characters": [],
    "world": {},
    "timeline": [],
    "outline": [],
    "style_guide": {},
    "continuity_ledger": [],
    "open_threads": []
  },
  "drafts": [
    {
      "id": "chapter-001",
      "title": "",
      "content_md": "",
      "summary": "",
      "canon_changes": [],
      "continuity_notes": []
    }
  ],
  "revision_history": []
}
```

## King Context Work Corpus JSON

The indexed corpus must follow King Context's section format:

```json
{
  "name": "work-slug",
  "display_name": "Title",
  "version": "v1",
  "base_url": "local://works/work-slug",
  "sections": [
    {
      "title": "Canon: Premise",
      "path": "canon-premise",
      "url": "local://works/work-slug#canon-premise",
      "keywords": ["premise", "canon", "story"],
      "use_cases": ["Recall the central premise before continuing the work"],
      "tags": ["canon", "premise"],
      "priority": 10,
      "source_type": "work",
      "content": "..."
    }
  ]
}
```

Every section, including chapter-specific memory sections, must use the same King Context corpus section contract:

| Field | Type | Required |
|---|---|---|
| `title` | string | yes |
| `path` | string filename-safe slug | yes |
| `url` | string, usually `local://works/<slug>#<path>` | yes |
| `keywords` | string array | yes |
| `use_cases` | string array | yes |
| `tags` | string array | yes |
| `priority` | integer | yes |
| `source_type` | `"work"` | yes |
| `content` | string | yes |

Do not create ad hoc chapter memory files that bypass this format. Chapter packets may exist as intermediate JSON, but the saved corpus must always become King Context sections.

Recommended section paths:

- `brief-current`
- `canon-premise`
- `canon-themes`
- `characters`
- `relationships`
- `world-rules`
- `timeline`
- `outline`
- `style-guide`
- `continuity-ledger`
- `open-threads`
- `draft-<unit-id>`
- `chapter-<number>-text`
- `chapter-<number>-summary`
- `chapter-<number>-canon-delta`
- `chapter-<number>-character-states`
- `chapter-<number>-timeline`
- `chapter-<number>-threads`
- `chapter-<number>-continuity`
- `revision-history`

## Chapter Memory Packet

After each chapter or major scene, append a packet like:

```json
{
  "work_slug": "work-slug",
  "chapter_id": "chapter-001",
  "chapter_number": 1,
  "title": "Chapter Title",
  "content_md": "Full chapter text or approved canonical excerpt",
  "summary": "What happened in this chapter",
  "canon_changes": [],
  "character_states": [],
  "relationship_changes": [],
  "world_updates": [],
  "timeline_updates": [],
  "new_threads": [],
  "resolved_threads": [],
  "callbacks": [],
  "continuity_risks": [],
  "style_notes": []
}
```

The chapter packet is not optional for long-form work. It is the primary mechanism that lets future sessions continue the same work without losing context.

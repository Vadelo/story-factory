---
name: king-context
description: Search and read indexed King Context docs, research corpora, and work memory through `.king-context/bin/kctx`. Use when the user asks to look up indexed documentation, query previous research, inspect corpus topics, read sections, grep indexed content, or use King Context as local retrieval memory.
---

# King Context

Use `.king-context/bin/kctx` as the retrieval interface. Search first, preview before full reads, and scope aggressively.

## Stores

- `docs`: scraped product/API documentation from `king-scrape`.
- `research`: topic research corpora from `king-research`.
- `works`: project/work-specific memory corpora when this local King Context supports them.

If a command rejects `works`, fall back to `docs` and `research`; the current installation may not have the work-memory extension yet.

## Retrieval Workflow

1. Check `.king-context/_learned/` for an existing shortcut when a doc/topic is known.
2. Run `kctx list` or `kctx list <source>` to identify available corpora.
3. Run `kctx search "<query>" --source <source> --top 3` or `--doc <slug>`.
4. Run `kctx read <doc> <section> --preview`.
5. Read the full section only after the preview confirms relevance.
6. Save useful discoveries in `.king-context/_learned/<doc-name>.md`.

## Commands

```bash
.king-context/bin/kctx list
.king-context/bin/kctx list docs
.king-context/bin/kctx list research
.king-context/bin/kctx list works
.king-context/bin/kctx search "query" --top 3
.king-context/bin/kctx search "query" --doc <slug>
.king-context/bin/kctx read <doc> <section> --preview
.king-context/bin/kctx read <doc> <section>
.king-context/bin/kctx topics <doc>
.king-context/bin/kctx grep "pattern" --doc <slug>
.king-context/bin/kctx index .king-context/data/<file>.json
.king-context/bin/kctx index --all
```

## Search Rules

- Prefer `search` over `grep` unless looking for exact strings or code patterns.
- Prefer `--doc` when the corpus slug is known.
- Use `--source research` for open-web topic corpora.
- Use `--source works` for a single story, book, campaign, screenplay, or other project memory corpus when available.
- Keep queries short: one to three meaningful terms usually works best.
- Do not read every section of a corpus. Search, preview, then read.

## Learned Shortcuts

Write discoveries as:

```markdown
# <Doc Name> - Learned Shortcuts

## <Topic>
- **<What>** -> `<section-path>` section
- Store: docs | research | works
- Gotcha: <non-obvious behavior>

---
Last updated: YYYY-MM-DD
```

Verify a learned path with `kctx read` before relying on it.

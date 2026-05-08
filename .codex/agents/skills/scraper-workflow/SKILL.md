---
name: scraper-workflow
description: Scrape, filter, enrich, export, and index documentation into King Context with `.king-context/bin/king-scrape` and `.king-context/bin/kctx`. Use when the user asks to scrape docs, crawl documentation, index docs from a URL, add product/API documentation, or build a local docs corpus.
---

# Scraper Workflow

Use this for documentation sites. For open-web topic research, use `king-research`.

## Rules

- Always pass `--name <slug>` to `king-scrape`.
- Index the exported JSON with `.king-context/bin/kctx index`; do not use `seed_data`.
- If using Codex subagents for enrichment, only do so when the user explicitly asks for delegated/parallel agent work.
- If not using subagents, prefer the automated CLI workflow.
- For destructive cleanup of `.king-context/_temp/<slug>`, ask before deleting.

## Resolve Input

If the user gives a deep docs URL, derive the docs root:

- Keep `/docs` when the URL contains `/docs/...`.
- Cut at `/api`, `/reference`, or `/guides` when those are the documentation root.
- If unsure, use the domain root and keep the original URL as a topic hint.

If no URL is provided, search for the official docs URL or ask the user for it.

Detect topic filters from phrases like "only auth", "just audio", "about TTS", or a deep link that implies a subset.

## Automated Workflow

For a full docs corpus:

```bash
.king-context/bin/king-scrape <base-url> --name <slug> --yes
.king-context/bin/kctx index .king-context/data/<slug>.json
```

For a filtered corpus, prepare or let the CLI filter by topic when available. If manual filtering is needed, write:

- `.king-context/_temp/<slug>/discovered_urls.json`
- `.king-context/_temp/<slug>/filtered_urls.json`
- `.king-context/_temp/<slug>/manifest.json`

Then resume:

```bash
.king-context/bin/king-scrape <base-url> --name <slug> --yes --step fetch
.king-context/bin/kctx index .king-context/data/<slug>.json
```

## Resume

Before starting, check `.king-context/_temp/<slug>/manifest.json` when a work dir exists. Summarize progress and continue from the latest stage unless the user asks for a fresh run.

## Codex-Agent Workflow

Use only when explicitly requested by the user. Run fetch/chunk first:

```bash
.king-context/bin/king-scrape <base-url> --name <slug> --no-llm-filter --stop-after chunk
```

Then delegate bounded enrichment batches to workers. Tell workers:

- They are not alone in the workspace.
- They must not revert edits from others.
- They should write enriched batch JSON files under `.king-context/_temp/<slug>/enriched/`.

After batches exist:

```bash
.king-context/bin/king-scrape <base-url> --name <slug> --step export
.king-context/bin/kctx index .king-context/data/<slug>.json
```

## Output

Report the slug, section count if available, and search examples:

```bash
.king-context/bin/kctx search "auth" --doc <slug>
.king-context/bin/kctx topics <slug>
```

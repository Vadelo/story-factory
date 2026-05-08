---
name: king-decisions
description: Retrieve indexed project ADRs and architectural decision history through `.king-context/bin/kctx adr`. Use when the user asks why the project uses something, whether a decision exists, what the current architecture decision is, what changed historically, or whether a planned change conflicts with prior decisions.
---

# King Decisions

Retrieve architectural decisions through `.king-context/bin/kctx adr`.

## Workflow

1. Run `.king-context/bin/kctx adr status`.
2. If stale, run `.king-context/bin/kctx adr index`.
3. Search active decisions:

```bash
.king-context/bin/kctx adr search "<topic>" --active --top 5
```

4. Read previews for likely matches.
5. Use timeline when history, supersession, or change rationale matters:

```bash
.king-context/bin/kctx adr timeline "<topic>"
```

## Rules

- Prefer active ADRs for current guidance.
- Cite ADR IDs.
- Mention superseded ADRs only when they affect the answer.
- If no ADR exists, say no indexed decision was found.
- Do not scan `.king-context/adr/*.md` directly for retrieval; use `kctx adr`.

## Output

State the current decision first, then relevant history or conflicts. Keep it concise and evidence-oriented.

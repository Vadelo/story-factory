---
name: king-record-decision
description: Create and maintain project ADRs through `.king-context/bin/kctx adr`. Use when the user asks to create an ADR, register a decision, document an architecture choice, supersede an old decision, or record why the project changed direction.
---

# King Record Decision

Create or update ADRs through `.king-context/bin/kctx adr`.

## Before Writing

1. Run `.king-context/bin/kctx adr status`.
2. If stale, run `.king-context/bin/kctx adr index`.
3. Search active decisions for the topic and key technologies.
4. Read previews for likely matches.
5. Use timeline if a previous decision may be superseded.

Do not scan `.king-context/adr/*.md` for discovery. Use the ADR CLI.

## Classify Matches

- `superseded-by-new`: the new ADR replaces this decision.
- `related`: relevant but still valid.
- `conflict`: contradicts an active ADR and needs user confirmation.
- `irrelevant`: do not link.

## Creation Rules

- Use `--supersedes` when replacing an ADR and include a concrete reason.
- Use `--related` for nearby architecture decisions that remain valid.
- Ask before writing if an unresolved conflict exists.
- Read or edit ADR markdown only when creating a new ADR or updating a specific ADR selected by this workflow.

## Validation

After writing:

```bash
.king-context/bin/kctx adr index
.king-context/bin/kctx adr validate
.king-context/bin/kctx adr timeline "<topic>"
```

## Output

Name the ADR created or changed, list superseded and related ADRs, state validation status, and mention any unresolved ambiguity.

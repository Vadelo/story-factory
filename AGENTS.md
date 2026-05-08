# King Context For Codex

This workspace includes Codex-adapted project skills in `.codex/agents/skills/`.

The main use case is `story-factory`: brainstorm, plan, write, continue, and revise stories while saving each work as a dedicated King Context `works` corpus.

## Commands

```bash
.king-context/bin/kctx list
.king-context/bin/kctx list works
.king-context/bin/kctx search "query"
.king-context/bin/kctx search "continuity style" --source works --doc <work-slug>
.king-context/bin/kctx read <doc> <section> --preview
.king-context/bin/kctx index .king-context/data/<file>.json
.king-context/bin/kctx index .king-context/data/works/<work-slug>.json --source works
.king-context/bin/king-research "<topic>" --medium --yes
.king-context/bin/king-scrape <url> --name <slug> --yes
```

Use the local `.codex/agents/skills` copies as the source of truth for project Codex behavior.

On Windows/PowerShell, prefer the `.cmd` wrappers:

```powershell
.\.king-context\bin\kctx.cmd list works
```

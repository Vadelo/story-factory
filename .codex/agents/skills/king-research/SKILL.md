---
name: king-research
description: Build topic-driven King Context research corpora with `.king-context/bin/king-research`. Use when the user asks to research a topic, build a corpus, find sources, create specialist knowledge bases, or gather open-web background for a workflow.
---

# King Research

Run `king-research` to create an indexed corpus from open-web sources.

## Topic And Effort

Extract a concise topic from the user request. If the topic is vague, ask one clarifying question.

Choose effort:

- `--basic`: quick overview, narrow topic, minimal cost.
- `--medium`: default.
- `--high`: detailed, broad, comparative, or important corpus.
- `--extrahigh`: exhaustive/state-of-the-art work. Warn that it can take around 10 minutes and use more API budget.

## Command

```bash
.king-context/bin/king-research "<topic>" --medium --yes
```

Useful flags:

- `--name <slug>`: set a stable corpus slug.
- `--no-auto-index`: keep JSON only when the user explicitly asks.
- `--step <stage>`: resume/debug a failed stage.

Pipeline stages are `generate -> search -> chunk -> enrich -> export`.

## Reporting

After completion, report:

- Corpus slug.
- Section count if shown.
- Example retrieval commands.

Example:

```bash
.king-context/bin/kctx search "character arcs" --doc story-character-arcs
.king-context/bin/kctx topics story-character-arcs
.king-context/bin/kctx list research
```

## Errors

- If `EXA_API_KEY` is missing, tell the user to set it in `.king-context/.env` or `./.env`.
- If LLM provider keys are missing, mention the relevant key from `.king-context/.env.example`.
- If results are empty, suggest broadening or rephrasing the topic.

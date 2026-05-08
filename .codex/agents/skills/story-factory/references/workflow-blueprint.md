# Workflow Blueprint

## Local MVP Pipeline

Input:

```json
{
  "idea": "uma fantasia sombria sobre uma cartografa que descobre mapas vivos",
  "form": "novel outline + chapter 1",
  "language": "pt-BR",
  "audience": "adult fantasy readers",
  "tone": "mysterious, emotional, tense",
  "outputs": ["markdown", "json", "work-corpus"]
}
```

Pipeline:

1. Normalize brief.
2. Ask missing high-impact brainstorming questions.
3. Search permanent craft corpora.
4. Create optional subject-matter corpora.
5. Build story bible.
6. Produce outline or draft.
7. Review genre promise, character, continuity, style, and safety.
8. Export Markdown and JSON.
9. Build/update work corpus.
10. Index with `kctx --source works`.

## Future App Modules

- Brief UI
- Brainstorm engine
- Corpus manager
- Story bible builder
- Draft worker
- Revision worker
- Continuity worker
- Work memory store
- Export layer for JSON, Markdown, API, app preview, or print pipeline

## Data Objects

- `StoryProject`
- `StoryBrief`
- `BrainstormSession`
- `ResearchCorpusSet`
- `StoryBible`
- `Outline`
- `DraftUnit`
- `ContinuityLedger`
- `RevisionReport`
- `WorkMemoryCorpus`

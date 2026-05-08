# Corpus Strategy

Story Factory uses three corpus classes.

For exact folders and naming patterns, read `corpus-map.md`.

## Permanent Research Corpora

These reusable corpora teach the workflow and craft areas:

| Corpus | Purpose |
|---|---|
| `story-factory-workflow` | End-to-end story pipeline from idea to draft, revision, and memory update. |
| `story-brainstorming-intake` | Questionnaires, creative brief refinement, defaults, and user collaboration. |
| `story-structure-plot` | Premise, conflict, stakes, acts, beats, scene architecture, pacing, climax. |
| `story-character-arcs` | Desire, fear, flaw, contradiction, relationships, arc design, voice. |
| `story-worldbuilding-setting` | Setting, social systems, magic/technology rules, culture, geography, history. |
| `story-genre-conventions` | Genre promises and reader expectations across major fiction forms. |
| `story-prose-style-voice` | Prose rhythm, POV, tense, tone, dialogue, narration, sentence texture. |
| `story-continuity-qa` | Canon tracking, timeline, contradictions, callbacks, revision gates. |

On a clean workspace, the skill checks `kctx list research`. Missing corpora are created from `assets/corpora/*.md` with `king-research`.

## Subject-Matter Corpora

Create topic corpora when the story needs researched knowledge:

- historical period;
- real city, culture, profession, law, science, illness, weapon, technology;
- mythological or literary tradition;
- current events or modern institutions;
- high-stakes sensitive representation.

Avoid over-research when the user wants fast ideation or a fully invented world.

Variable request corpora should use this naming pattern:

```text
story-variable-<work-slug>-<topic-slug>
```

They still live in the King Context `research` store because they are created by `king-research`.

## Work Memory Corpora

Each story gets a `works` corpus:

```text
.king-context/data/works/<work-slug>.json
.king-context/works/<work-slug>/
```

Use it for canon, continuity, drafts, decisions, and future continuation. It should be searchable with:

```powershell
.\.king-context\bin\kctx search "timeline betrayal reveal" --doc <work-slug> --source works
```

Do not mix one work's canon into another work's corpus.

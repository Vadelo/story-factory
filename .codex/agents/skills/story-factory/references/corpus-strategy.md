# Corpus Strategy

Story Factory uses separated corpus classes. Do not let process guidance, specialist knowledge, and story canon blur together.

For exact folders and naming patterns, read `corpus-map.md`.

## 1. Permanent Craft Corpora

These reusable corpora teach the workflow and craft areas. They are process guidance, not fictional content.

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

Hard rule: use these to guide planning and review. Do not import their terminology or methods into the story world unless the user explicitly wants metafiction.

## 2. Work Memory Corpora

Each story gets a `works` corpus:

```text
.king-context/data/works/<work-slug>.json
.king-context/works/<work-slug>/
```

Use it for canon, continuity, drafts, decisions, ledgers, and future continuation.

The work memory decides canon. Specialist knowledge can challenge plausibility, but it must not silently overwrite established story facts.

## 3. Specialist Knowledge Corpora

Create these when the story needs researched knowledge:

- historical period, place, culture, religion, language, or community;
- profession, institution, law, medicine, science, craft, weapon, or technology;
- politics, economy, warfare, logistics, trade, agriculture, engineering, or social systems;
- invented systems that need rule design, costs, limits, or consequences;
- genre, market, style, format, or comparator work conventions.

Use `story-knowledge-architect` before creating or activating specialist corpora. It should return a Corpus Plan, Activation Pack, or Research Prompt Pack.

Prefer these names:

```text
story-knowledge-<work-slug>-<topic-slug>
story-style-<work-slug>-<topic-slug>
story-history-<work-slug>-<invention-slug>
story-global-<topic-slug>
```

Use `story-global-*` only for reusable knowledge that is not tied to a single work's canon.

### Featured Invention History Corpora

When a route, arc, or chapter chooses a specific invention or object as a major story beat, create a separate `low` corpus when its history would improve context.

Use:

```text
story-history-<work-slug>-<invention-slug>
```

Purpose:

- origin and early use;
- adoption path;
- cultural meaning;
- social or political impact;
- misconceptions and myths;
- scene hooks and symbolic texture.

Do not put detailed construction, formulas, manufacturing steps, or safety procedures here. Keep those in `story-knowledge-*` technical/bridge corpora.

## 4. Activation Policy

Use the smallest set that answers the current narrative question:

| Mode | Meaning |
|---|---|
| `none` | No specialist corpus; use work memory and craft judgment. |
| `single` | One focused specialist corpus. |
| `bundle` | Several corpora because the task crosses domains. |
| `architect` | Design or create corpora before continuing. |

Depth policy:

| Depth | Use For |
|---|---|
| `low` | texture, vocabulary, daily-life details, narrow scene support |
| `medium` | recurring domains that affect multiple scenes |
| `high` | structural premise, high-risk plausibility, sensitive representation, major consequences |

Avoid over-research when the user wants fast ideation or when the current scene has no concrete knowledge question.

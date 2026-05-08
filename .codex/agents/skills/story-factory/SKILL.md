---
name: story-factory
description: Create fiction and narrative works with King Context. Use when the user wants to brainstorm, plan, write, continue, revise, or maintain a story, novel, saga, screenplay, RPG campaign, webnovel, comic script, children's story, romance, horror, fantasy, sci-fi, thriller, literary fiction, or any narrative work with Markdown and JSON outputs plus a persistent King Context work-memory corpus.
---

# Story Factory

Build stories from a small user idea through a local King Context workflow: brainstorm, specialize knowledge corpora, create a story bible, write Markdown and JSON outputs, then save a work-specific memory corpus under `works`.

This skill is local-first: artifacts live in the workspace, while optional research corpora are created with `king-research` and queried with `kctx`.

## Required Corpora

Permanent research corpora:

- `story-factory-workflow`
- `story-brainstorming-intake`
- `story-structure-plot`
- `story-character-arcs`
- `story-worldbuilding-setting`
- `story-genre-conventions`
- `story-prose-style-voice`
- `story-continuity-qa`

Check:

```powershell
.\.king-context\bin\kctx list research
```

If any core corpus is missing, read `assets/corpora/<corpus-name>.md` and run its recommended `king-research` command. Do this before producing a serious story plan.

Hard rule: do not produce the final story before the permanent corpora exist unless the user explicitly asks for a quick mock without research/corpora.

To create every missing required corpus at once after `.king-context/.env` has `EXA_API_KEY` and `OPENROUTER_API_KEY`, run:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py
```

To preview commands without API calls:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py --dry-run
```

## Workflow

1. **Intake**
   Extract the user's idea, target form, language, audience, genre, tone, length, rating, POV, tense, themes, setting, constraints, and desired output.

2. **Brainstorm**
   Use `references/brainstorming-questionnaire.md`. Ask only the missing high-impact questions. If the user leaves fields blank, propose defaults and label them as suggestions.

3. **Corpus Retrieval**
   Query the permanent corpora before planning:

```powershell
.\.king-context\bin\kctx search "brainstorm genre tone premise questionnaire" --doc story-brainstorming-intake --source research --top 4
.\.king-context\bin\kctx search "plot structure scenes escalation climax" --doc story-structure-plot --source research --top 4
.\.king-context\bin\kctx search "character arc desire flaw conflict" --doc story-character-arcs --source research --top 4
.\.king-context\bin\kctx search "continuity canon timeline memory revision" --doc story-continuity-qa --source research --top 4
```

4. **Optional Subject Corpus**
   Use `king-research` for the user's specific style, type, genre, setting, culture, historical period, profession, technical detail, comparator, or factual requirement. Name these variable corpora with `story-variable-<work-slug>-<topic-slug>`.

5. **Story Bible**
   Create a structured bible: premise, promise, audience, genre contract, themes, characters, relationships, setting, rules, timeline, plot outline, style guide, continuity ledger, open questions.

6. **Draft**
   Write the requested artifact: synopsis, chapter outline, scene list, chapter, full short story, screenplay scene, comic issue, RPG session, or continuation.

7. **Output Formats**
   Produce both:
   - Markdown for human reading and editing.
   - JSON for apps, APIs, future continuation, or indexing.

8. **Work Memory Corpus**
   Save or update `.king-context/data/works/<work-slug>.json` with `source_type: "work"` sections. Then index:

```powershell
.\.king-context\bin\kctx index .king-context\data\works\<work-slug>.json --source works
```

9. **Chapter Memory Enrichment**
   After each created chapter, create a chapter memory packet and append it to the same work corpus:

```powershell
python .codex\agents\skills\story-factory\scripts\append_chapter_memory.py `
  .king-context\data\works\<work-slug>.json `
  output\<work-slug>\chapter-001.memory.json

.\.king-context\bin\kctx index .king-context\data\works\<work-slug>.json --source works
```

Each chapter packet must include the chapter text or excerpt, summary, canon changes, character states, timeline changes, unresolved threads, resolved threads, callbacks, and continuity risks. This is how the work remembers itself from beginning to end.

The intermediate packet can have chapter-friendly fields, but the persisted corpus must always be converted into standard King Context sections with `title`, `path`, `url`, `keywords`, `use_cases`, `tags`, `priority`, `source_type`, and `content`.

Search later:

```powershell
.\.king-context\bin\kctx search "character motive unresolved thread" --doc <work-slug> --source works
.\.king-context\bin\kctx read <work-slug> canon-premise --source works
```

## Work Memory Rules

- Treat the `works` corpus as canon unless the user explicitly retcons it.
- Before continuing an existing work, search its `works` corpus for premise, characters, timeline, unresolved threads, style, and the last produced chapter/scene.
- After every meaningful draft, chapter, scene, or revision, update the work corpus.
- Store one chapter memory packet per chapter. Do not collapse the whole work into a single rolling summary.
- Store contradictions and retcons explicitly; never silently overwrite canon.

## Read As Needed

- `references/corpus-strategy.md`: permanent corpora and research policy.
- `references/corpus-map.md`: exact folder/store/naming pattern for permanent, variable, and work-memory corpora.
- `references/brainstorming-questionnaire.md`: intake questions and suggestion rules.
- `references/workflow-blueprint.md`: full product pipeline.
- `references/work-memory-schema.md`: JSON/Markdown output structure.
- `references/quality-gates.md`: review gates for narrative quality and continuity.

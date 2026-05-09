# Story Factory with King Context

This repository is a practical King Context use case for creating long-form stories with persistent memory, specialist research corpora, and reusable local Codex skills.

The main skill is `story-factory`. It can brainstorm, plan, write, continue, revise, and preserve narrative context by saving each work as a dedicated King Context `works` corpus.

The newest improvement is an autopilot workflow: for serious story requests, Story Factory can infer the pipeline, design or activate specialist knowledge corpora, create a story bible, draft chapters, save Markdown/JSON outputs, append chapter memory, and reindex the work corpus.

## Quick Start

In any AI assistant or agent environment that supports local skills, mention the skill in your prompt with `$story-factory`.

Example:

```text
$story-factory create a webnovel about a modern inventor reincarnated as Crown Prince Hyang in Joseon during King Sejong's reign.
```

More examples:

```text
$story-factory brainstorm a dark fantasy webnovel about a cursed cartographer.
```

```text
$story-factory create chapter 1 of a mystery light novel and save Markdown, JSON, and work memory.
```

```text
$story-factory continue o-principe-das-mil-invencoes with chapter 3 using the existing work corpus.
```

```text
$story-factory revise chapter 2 and update the work memory corpus afterward.
```

When the skill runs correctly, the assistant should:

1. Read the local `story-factory` instructions.
2. Query the permanent craft corpora.
3. Query or create the work-specific corpus.
4. Run a knowledge need check for serious or specialized stories.
5. Use `story-knowledge-architect` when the premise needs history, culture, science, politics, professional realism, genre emulation, or other specialist knowledge.
6. Create or activate only the corpora needed for the current deliverable.
7. Create/update the story bible when needed.
8. Write the requested story output.
9. Save Markdown and JSON files.
10. Append chapter memory to the work corpus.
11. Reindex the work corpus.
12. Review continuity and memory retrieval.

## What This Project Contains

```text
.codex/agents/skills/story-factory/
  SKILL.md
  scripts/
  references/
  assets/corpora/

.codex/agents/skills/story-knowledge-architect/
  SKILL.md
  agents/
  references/

.king-context/data/research/
  story-*.json
  story-knowledge-*.json
  story-history-*.json

.king-context/research/
  story-*/

.king-context/data/works/
  a-margem-que-devora-o-heroi.json
  o-principe-das-mil-invencoes.json

.king-context/works/
  a-margem-que-devora-o-heroi/
  o-principe-das-mil-invencoes/

output/
  a-margem-que-devora-o-heroi/
  o-principe-das-mil-invencoes/

tools/
  build_ollama_research_corpus.py
```

The `.king-context/.env` file is intentionally not committed. Use `.king-context/.env.example` as the template.

## New Improvements

- `story-factory` now acts as a top-level orchestrator instead of only a writing helper.
- Serious requests can run through an inferred pipeline: intake, craft retrieval, knowledge check, corpus planning, research activation, story bible, chapter draft, chapter memory, and indexing.
- `story-knowledge-architect` was added to design minimal specialist corpora and activation packs.
- Specialist corpora now have clear depth levels: `low`, `medium`, and `high`.
- Work memory remains canon, while specialist research stays reference-only until the story adopts it.
- Featured inventions can get separate `story-history-*` corpora, distinct from technical feasibility corpora.
- A local Ollama consolidation helper was added at `tools/build_ollama_research_corpus.py` for generating focused research corpora from discovered chunks.
- A new example work, `o-principe-das-mil-invencoes`, demonstrates historical alternate-fiction, technology uplift, court politics, specialist corpora, story bible creation, and chapter memory.

## How The Context System Works

Story Factory now uses four context layers.

## 1. Permanent Craft Corpora

These live in the King Context `research` store and provide reusable writing-process knowledge:

```text
story-factory-workflow
story-brainstorming-intake
story-structure-plot
story-character-arcs
story-worldbuilding-setting
story-genre-conventions
story-prose-style-voice
story-continuity-qa
```

They cover workflow, brainstorming, plot, characters, worldbuilding, genre, prose style, and continuity.

Hard rule: craft corpora guide the writer. They are not story canon and should not leak into fictional content unless the user explicitly wants metafiction.

## 2. Work Memory Corpus

Each story gets its own dedicated corpus in `works`:

```text
.king-context/data/works/<work-slug>.json
.king-context/works/<work-slug>/
```

The work corpus stores premise, themes, characters, relationships, world rules, timeline, style guide, chapter text, chapter summaries, canon changes, character states, unresolved threads, and continuity risks.

This is what lets an assistant continue a story later without relying only on the current chat history.

## 3. Specialist Knowledge Corpora

Specialist corpora live in the `research` store, but they are not permanent craft corpora and they are not canon. They provide researched support for a specific work, arc, chapter, or domain.

Naming patterns:

```text
story-knowledge-<work-slug>-<topic-slug>
story-style-<work-slug>-<topic-slug>
story-history-<work-slug>-<invention-slug>
story-global-<topic-slug>
```

Use `story-knowledge-architect` to decide whether the current task needs:

```text
none
single
bundle
architect
```

## 4. Temporary Request Corpora

Temporary corpora are useful for one-off experiments or comparator research:

```text
story-temp-<work-slug>-<topic-slug>
```

Promote them to `story-knowledge-*`, `story-style-*`, or `story-global-*` only when they become recurring.

## Included Example Works

### `a-margem-que-devora-o-heroi`

Davi Noh dies and wakes up trapped in the textual margin of a regression light novel/manhwa he once edited. He has no body, no system, and no status screen. His power is editorial: he can alter phrases, recover cut versions, interfere with review comments, and return agency to characters who were flattened by the original hero-centered narrative.

Included chapters:

- `chapter-001-light-novel.md`: Davi wakes in the margin, prevents Yerin from becoming emotional fuel for Kael's heroic entrance, and discovers that Kael can also write review comments in the margin.
- `chapter-002-light-novel.md`: Kael weaponizes review comments, the `resolve conversation` button becomes a real threat, Yerin receives a cut line back, and she escapes toward the Archive Pavilion.

### `o-principe-das-mil-invencoes`

Artur Vale, a modern Nobel-level inventor, dies in an experiment and reincarnates as Yi Hyang, Crown Prince of Joseon and son of King Sejong. He has modern memory and interdisciplinary genius, but no system, no magic, and no industrial base. To transform Joseon, he must navigate preindustrial materials, court politics, Confucian institutions, his fragile body, and a brilliant father-king who both admires and fears the speed of his changes.

Included artifacts:

- `story-bible.md`: premise, knowledge delta, corpus plan, characters, rules, arcs, style, continuity ledger, and open threads.
- `chapter-001.md`: Hyang awakens in Joseon and begins with measurement instead of spectacle.
- `chapter-002.md`: Jang Yeong-sil tests the rain-measurement prototype, court resistance sharpens, and Sejong limits the next step to three instruments in the capital.
- `project.json`: machine-readable project state, corpus plan, bible, chapter summaries, canon changes, and revision history.

Specialist corpora created for this work:

```text
story-knowledge-o-principe-das-mil-invencoes-joseon-sejong-baseline
story-knowledge-o-principe-das-mil-invencoes-preindustrial-engineering-bridges
story-knowledge-o-principe-das-mil-invencoes-court-politics-reform-backlash
story-history-o-principe-das-mil-invencoes-rain-gauge
```

## Useful Commands

On Windows/PowerShell, prefer the `.cmd` wrappers.

List permanent and specialist research corpora:

```powershell
.\.king-context\bin\kctx.cmd list research
```

List story works:

```powershell
.\.king-context\bin\kctx.cmd list works
```

Search a work corpus:

```powershell
.\.king-context\bin\kctx.cmd search "Hyang Sejong rain measurement" --doc o-principe-das-mil-invencoes --source works
```

Read a specific memory section:

```powershell
.\.king-context\bin\kctx.cmd read o-principe-das-mil-invencoes chapter-002-summary --source works
```

Preview full chapter text stored inside the corpus:

```powershell
.\.king-context\bin\kctx.cmd read o-principe-das-mil-invencoes chapter-002-text --source works --preview
```

Search a specialist research corpus:

```powershell
.\.king-context\bin\kctx.cmd search "measurement taxation backlash" --doc story-knowledge-o-principe-das-mil-invencoes-court-politics-reform-backlash --source research
```

## Creating A New Chapter

The expected `story-factory` workflow is:

1. Search permanent craft corpora in `research`.
2. Search the specific work corpus in `works`.
3. Run the knowledge need check.
4. Activate or create specialist corpora only when needed.
5. Write the chapter in Markdown.
6. Create a chapter JSON file.
7. Create a chapter memory packet.
8. Append the packet to the work corpus.
9. Reindex the work corpus.
10. Run a continuity review.

Append chapter memory:

```powershell
python .codex\agents\skills\story-factory\scripts\append_chapter_memory.py `
  .king-context\data\works\o-principe-das-mil-invencoes.json `
  output\o-principe-das-mil-invencoes\chapter-002.memory.json
```

Reindex the work:

```powershell
.\.king-context\bin\kctx.cmd index .king-context\data\works\o-principe-das-mil-invencoes.json --source works
```

Confirm the indexed section count:

```powershell
.\.king-context\bin\kctx.cmd list works
```

Each chapter memory packet adds these 7 standard King Context sections:

```text
chapter-<id>-text
chapter-<id>-summary
chapter-<id>-canon-delta
chapter-<id>-character-states
chapter-<id>-timeline
chapter-<id>-threads
chapter-<id>-continuity
```

## Building Specialist Corpora With Ollama

The permanent corpora can still be created with `king-research`, but this repo also includes a local helper for building focused research corpora from discovered chunks using Ollama:

```powershell
python tools\build_ollama_research_corpus.py `
  --name story-knowledge-o-principe-das-mil-invencoes-joseon-sejong-baseline `
  --chunks-dir .king-context\research\<source-corpus>\chunks `
  --profile joseon-baseline `
  --model qwen3.6:latest
```

Available profiles:

```text
joseon-baseline
preindustrial-engineering
court-politics-reform
featured-invention-history
```

The generated JSON should be indexed into the `research` store:

```powershell
.\.king-context\bin\kctx.cmd index .king-context\data\research\<corpus-name>.json --source research
```

## Rebuilding The Permanent Corpora

The permanent craft corpora are already included, but the skill can rebuild missing corpora when API keys are configured.

Create `.king-context/.env` from `.king-context/.env.example`, then set:

```text
EXA_API_KEY=
OPENROUTER_API_KEY=
RESEARCH_PROVIDER=openrouter
ENRICH_PROVIDER=openrouter
```

Run:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py
```

Preview the commands without API calls:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py --dry-run
```

You can also use local Ollama if OpenRouter is unavailable or rate-limited:

```powershell
$env:RESEARCH_PROVIDER='ollama'
$env:RESEARCH_MODEL='gpt-oss:20b'
$env:ENRICH_PROVIDER='ollama'
$env:ENRICH_MODEL='gpt-oss:20b'
$env:FILTER_PROVIDER='ollama'
$env:FILTER_MODEL='gpt-oss:20b'
```

## Current Test Result

```powershell
.\.king-context\bin\kctx.cmd list research
```

Returns 12 research corpora:

- 8 permanent craft corpora.
- 4 specialist corpora for `o-principe-das-mil-invencoes`.

```powershell
.\.king-context\bin\kctx.cmd list works
```

Returns:

```text
a-margem-que-devora-o-heroi   29 sections
o-principe-das-mil-invencoes  23 sections
```

This confirms that the repository now supports both the original editorial-metafiction example and the newer specialist-research/autopilot example.

## Git Notes

The `.gitignore` keeps these local-only files out of Git:

```text
.env
.king-context/.env
.king-context/core/
.king-context/_temp/
.king-context/_learned/
*.zip
```

The corpora in `.king-context/data`, `.king-context/research`, and `.king-context/works` are intentionally versionable because they are part of the examples.

`.king-context/core/` is local King Context runtime/venv data. The important project assets are the skills, corpora, indexed context, and generated story outputs.

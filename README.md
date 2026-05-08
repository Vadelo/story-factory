# Story Factory with King Context

This repository is a practical King Context use case for creating stories instead of PDFs.

The main skill is `story-factory`. It can brainstorm, plan, write, continue, revise, and preserve long-form narrative context by saving each work as a dedicated King Context `works` corpus.

## Quick Start

In any AI assistant or agent environment that supports local skills, mention the skill in your prompt with `$story-factory`.

Example:

```text
$story-factory use this skill to create an isekai story in light novel style.
```

More examples:

```text
$story-factory brainstorm a dark fantasy webnovel about a cursed cartographer.
```

```text
$story-factory create chapter 1 of a mystery light novel and save Markdown, JSON, and work memory.
```

```text
$story-factory continue a-margem-que-devora-o-heroi with chapter 3 using the existing work corpus.
```

```text
$story-factory revise chapter 2 and update the work memory corpus afterward.
```

When the skill runs correctly, the assistant should:

1. Read the `story-factory` instructions.
2. Query the permanent story-writing corpora.
3. Query or create the work-specific corpus.
4. Ask only the missing high-impact brainstorming questions.
5. Write the requested story output.
6. Save Markdown and JSON files.
7. Append chapter memory to the work corpus.
8. Reindex the work corpus.
9. Review continuity and memory retrieval.

## What This Project Contains

```text
<skills-dir>/story-factory/
  SKILL.md
  scripts/
  references/
  assets/corpora/

.king-context/data/research/
  story-*.json

.king-context/research/
  story-*/

.king-context/data/works/
  a-margem-que-devora-o-heroi.json

.king-context/works/
  a-margem-que-devora-o-heroi/

output/a-margem-que-devora-o-heroi/
  chapter-001-light-novel.md
  chapter-001-light-novel.json
  chapter-001-light-novel.memory.json
  chapter-002-light-novel.md
  chapter-002-light-novel.json
  chapter-002-light-novel.memory.json
  project.json
```

The `.king-context/.env` file is intentionally not committed. Use `.king-context/.env.example` as the template.

## How The Context System Works

`story-factory` uses three context layers.

## 1. Permanent Research Corpora

These live in the King Context `research` store and provide reusable knowledge for story creation:

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

They cover story workflow, brainstorming, plot, characters, worldbuilding, genre, prose style, and continuity.

## 2. Variable Research Corpora

These are created when a specific story needs extra research, such as a historical period, profession, culture, genre niche, technical domain, or factual setting detail.

Recommended naming pattern:

```text
story-variable-<work-slug>-<topic-slug>
```

## 3. Work Memory Corpus

Each story gets its own dedicated corpus in `works`:

```text
.king-context/data/works/<work-slug>.json
.king-context/works/<work-slug>/
```

The work corpus stores:

- premise
- themes
- characters
- relationships
- world rules
- timeline
- style guide
- chapter text
- chapter summaries
- canon changes
- character states
- unresolved threads
- continuity risks

This is what lets an assistant continue a story later without relying only on the current chat history.

## Included Example Work

The included test work is:

```text
a-margem-que-devora-o-heroi
```

English summary:

Davi Noh dies and wakes up trapped in the textual margin of a regression light novel/manhwa he once edited. He has no body, no system, and no status screen. His power is editorial: he can alter phrases, recover cut versions, interfere with review comments, and return agency to characters who were flattened by the original hero-centered narrative.

Included chapters:

- `chapter-001-light-novel.md`: Davi wakes in the margin, prevents Yerin from becoming emotional fuel for Kael's heroic entrance, and discovers that Kael can also write review comments in the margin.
- `chapter-002-light-novel.md`: Kael weaponizes review comments, the `resolve conversation` button becomes a real threat, Yerin receives a cut line back, and she escapes toward the Archive Pavilion.

## Useful Commands

On Windows/PowerShell, prefer the `.cmd` wrappers.

List permanent research corpora:

```powershell
.\.king-context\bin\kctx.cmd list research
```

List story works:

```powershell
.\.king-context\bin\kctx.cmd list works
```

Search the example work corpus:

```powershell
.\.king-context\bin\kctx.cmd search "Yerin Kael resolve conversation" --doc a-margem-que-devora-o-heroi --source works
```

Read a specific memory section:

```powershell
.\.king-context\bin\kctx.cmd read a-margem-que-devora-o-heroi chapter-002-light-novel-summary --source works
```

Preview the full chapter text stored inside the corpus:

```powershell
.\.king-context\bin\kctx.cmd read a-margem-que-devora-o-heroi chapter-002-light-novel-text --source works --preview
```

## Creating A New Chapter

The expected `story-factory` workflow is:

1. Search permanent corpora in `research`.
2. Search the specific work corpus in `works`.
3. Write the chapter in Markdown.
4. Create a chapter JSON file.
5. Create a chapter memory packet.
6. Append the packet to the work corpus.
7. Reindex the work corpus.
8. Run a continuity review.

Append chapter memory:

```powershell
python .codex\agents\skills\story-factory\scripts\append_chapter_memory.py `
  .king-context\data\works\a-margem-que-devora-o-heroi.json `
  output\a-margem-que-devora-o-heroi\chapter-002-light-novel.memory.json
```

Reindex the work:

```powershell
.\.king-context\bin\kctx.cmd index .king-context\data\works\a-margem-que-devora-o-heroi.json --source works
```

Confirm the indexed section count:

```powershell
.\.king-context\bin\kctx.cmd list works
```

In the final test, the example work has `29` indexed sections. Each chapter memory packet adds these 7 standard King Context sections:

```text
chapter-<id>-text
chapter-<id>-summary
chapter-<id>-canon-delta
chapter-<id>-character-states
chapter-<id>-timeline
chapter-<id>-threads
chapter-<id>-continuity
```

## Rebuilding The Permanent Corpora

The permanent corpora are already included, but the skill can rebuild missing corpora when API keys are configured.

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

## What Was Tested

1. Project skills were adapted into a local skill directory for assistant environments that support skills.
2. The `story-factory` skill was created with scripts, references, corpus seeds, and workflow rules.
3. King Context was extended to support a separate `works` store.
4. Eight permanent story-writing corpora were generated.
5. The example work `a-margem-que-devora-o-heroi` was created.
6. Chapter 1 was generated in light novel/webnovel style.
7. Chapter 1 was saved into the work corpus with structured chapter memory.
8. Chapter 2 was generated after retrieving:
   - the work corpus;
   - `story-structure-plot`;
   - `story-character-arcs`;
   - `story-continuity-qa`.
9. Chapter 2 was saved as Markdown, JSON, and a memory packet.
10. The work corpus was enriched and reindexed.
11. `kctx search` and `kctx read` confirmed that chapter 2 is retrievable for future continuation.

## Test Result

```powershell
.\.king-context\bin\kctx.cmd list research
```

Returns 8 permanent research corpora.

```powershell
.\.king-context\bin\kctx.cmd list works
```

Returns:

```text
a-margem-que-devora-o-heroi  29 sections
```

This confirms that the work memory was enriched with chapter 2 and that future continuations can recover story state from King Context instead of depending only on chat history.

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

The corpora in `.king-context/data`, `.king-context/research`, and `.king-context/works` are intentionally versionable because they are part of the example.

`.king-context/core/` is local King Context runtime/venv data. The important project assets are the skills, corpora, indexed context, and generated story outputs.

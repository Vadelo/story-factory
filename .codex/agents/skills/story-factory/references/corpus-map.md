# Corpus Map

Story Factory uses three corpus layers. They must not be confused.

## Layer 1: Permanent Craft Corpora

Purpose: reusable knowledge for creating stories.

Producer: `king-research`.

Raw JSON location:

```text
.king-context/data/research/<corpus-slug>.json
```

Indexed location:

```text
.king-context/research/<corpus-slug>/
```

Store:

```text
research
```

Required permanent corpora:

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

Hard rule: a serious Story Factory run must not create the final story before these corpora exist, unless the user explicitly says to skip research/corpora for a quick mock.

## Layer 2: Variable Request Corpora

Purpose: knowledge specific to the user's requested genre, tone, style, setting, culture, profession, historical period, or narrative reference.

Producer: `king-research`.

Naming pattern:

```text
story-variable-<work-slug>-<topic-slug>
```

Examples:

```text
story-variable-a-margem-light-novel-isekai
story-variable-a-margem-korean-webnovel-structure
story-variable-a-margem-metafiction
```

Raw JSON location:

```text
.king-context/data/research/story-variable-<work-slug>-<topic-slug>.json
```

Indexed location:

```text
.king-context/research/story-variable-<work-slug>-<topic-slug>/
```

Store:

```text
research
```

Create variable corpora when the user's request names a style, genre, culture, period, profession, technical field, or comparator that should guide the story.

## Layer 3: Work Memory Corpus

Purpose: canon and continuity for one specific story.

Producer: Story Factory local scripts after story output.

Raw JSON location:

```text
.king-context/data/works/<work-slug>.json
```

Indexed location:

```text
.king-context/works/<work-slug>/
```

Store:

```text
works
```

This corpus is enriched after every chapter with standard King Context sections:

```text
chapter-001-text
chapter-001-summary
chapter-001-canon-delta
chapter-001-character-states
chapter-001-timeline
chapter-001-threads
chapter-001-continuity
```

Hard rule: all work-memory sections must follow the normal King Context section schema.

## Required Preflight

Before creating a story:

```powershell
.\.king-context\bin\kctx.cmd list research
.\.king-context\bin\kctx.cmd list works
```

If permanent corpora are missing:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py
```

If the user's request needs variable corpora, run `king-research` with the `story-variable-*` naming pattern before drafting.

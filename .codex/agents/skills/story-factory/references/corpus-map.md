# Corpus Map

Story Factory uses four layers. They must not be confused.

## Layer 1: Permanent Craft Corpora

Purpose: reusable process and craft knowledge for creating stories.

Producer: `king-research`.

Store:

```text
research
```

Raw JSON:

```text
.king-context/data/research/<corpus-slug>.json
```

Indexed:

```text
.king-context/research/<corpus-slug>/
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

Hard rule: these corpora guide the writer. They are not story canon and should not leak into the fictional premise unless explicitly requested.

## Layer 2: Work Memory Corpus

Purpose: canon and continuity for one specific story.

Producer: Story Factory local scripts after story output.

Store:

```text
works
```

Raw JSON:

```text
.king-context/data/works/<work-slug>.json
```

Indexed:

```text
.king-context/works/<work-slug>/
```

Typical sections:

```text
canon-premise
canon-characters
canon-world-rules
canon-style
chapter-001-text
chapter-001-summary
chapter-001-canon-delta
chapter-001-character-states
chapter-001-timeline
chapter-001-threads
chapter-001-continuity
```

Hard rule: all work-memory sections must follow the normal King Context section schema.

## Layer 3: Specialist Knowledge Corpora

Purpose: researched knowledge that informs the work but is not canon by itself.

Producer: `story-knowledge-architect` designs the corpus; `king-research` creates it.

Store:

```text
research
```

Naming patterns:

```text
story-knowledge-<work-slug>-<topic-slug>
story-style-<work-slug>-<topic-slug>
story-global-<topic-slug>
```

Examples:

```text
story-knowledge-royal-inventor-joseon-court-politics
story-knowledge-royal-inventor-preindustrial-printing
story-knowledge-royal-inventor-innovation-backlash
story-style-royal-inventor-korean-webnovel-uplift
story-global-preindustrial-metalworking
```

Raw JSON:

```text
.king-context/data/research/story-knowledge-<work-slug>-<topic-slug>.json
```

Indexed:

```text
.king-context/research/story-knowledge-<work-slug>-<topic-slug>/
```

Use specialist corpora through Activation Packs:

```text
none | single | bundle | architect
```

## Layer 4: Temporary Request Corpora

Purpose: short-lived or experimental research for a one-off request, draft experiment, or comparator that may not become part of the work's long-term knowledge architecture.

Producer: `king-research`.

Naming pattern:

```text
story-temp-<work-slug>-<topic-slug>
```

Promote a temporary corpus to `story-knowledge-*`, `story-style-*`, or `story-global-*` only if it becomes recurring.

## Required Preflight

Before creating a serious story:

```powershell
.\.king-context\bin\kctx.cmd list research
.\.king-context\bin\kctx.cmd list works
```

If permanent craft corpora are missing:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py
```

If the request needs specialist knowledge, use `story-knowledge-architect` first. Create new corpora only when it returns `architect` mode or a Research Prompt Pack.

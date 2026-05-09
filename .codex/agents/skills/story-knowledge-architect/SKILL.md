---
name: story-knowledge-architect
description: Design and route knowledge corpora for fiction projects. Use when a story premise, arc, chapter, or revision depends on external or specialized knowledge such as history, culture, professions, science, technology, politics, warfare, medicine, law, religion, invented systems, genre emulation, or source comparators; use to decide which corpora to create, which existing corpora to activate, and whether the needed depth is low, medium, or high.
---

# Story Knowledge Architect

Diagnose what a story needs to know, design minimal research corpora, and produce activation packs for Story Factory. This skill does not write the story; it decides what knowledge should inform the next creative step.

## Core Rule

Use the smallest knowledge set that can answer the current narrative question.

Do not load or recommend corpora because they might be interesting. Every activated corpus must answer a concrete question for the current premise, arc, chapter, or revision.

## Workflow

1. **Understand the task**
   Identify whether the user is creating a new work, planning an arc, writing a chapter, revising continuity, or solving one specialized scene.

2. **Identify promises**
   Extract what the story promises readers: setting, profession, system, genre, culture, technology, politics, history, tone, comparator works, or factual realism.

3. **Run the Narrative Knowledge Delta**
   Decide what knowledge gap exists between the story promise and what the writer must know to execute it. Read `references/narrative-knowledge-delta.md` when the gap is not obvious.

4. **Choose an activation mode**
   Use `none`, `single`, `bundle`, or `architect`. Read `references/activation-routing.md` for the decision rules.

5. **Design or select corpora**
   Prefer existing work and research corpora when they are enough. Propose new corpora only when the missing knowledge will recur, affect plausibility, or support a major promise.

6. **Assign depth**
   Use:
   - `low` for texture, vocabulary, everyday details, and narrow scene support.
   - `medium` for recurring knowledge that affects multiple scenes.
   - `high` only for structural premises, high-risk plausibility, or major plot consequences.

7. **Return one of three outputs**
   - **Corpus Plan**: new corpora to create for a work or arc.
   - **Activation Pack**: existing corpora to use for the immediate task.
   - **Research Prompt Pack**: ready prompts for `king-research`.

## Output Shapes

### Corpus Plan

Use when starting a work or introducing a major new domain.

```json
{
  "work_slug": "<work-slug>",
  "knowledge_delta": ["<delta-type>"],
  "corpora": [
    {
      "name": "story-knowledge-<work-slug>-<topic-slug>",
      "depth": "low|medium|high",
      "class": "baseline|expertise|bridge|consequence|system|style|history-of-object",
      "purpose": "<why this corpus exists>",
      "activate_when": ["<task or scene trigger>"],
      "avoid": "<what this corpus must not do>"
    }
  ]
}
```

### Activation Pack

Use before writing, planning, or revising a specific unit.

```json
{
  "task": "<current task>",
  "mode": "none|single|bundle|architect",
  "use_corpora": [
    {
      "name": "<corpus-name>",
      "source": "works|research",
      "depth": "low|medium|high",
      "reason": "<specific question this answers>"
    }
  ],
  "exclude": [
    {
      "name": "<corpus-name>",
      "reason": "<why it is unnecessary now>"
    }
  ],
  "task_questions": ["<focused question to answer from corpora>"]
}
```

### Research Prompt Pack

Use when new corpora are needed. Read `references/corpus-design-prompts.md` for prompt patterns.

```json
{
  "corpus_name": "story-knowledge-<work-slug>-<topic-slug>",
  "depth": "low|medium|high",
  "king_research_prompt": "<narrative-oriented research prompt>",
  "success_criteria": ["<what useful output must include>"]
}
```

## Naming

Use these names unless the project defines a different map:

```text
story-knowledge-<work-slug>-<topic-slug>
story-style-<work-slug>-<topic-slug>
story-history-<work-slug>-<invention-slug>
story-global-<topic-slug>
```

Use `story-global-*` only for reusable knowledge that is not tied to one work's canon.

## Highlight Invention History

When an outline, arc, or chapter chooses a specific invention or object as a major reveal, reform, prototype, or plot engine, consider a separate `low` corpus for the history of that invention.

Use this when the invention is narratively important enough to shape scenes, metaphors, adoption resistance, public reaction, or institutional consequences. Do not use it for disposable tools mentioned once.

Keep it separate from technical corpora:

- technical corpus: how the thing works, required materials, production constraints, safety, scaling;
- history corpus: why it emerged, who used it, what problem it solved, how adoption spread, what myths or misconceptions surround it, what social changes followed.

Default name:

```text
story-history-<work-slug>-<invention-slug>
```

Default depth: `low`.

Escalate to `medium` only if the invention becomes an arc-long institution, economy, military, or cultural transformation.

Activation examples:

```json
{
  "name": "story-history-o-principe-das-mil-invencoes-rain-gauge",
  "depth": "low",
  "class": "history-of-object",
  "purpose": "Understand the real history, adoption, cultural meaning, and narrative hooks of rain gauges before making Hyang's measurement arc central.",
  "activate_when": ["chapter outline selects rain gauge as featured invention"],
  "avoid": "Do not replace the technical engineering bridge; this corpus is for historical context and story hooks."
}
```

## Guardrails

- Keep craft/process corpora out of the fictional content unless the user explicitly wants metafiction.
- Keep work memory as canon; do not let external research override established canon silently.
- Separate knowledge from consequence: facts say what is plausible, the story decides what changes.
- Separate invention history from technical construction. A history corpus can inspire scenes; a bridge/technical corpus checks feasibility.
- Prefer one strong specialist corpus over several broad corpora for a focused scene.
- Prefer a bundle when the scene's problem sits at an intersection, such as technology plus politics plus materials.
- If a missing corpus would only answer one minor sentence, use general reasoning or a low-depth note instead of creating it.

## Read As Needed

- `references/narrative-knowledge-delta.md`: diagnose types of knowledge gaps.
- `references/activation-routing.md`: choose `none`, `single`, `bundle`, or `architect`.
- `references/corpus-design-prompts.md`: write focused `king-research` prompts.

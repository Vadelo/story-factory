---
name: story-factory
description: Create fiction and narrative works with King Context. Use when the user wants to brainstorm, plan, write, continue, revise, or maintain a story, novel, saga, screenplay, RPG campaign, webnovel, comic script, children's story, romance, horror, fantasy, sci-fi, thriller, literary fiction, or any narrative work with Markdown and JSON outputs plus a persistent King Context work-memory corpus.
---

# Story Factory

Build stories from a small user idea through a local King Context workflow: brainstorm, specialize knowledge corpora, create a story bible, write Markdown and JSON outputs, then save a work-specific memory corpus under `works`.

This skill is local-first: artifacts live in the workspace, while optional knowledge corpora are designed by `story-knowledge-architect`, created with `king-research`, and queried with `kctx`.

## Role

Act as the top-level orchestrator for fiction requests. The user should be able to ask naturally, such as "create a webnovel about an inventor reborn in Joseon", without separately asking for corpus planning, story bible creation, or chapter sequencing.

When the request is complex, infer the right pipeline and call supporting skills or references as needed:

```text
user idea -> intake -> knowledge need check -> corpus plan/activation -> bible -> draft/revision -> work memory
```

Do not require the user to manually prompt each stage unless they explicitly want step-by-step control.

Default completion target: when the user asks to create a story, continue end-to-end until the next meaningful deliverable exists. For a new serious long-form work, that usually means: create required corpus plan, create or activate the essential corpora that unblock drafting, build/update the bible, write chapter 1, create chapter memory, and index the work. Do not stop after the corpus plan unless a real blocker exists.

## Required Corpora

Permanent craft corpora:

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

Hard separation: permanent craft corpora guide the writing process. Do not import their concepts, workflow terms, or methodology into the fictional content unless the user explicitly asks for metafiction about writing, revision, memory, corpora, or similar process material.

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

0. **Request Orchestration**
   Decide whether the user is asking for quick output or a serious project pipeline.

   Use the serious pipeline automatically when the premise includes real history, specialized professions, technical/scientific knowledge, culture-specific setting, politics, law, medicine, warfare, invented systems, or a long-form work.

   Use the quick pipeline only when the user asks for a fast mock, short brainstorm, simple scene, or explicitly says to skip research/corpora.

   For serious projects, do not jump straight to chapter prose if the premise needs a knowledge architecture. First create or propose the required Corpus Plan and Story Bible, then draft when enough grounding exists.

   If tool/API limitations block full research, create the best provisional corpus plan/bible and then draft with clearly marked assumptions. Otherwise, keep going without asking the user to say "continue".

1. **Intake**
   Extract the user's idea, target form, language, audience, genre, tone, length, rating, POV, tense, themes, setting, constraints, and desired output.

2. **Brainstorm**
   Use `references/brainstorming-questionnaire.md`. Ask only the missing high-impact questions. If the user leaves fields blank, propose defaults and label them as suggestions.

3. **Craft Corpus Retrieval**
   Query permanent craft corpora for process guidance before serious planning:

```powershell
.\.king-context\bin\kctx search "brainstorm genre tone premise questionnaire" --doc story-brainstorming-intake --source research --top 4
.\.king-context\bin\kctx search "plot structure scenes escalation climax" --doc story-structure-plot --source research --top 4
.\.king-context\bin\kctx search "character arc desire flaw conflict" --doc story-character-arcs --source research --top 4
.\.king-context\bin\kctx search "continuity canon timeline memory revision" --doc story-continuity-qa --source research --top 4
```

4. **Knowledge Need Check**
   Decide whether the current task needs external or specialized knowledge beyond the work memory and craft guidance.

   Do not activate specialist corpora by default. Use `story-knowledge-architect` only when the premise, arc, chapter, or revision depends on knowledge such as history, culture, profession, science, technology, politics, warfare, medicine, law, religion, invented systems, genre emulation, or source comparators.

   The check must choose one mode:

   - `none`: no specialist corpus needed.
   - `single`: one focused specialist corpus answers the current question.
   - `bundle`: several corpora are needed because the task crosses domains.
   - `architect`: pause to design or create corpora before continuing.

   If the mode is `architect`, use `story-knowledge-architect` directly. The user does not need to ask for it separately.

5. **Specialist Knowledge Corpora**
   When `story-knowledge-architect` returns a Corpus Plan or Research Prompt Pack, create only the recommended corpora. Use low/medium/high depth economically:

   - `low`: texture and narrow scene details.
   - `medium`: recurring knowledge that affects scenes.
   - `high`: structural premise, sensitive representation, or high-risk plausibility.

   Prefer the naming pattern `story-knowledge-<work-slug>-<topic-slug>` for work-specific knowledge and `story-global-<topic-slug>` for reusable knowledge.

   When an outline, arc, or chapter selects a specific invention/object as a major reveal, milestone, or plot engine, ask `story-knowledge-architect` whether to create a separate low-depth history corpus:

   ```text
   story-history-<work-slug>-<invention-slug>
   ```

   Keep this separate from technical corpora. The history corpus supports context, adoption, symbolism, resistance, and story hooks; the technical corpus supports feasibility and construction.

6. **Story Bible**
   Create a structured bible: premise, promise, audience, genre contract, themes, characters, relationships, setting, rules, timeline, plot outline, style guide, continuity ledger, open questions.

7. **Draft**
   Write the requested artifact: synopsis, chapter outline, scene list, chapter, full short story, screenplay scene, comic issue, RPG session, or continuation.

   When the user asks for a story rather than a specific planning artifact, default to writing the next chapter after the required groundwork is done.

   When the user asks for chapter N of an existing work:
   - read the work memory first;
   - identify chapter N-1 and unresolved threads;
   - run Knowledge Need Check for chapter N;
   - create or activate any featured-invention/history corpora needed by the chapter;
   - write chapter N;
   - create chapter memory and index the work.

8. **Output Formats**
   Produce both:
   - Markdown for human reading and editing.
   - JSON for apps, APIs, future continuation, or indexing.

9. **Work Memory Corpus**
   Save or update `.king-context/data/works/<work-slug>.json` with `source_type: "work"` sections. Then index:

```powershell
.\.king-context\bin\kctx index .king-context\data\works\<work-slug>.json --source works
```

10. **Chapter Memory Enrichment**
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

## Knowledge Routing Rules

- Always treat the `works` corpus as canon and specialist knowledge corpora as reference material.
- Use craft corpora for process, not fictional content.
- Ask `story-knowledge-architect` for an Activation Pack before loading multiple specialist corpora.
- Prefer `none` for emotional scenes, style polish, and continuity-only reviews.
- Prefer `single` for one focused domain question.
- Prefer `bundle` only when a scene or arc depends on intersections such as technology plus politics, medicine plus ethics, or magic rules plus economy.
- Prefer `architect` when starting a specialized work, introducing a major new domain, or discovering that no existing corpus can answer a recurring knowledge need.
- For featured inventions, prefer a separate `low` `story-history-*` corpus for historical/cultural context instead of bloating the technical corpus.

## Autopilot Behavior

When the user gives a single high-level story request, produce the next useful artifact instead of asking them to restate the pipeline.

For a serious new work, proceed end-to-end until chapter 1 unless blocked. The default workflow should produce:

- normalized premise and assumptions;
- knowledge delta summary;
- Corpus Plan with low/medium/high depths;
- any Research Prompt Pack needed to create missing corpora;
- initial Story Bible;
- chapter 1;
- chapter memory packet;
- updated/indexed work corpus.

If tools and API keys are available, create/index the needed corpora and continue to the bible/draft. If research tooling is unavailable, create the plan and proceed with clearly marked provisional assumptions.

If the user asks "write chapter 1" for a specialized serious work, do not refuse. Either:

- create a grounded Chapter 1 after running the needed activation/research steps; or
- write a rough provisional Chapter 1 and mark knowledge gaps if research cannot be completed.

If the user asks "continue", infer the next missing deliverable from the work memory and project files. Do not ask which step comes next when the workflow state is clear.

## Read As Needed

- `references/corpus-strategy.md`: permanent corpora and research policy.
- `references/corpus-map.md`: exact folder/store/naming pattern for permanent, variable, and work-memory corpora.
- `references/brainstorming-questionnaire.md`: intake questions and suggestion rules.
- `references/workflow-blueprint.md`: full product pipeline.
- `references/orchestration-autopilot.md`: how to turn one natural story request into the right staged workflow.
- `references/work-memory-schema.md`: JSON/Markdown output structure.
- `references/quality-gates.md`: review gates for narrative quality and continuity.
- Use `story-knowledge-architect` for specialist knowledge corpus design, activation packs, and `king-research` prompt packs.

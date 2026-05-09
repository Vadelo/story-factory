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

0. Select quick or serious pipeline from the user's natural request.
1. Normalize brief.
2. Ask missing high-impact brainstorming questions only when the answer changes direction.
3. Search permanent craft corpora for process guidance.
4. Build or read the work memory corpus if this is an existing work.
5. Run Knowledge Need Check:
   - `none`: continue without specialist corpora.
   - `single`: activate one focused corpus.
   - `bundle`: activate a small set of corpora for intersecting questions.
   - `architect`: use `story-knowledge-architect` to design or create corpora first.
6. Create only the specialist corpora required to unblock the next chapter. Do not wait for the user to say "continue" when the next step is obvious.
7. Build story bible or update it.
8. Produce outline or scene list.
9. If the outline selects a featured invention/object, consider a low `story-history-*` corpus for that item.
10. Produce draft or revision.
11. Create chapter memory for long-form chapter output.
12. Review genre promise, character, continuity, style, and knowledge plausibility.
13. Export Markdown and JSON.
14. Build/update work corpus.
15. Index with `kctx --source works`.

## Knowledge Need Check

Ask this before loading specialist corpora:

```text
Does the current task depend on external or specialized knowledge that the work memory and general writing craft do not answer?
```

Call `story-knowledge-architect` when the answer is yes for history, culture, profession, technology, science, politics, warfare, medicine, law, religion, invented systems, source comparators, or sensitive plausibility.

Do not call it for simple summaries, emotional scene polish, continuity-only review, or quick ideation unless the user asks for research.

## One-Request Orchestration

For a natural request like "create a story about X", do not require the user to ask for each stage.

Infer the next useful workflow:

```text
simple/fast request -> quick pipeline -> output
complex/long-form/specialized request -> serious pipeline -> corpus plan -> bible -> draft
existing work request -> read work memory -> activation pack -> continue/revise
```

If the user asks for a chapter before the knowledge architecture exists, create the architecture first when the premise is serious and specialized. Then draft if enough grounding exists, or clearly mark the draft as provisional.

If the user asks for a story and does not explicitly ask to stop at planning, continue until chapter 1 and memory are produced.

When an outline chooses a specific invention as a chapter centerpiece, insert this lightweight branch:

```text
featured invention chosen -> story-history-<work-slug>-<invention-slug> low corpus -> activation pack -> draft
```

Skip this branch for disposable tools or passing references.

## Activation Examples

```text
Task: revise a dialogue for voice.
Mode: none.
Use: work memory and style guide.
```

```text
Task: write a scene where a prince proposes a printing reform.
Mode: bundle.
Use: work memory, court politics, printing technology, innovation backlash.
```

```text
Task: outline a chapter centered on the rain gauge as Hyang's first public measurement reform.
Mode: single + optional technical pair.
Use: story-history-<work-slug>-rain-gauge for history/context; pair with engineering bridge only if construction details matter.
```

```text
Task: start a new medical thriller.
Mode: architect.
Use: story-knowledge-architect to design professional realism corpora first.
```

## Future App Modules

- Brief UI
- Brainstorm engine
- Corpus manager
- Knowledge architect
- Activation pack selector
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
- `KnowledgeCorpusPlan`
- `KnowledgeActivationPack`
- `ResearchPromptPack`
- `StoryBible`
- `Outline`
- `DraftUnit`
- `ContinuityLedger`
- `RevisionReport`
- `WorkMemoryCorpus`

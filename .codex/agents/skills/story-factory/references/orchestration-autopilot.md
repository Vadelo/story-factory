# Orchestration Autopilot

Use this reference when the user gives one natural story request and expects Story Factory to decide the right workflow.

## Goal

The user should not need to say:

```text
first make a corpus plan, then create research prompts, then create a bible, then write chapter 1
```

Story Factory must infer that sequence when the request needs it.

It must also keep going until the user's likely deliverable exists. For a new serious fiction request, that deliverable is normally chapter 1 plus memory, not just a plan.

## Pipeline Selection

### Quick Pipeline

Use when:

- the user asks for a quick idea, mock, sample, or brainstorm;
- the request is low-risk and does not depend on researched knowledge;
- the user explicitly says to skip research/corpora;
- the output is small and disposable.

Flow:

```text
intake -> light craft guidance -> output -> optional memory
```

### Serious Pipeline

Use when:

- the work is long-form or likely to continue;
- the premise depends on history, culture, profession, science, technology, politics, warfare, law, medicine, religion, or invented systems;
- the user wants a dedicated work memory;
- factual plausibility, continuity, or specialist knowledge affects the premise.

Flow:

```text
intake -> craft retrieval -> knowledge need check -> story-knowledge-architect -> corpus plan/research prompts -> create/activate essential corpora -> bible -> chapter 1 -> chapter memory -> index
```

## Complexity Signals

Trigger the serious pipeline when the request includes signals like:

```text
historical period
real monarch or real place
specialist protagonist
inventor, doctor, lawyer, soldier, engineer, scientist, chef, hacker
political reform
technology uplift
complex magic/cultivation/system
real religion or culture
warfare, economics, law, medicine, diplomacy
webnovel/light novel/novel with chapters
```

## Default Response for Serious New Work

If the user asks for a new serious story, produce:

1. normalized premise;
2. assumptions and questions only if critical;
3. knowledge delta;
4. Corpus Plan;
5. create or activate essential corpora when tools allow it;
6. Story Bible;
7. chapter 1;
8. chapter memory and indexed work corpus.

Stop early only for a real blocker, such as missing permission for paid/network calls, missing API keys, unavailable local model, or a creative decision that changes the project direction.

## When to Ask the User

Ask only when a decision cannot be safely inferred:

- historical accuracy vs alternate history;
- real person portrayal vs fictionalized analogue;
- explicit content/rating;
- whether to use a sensitive culture/religion/community in a stylized way;
- whether to spend API requests creating corpora now when tool use has cost.

Do not ask the user to choose between obvious workflow steps. Choose the workflow and proceed.

## Continue Semantics

When the user says "continue", inspect the work state:

```text
no project -> start serious pipeline
project but no essential corpora -> create next essential corpus
corpora but no bible -> create/update bible
bible but no chapter 1 -> write chapter 1
chapter N exists -> plan/write chapter N+1
chapter exists but no memory -> create memory and index
```

Prefer completing the next missing deliverable over reporting a menu.

## Example

User:

```text
Quero uma webnovel sobre um inventor moderno reencarnado como príncipe Hyang em Joseon, na época do Rei Sejong.
```

Story Factory should infer:

```text
serious pipeline
knowledge architect needed
deltas: transferred-expertise, historical-immersion, speculative-consequence, political-reform
first artifacts: Corpus Plan + Research Prompt Pack + Bible skeleton
then: create essential corpora, write chapter 1, save memory
```

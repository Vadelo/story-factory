# Activation Routing

Use this reference to decide how much knowledge to activate for a specific Story Factory step.

## Modes

### `none`

Use no external specialist corpus.

Choose this when:

- the task is emotional, stylistic, or continuity-only;
- the work memory already answers the question;
- the knowledge would be decorative rather than decisive;
- the user asked for a quick draft or review.

### `single`

Use one focused specialist corpus.

Choose this when:

- the scene has one main knowledge problem;
- a narrow corpus can answer the needed question;
- loading multiple corpora would add noise.

Example: a scene about courtroom etiquette uses one court-procedure corpus plus the work memory.

### `bundle`

Use several corpora together.

Choose this when:

- the scene sits at an intersection of domains;
- a decision has technical plus social or political consequences;
- the chapter needs both baseline and bridge knowledge;
- one corpus alone would miss the cause-and-effect chain.

Example: a printing reform chapter may need paper, metal type, court politics, and education policy.

### `architect`

Pause to design or create corpora before continuing.

Choose this when:

- starting a new work with specialized promises;
- introducing a major arc in a new domain;
- no existing corpus can answer a recurring or high-risk knowledge need;
- the story's premise depends on a knowledge bridge not yet mapped.

## Step-Based Defaults

| Story Step | Default Mode | Notes |
|---|---|---|
| quick idea | none | Use general reasoning unless user asks for research. |
| serious concept | architect | Design corpus plan before bible. |
| story bible | bundle | Use only corpora that shape the premise and constraints. |
| arc planning | bundle | Include consequence corpora when changes ripple. |
| chapter drafting | single or bundle | Use minimal corpora tied to the chapter questions. |
| featured invention chosen | single | Add one `low` history-of-object corpus if the invention is a major reveal, reform, or plot engine. |
| scene polish | none or single | Use style or one specialist corpus only. |
| continuity review | none | Work memory first; add specialist corpus only for factual/plausibility checks. |
| factual review | single or bundle | Activate exactly the domains being checked. |

## Cost Rules

- Prefer `low` depth for texture and narrow details.
- Prefer `medium` for recurring domain knowledge.
- Reserve `high` for structural premise, major plot engine, sensitive representation, or high-risk technical plausibility.
- If more than four corpora seem necessary for one chapter, split the chapter problem into smaller questions.
- If the current task has no concrete question, do not activate specialist corpora yet.
- When a chapter or arc features one standout invention, prefer one separate `low` history corpus for context and hooks instead of bloating the technical corpus.

## Activation Pack Checklist

An activation pack is valid only if each corpus has:

- a specific reason;
- a source (`works` or `research`);
- a depth;
- at least one question it will answer;
- an exclusion list for plausible-but-unneeded corpora when noise is likely.

## Featured Invention Rule

If an invention is selected as a chapter centerpiece, ask:

```text
Will knowing the invention's real history improve adoption conflict, symbolism, public reaction, institutional resistance, or scene texture?
```

If yes, create or activate:

```text
story-history-<work-slug>-<invention-slug>
```

Use it with `low` depth by default. Pair it with a technical corpus only when the scene also needs construction plausibility.

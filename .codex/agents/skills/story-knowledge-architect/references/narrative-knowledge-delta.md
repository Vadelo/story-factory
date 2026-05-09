# Narrative Knowledge Delta

Use this reference when a story needs specialized knowledge but the correct corpus shape is not obvious.

## Principle

Do not ask only "what topic is this story about?" Ask "what gap must be crossed for this premise to work?"

Common gap types:

| Delta | Use When | Corpus Classes |
|---|---|---|
| `transferred-expertise` | A character brings knowledge from one world, time, profession, or life into another. | baseline, expertise, bridge, consequence |
| `historical-immersion` | The story happens in a real period without a modern expert changing it. | baseline, culture, daily-life, politics |
| `professional-realism` | The story depends on a job, institution, craft, or technical routine. | expertise, workflow, ethics, vocabulary |
| `invented-system` | Magic, cultivation, psychic powers, fictional science, game systems, or social rules drive the plot. | system, limits, costs, consequences |
| `hidden-world` | A secret society, supernatural layer, conspiracy, or underworld coexists with normal reality. | baseline, concealment, institutions, genre |
| `speculative-consequence` | The premise asks "what if this technology/event/rule existed?" | baseline, change-vector, consequence |
| `cultural-authenticity` | The story uses a culture, religion, language, place, or community the writer must handle carefully. | culture, daily-life, values, representation |
| `genre-emulation` | The work wants to feel like a genre, format, market, or comparator. | style, structure, reader-promises |
| `featured-object-history` | A specific invention, tool, text, medicine, weapon, food, machine, or craft process becomes a major story beat. | history-of-object, consequence, style |

## Corpus Classes

- `baseline`: what exists before the story changes anything.
- `expertise`: what a character, profession, or institution knows.
- `bridge`: how knowledge, tools, resources, or rules can be adapted.
- `consequence`: what changes socially, politically, economically, emotionally, or militarily.
- `system`: internal rules, limits, costs, loopholes, and failure modes.
- `style`: voice, pacing, scene grammar, genre contracts, and comparator texture.
- `daily-life`: food, clothing, objects, manners, spaces, travel, money, routines.
- `history-of-object`: origin, adoption, cultural meaning, misconceptions, historical examples, and story hooks for a highlighted invention or object.

## Diagnostic Questions

Ask only what matters for the task:

1. What does the premise promise that ordinary story reasoning cannot safely fill?
2. Is the missing knowledge about the world, the character's expertise, a bridge between them, or consequences?
3. Will this knowledge recur across the work, or is it a one-scene detail?
4. Would getting this wrong break plausibility, representation, plot logic, or reader trust?
5. Is the knowledge needed now, or can it be created later when the chapter reaches that problem?

## Example Mappings

Modern engineer reborn in Joseon:

```text
deltas: transferred-expertise, historical-immersion, speculative-consequence
baseline: Joseon court, materials, institutions
expertise: practical modern engineering and scientific method
bridge: preindustrial manufacturing paths
consequence: political backlash and reform pressure
```

Hospital romance:

```text
deltas: professional-realism, cultural-authenticity
expertise: medical hierarchy and hospital workflow
ethics: patient privacy and consent
style: romantic pacing without turning scenes into protocol manuals
```

Magic academy with strict rules:

```text
deltas: invented-system, genre-emulation
system: costs, limits, pedagogy, failure modes
consequence: class, economy, warfare, religion
style: academy progression and rivalry scenes
```

Rain gauge as first Joseon measurement reform:

```text
deltas: featured-object-history, speculative-consequence
history-of-object: why rain gauges matter, earlier/later adoption, measurement culture
bridge: what materials and workshop steps make a plausible prototype
consequence: taxation, agriculture, flood management, royal authority
```

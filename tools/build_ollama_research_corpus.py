import argparse
import json
import re
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


JOSEON_BASELINE_SECTIONS = [
    {
        "path": "sejong-statecraft-baseline",
        "title": "Sejong Statecraft Baseline",
        "keywords": ["Sejong", "Joseon", "statecraft", "governance", "court"],
        "tags": ["history", "governance", "baseline"],
        "priority": 10,
        "query_terms": [
            "statecraft", "administration", "governance", "Confucian",
            "king", "Sejong", "policy", "court", "bureaucracy",
        ],
        "focus": (
            "Sejong's statecraft, royal authority, bureaucracy, Confucian "
            "governance, and constraints useful for court-politics fiction."
        ),
    },
    {
        "path": "institutions-jiphyeonjeon-gyeongyeon",
        "title": "Institutions: Jiphyeonjeon, Gyeongyeon, and Scholarly Government",
        "keywords": ["Jiphyeonjeon", "Gyeongyeon", "Hall of Worthies", "scholars"],
        "tags": ["institutions", "scholar-officials"],
        "priority": 9,
        "query_terms": [
            "Jiphyeonjeon", "Hall of Worthies", "Gyeongyeon", "royal lecture",
            "scholars", "research", "classics", "documents",
        ],
        "focus": (
            "scholarly institutions, research culture, royal lectures, state "
            "documents, and how a prince inventor could interact with them."
        ),
    },
    {
        "path": "ideology-religion-resistance",
        "title": "Ideology, Religion, and Reform Resistance",
        "keywords": ["Neo-Confucianism", "Buddhism", "reform", "resistance"],
        "tags": ["ideology", "conflict"],
        "priority": 9,
        "query_terms": [
            "Buddhism", "Confucianism", "Neo-Confucian", "opponents",
            "criticism", "reform", "ideology", "religion", "politics",
        ],
        "focus": (
            "ideological tensions, Buddhist/Confucian policy, scholar-official "
            "objections, and plausible reasons ministers resist rapid reforms."
        ),
    },
    {
        "path": "science-technology-measurement",
        "title": "Science, Technology, and Measurement Baseline",
        "keywords": ["technology", "astronomy", "rain gauge", "measurement"],
        "tags": ["technology", "science"],
        "priority": 10,
        "query_terms": [
            "science", "technology", "astronomy", "meteorology", "calendar",
            "water clock", "rain gauge", "measurement", "Jang Yeong-sil",
            "Yi Hyang",
        ],
        "focus": (
            "Sejong-era technology baseline, measurement instruments, astronomy, "
            "meteorology, workshops, and plausible starting points for uplift."
        ),
    },
    {
        "path": "society-status-daily-constraints",
        "title": "Society, Status, and Daily Constraints",
        "keywords": ["yangban", "social hierarchy", "Joseon society", "daily life"],
        "tags": ["society", "daily-life"],
        "priority": 8,
        "query_terms": [
            "society", "social", "yangban", "status", "class", "daily",
            "hierarchy", "literati", "officials", "commoners",
        ],
        "focus": (
            "social hierarchy, yangban/literati culture, status constraints, "
            "daily-life texture, and who gains or loses from new knowledge."
        ),
    },
]


PREINDUSTRIAL_ENGINEERING_SECTIONS = [
    {
        "path": "knowledge-bridge-principles",
        "title": "Knowledge Bridge Principles",
        "keywords": ["technology uplift", "preindustrial engineering", "constraints", "adaptation"],
        "tags": ["engineering", "bridge", "constraints"],
        "priority": 10,
        "query_terms": [
            "preindustrial", "industrial", "technology", "invention", "innovation",
            "tools", "materials", "manufacturing", "craft", "workshop",
        ],
        "focus": (
            "general principles for translating modern scientific and engineering "
            "knowledge into preindustrial tools, materials, labor, and institutions."
        ),
    },
    {
        "path": "materials-metallurgy-tools",
        "title": "Materials, Metallurgy, and Tooling Constraints",
        "keywords": ["metallurgy", "iron", "steel", "tools", "furnaces", "charcoal"],
        "tags": ["materials", "metallurgy", "tooling"],
        "priority": 10,
        "query_terms": [
            "metallurgy", "iron", "steel", "furnace", "charcoal", "casting",
            "forging", "tools", "lathe", "drill", "workshop", "alloy",
        ],
        "focus": (
            "metalworking, heat, furnaces, charcoal, casting, forging, tooling, "
            "measurement, and what a Joseon workshop could plausibly improve first."
        ),
    },
    {
        "path": "measurement-standardization-quality-control",
        "title": "Measurement, Standardization, and Quality Control",
        "keywords": ["measurement", "standardization", "quality control", "metrology"],
        "tags": ["measurement", "standardization"],
        "priority": 10,
        "query_terms": [
            "measurement", "standardization", "metrology", "precision", "quality",
            "calibration", "weights", "measures", "repeatability", "records",
        ],
        "focus": (
            "why measurement, repeatability, records, standards, and quality control "
            "must precede spectacular inventions in a preindustrial uplift story."
        ),
    },
    {
        "path": "power-machines-workshop-scaling",
        "title": "Power, Machines, Workshops, and Scaling",
        "keywords": ["water power", "wind power", "machines", "workshops", "scaling"],
        "tags": ["machines", "production", "scaling"],
        "priority": 9,
        "query_terms": [
            "water power", "windmill", "watermill", "gear", "machine", "pump",
            "workshop", "production", "scale", "labor", "mechanical",
        ],
        "focus": (
            "available power sources, simple machines, workshop organization, "
            "production scaling, labor training, and bottlenecks between prototype and adoption."
        ),
    },
    {
        "path": "chemistry-agriculture-medicine-limits",
        "title": "Chemistry, Agriculture, Medicine, and Safety Limits",
        "keywords": ["chemistry", "agriculture", "medicine", "safety", "public health"],
        "tags": ["chemistry", "agriculture", "medicine"],
        "priority": 8,
        "query_terms": [
            "chemistry", "soap", "lime", "fertilizer", "agriculture", "irrigation",
            "medicine", "public health", "sanitation", "distillation", "safety",
        ],
        "focus": (
            "low-to-medium tech improvements in chemistry, agriculture, medicine, "
            "sanitation, and safety that can create story progress without impossible industrial leaps."
        ),
    },
]


COURT_POLITICS_REFORM_SECTIONS = [
    {
        "path": "court-power-map",
        "title": "Court Power Map and Institutional Friction",
        "keywords": ["Joseon court", "bureaucracy", "royal authority", "ministers"],
        "tags": ["politics", "institutions"],
        "priority": 10,
        "query_terms": [
            "court", "bureaucracy", "ministers", "officials", "king", "royal",
            "authority", "government", "administration", "Joseon", "Choson",
            "State Council", "Six Ministries",
        ],
        "focus": (
            "court power structure, institutional checks, ministerial authority, "
            "and friction between royal initiative and scholar-official governance."
        ),
    },
    {
        "path": "confucian-arguments-against-reform",
        "title": "Confucian Arguments Against Rapid Reform",
        "keywords": ["Confucianism", "reform resistance", "orthodoxy", "stability"],
        "tags": ["ideology", "resistance"],
        "priority": 10,
        "query_terms": [
            "Confucian", "Neo-Confucian", "orthodoxy", "ritual", "classics",
            "remonstrance", "stability", "tradition", "moral", "propriety",
            "Buddhism", "ideology",
        ],
        "focus": (
            "plausible ideological, moral, ritual, and statecraft arguments that "
            "conservative ministers can use against Hyang's reforms."
        ),
    },
    {
        "path": "knowledge-monopoly-education-documents",
        "title": "Knowledge Monopoly, Education, and State Documents",
        "keywords": ["education", "documents", "Hall of Worthies", "literati", "knowledge"],
        "tags": ["knowledge", "education"],
        "priority": 9,
        "query_terms": [
            "education", "documents", "records", "Hall of Worthies", "Jiphyeonjeon",
            "Gyeongyeon", "literati", "examination", "classics", "scholars",
            "printing", "Hangul",
        ],
        "focus": (
            "who controls knowledge, records, education, interpretation, and state "
            "documents, plus how new technical knowledge threatens literati status."
        ),
    },
    {
        "path": "tax-labor-measurement-backlash",
        "title": "Tax, Labor, Measurement, and Administrative Backlash",
        "keywords": ["tax", "labor", "measurement", "land", "administration"],
        "tags": ["taxation", "labor", "measurement"],
        "priority": 9,
        "query_terms": [
            "tax", "taxation", "land", "labor", "corvee", "tribute", "measurement",
            "weights", "measures", "administration", "survey", "grain",
        ],
        "focus": (
            "how measurement, standardization, taxation, labor obligations, and "
            "administrative records create winners and losers around reforms."
        ),
    },
    {
        "path": "antagonist-design-hooks",
        "title": "Antagonist Design Hooks for Reform Backlash",
        "keywords": ["antagonist", "political conflict", "court intrigue", "reform"],
        "tags": ["story-hooks", "antagonists"],
        "priority": 8,
        "query_terms": [
            "opposition", "criticism", "remonstrance", "censors", "officials",
            "faction", "purge", "court debate", "policy", "king", "minister",
        ],
        "focus": (
            "turn historical court resistance patterns into nuanced antagonists, "
            "debate scenes, traps, tests, compromises, and reform consequences."
        ),
    },
]


FEATURED_INVENTION_HISTORY_SECTIONS = [
    {
        "path": "origin-and-early-use",
        "title": "Origin and Early Use",
        "keywords": ["origin", "early use", "invention history", "adoption"],
        "tags": ["history", "origin"],
        "priority": 10,
        "query_terms": [
            "origin", "invented", "first", "early", "history", "ancient",
            "medieval", "use", "adoption", "introduced",
        ],
        "focus": (
            "origin, early uses, adoption path, and named historical examples of the featured invention."
        ),
    },
    {
        "path": "problem-solved-and-users",
        "title": "Problem Solved and Early Users",
        "keywords": ["problem", "users", "administration", "agriculture"],
        "tags": ["use", "society"],
        "priority": 9,
        "query_terms": [
            "problem", "measure", "agriculture", "farming", "tax", "flood",
            "drought", "weather", "administration", "official", "farmer",
        ],
        "focus": (
            "what practical problem the invention solved, who used it, and why institutions cared."
        ),
    },
    {
        "path": "cultural-and-political-meaning",
        "title": "Cultural and Political Meaning",
        "keywords": ["culture", "politics", "authority", "symbolism"],
        "tags": ["culture", "politics"],
        "priority": 8,
        "query_terms": [
            "culture", "political", "authority", "king", "state", "symbol",
            "ritual", "legitimacy", "public", "official",
        ],
        "focus": (
            "symbolic, cultural, administrative, or political meaning that can be dramatized."
        ),
    },
    {
        "path": "misconceptions-and-anachronism-risks",
        "title": "Misconceptions and Anachronism Risks",
        "keywords": ["misconceptions", "anachronism", "risks", "accuracy"],
        "tags": ["risks", "accuracy"],
        "priority": 8,
        "query_terms": [
            "misconception", "myth", "anachronism", "accuracy", "before",
            "after", "Europe", "China", "Korea", "wrong",
        ],
        "focus": (
            "common misconceptions, chronology traps, claims to avoid, and how to keep the invention grounded."
        ),
    },
    {
        "path": "story-hooks",
        "title": "Story Hooks",
        "keywords": ["story hooks", "scene ideas", "conflict", "adoption"],
        "tags": ["story-hooks"],
        "priority": 9,
        "query_terms": [
            "impact", "adoption", "resistance", "official", "records", "measure",
            "data", "policy", "agriculture", "tax", "weather",
        ],
        "focus": (
            "scene hooks, conflicts, adoption beats, metaphors, public reactions, and emotional uses."
        ),
    },
]


PROFILES = {
    "joseon-baseline": {
        "display_name": "O Principe das Mil Invencoes - Joseon Sejong Baseline",
        "sections": JOSEON_BASELINE_SECTIONS,
    },
    "preindustrial-engineering": {
        "display_name": "O Principe das Mil Invencoes - Preindustrial Engineering Bridges",
        "sections": PREINDUSTRIAL_ENGINEERING_SECTIONS,
    },
    "court-politics-reform": {
        "display_name": "O Principe das Mil Invencoes - Court Politics Reform Backlash",
        "sections": COURT_POLITICS_REFORM_SECTIONS,
    },
    "featured-invention-history": {
        "display_name": "O Principe das Mil Invencoes - Featured Invention History",
        "sections": FEATURED_INVENTION_HISTORY_SECTIONS,
    },
}


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "section"


def strip_thinking(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"(?is)^thinking\.\.\..*?\.\.\.done thinking\.", "", text).strip()
    return text.strip()


def load_chunks(chunks_dir: Path) -> list[dict]:
    chunks = []
    for path in sorted(chunks_dir.glob("*.json")):
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for item in items:
            content = (item.get("content") or "").strip()
            if not content:
                continue
            chunks.append({
                "title": item.get("title") or path.stem,
                "url": item.get("source_url") or "",
                "content": content,
            })
    return chunks


def score_chunk(chunk: dict, terms: list[str]) -> int:
    haystack = f"{chunk['title']}\n{chunk['content']}".lower()
    score = 0
    for term in terms:
        score += haystack.count(term.lower())
    return score


def select_context(chunks: list[dict], terms: list[str], max_chars: int) -> tuple[str, list[str]]:
    ranked = sorted(chunks, key=lambda c: score_chunk(c, terms), reverse=True)
    selected = []
    sources = []
    total = 0
    for chunk in ranked:
        score = score_chunk(chunk, terms)
        if score <= 0 and selected:
            break
        excerpt = chunk["content"][:1800].strip()
        block = f"TITLE: {chunk['title']}\nURL: {chunk['url']}\nEXCERPT:\n{excerpt}\n"
        if total + len(block) > max_chars:
            continue
        selected.append(block)
        if chunk["url"] and chunk["url"] not in sources:
            sources.append(chunk["url"])
        total += len(block)
        if len(selected) >= 8:
            break
    return "\n---\n".join(selected), sources


def ollama_chat(model: str, prompt: str, timeout: int) -> str:
    payload = {
        "model": model,
        "stream": False,
        "think": False,
        "messages": [
            {
                "role": "system",
                "content": (
                    "/no_think\n"
                    "You synthesize research notes for fiction planning. "
                    "Do not invent facts beyond the excerpts. Write in pt-BR. "
                    "Return concise Markdown only. Do not include reasoning, "
                    "thinking traces, or analysis."
                ),
            },
            {"role": "user", "content": "/no_think\n" + prompt},
        ],
        "options": {
            "temperature": 0.2,
            "num_predict": 900,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "http://localhost:11434/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        raw = json.loads(response.read().decode("utf-8"))
    return strip_thinking(raw.get("message", {}).get("content", ""))


def build_section(model: str, spec: dict, chunks: list[dict], timeout: int, corpus_name: str) -> dict:
    context, sources = select_context(chunks, spec["query_terms"], max_chars=11000)
    prompt = f"""\
Corpus: {corpus_name}
Section focus: {spec['focus']}

Use the excerpts below to create a writer-facing research section for the story "O Principe das Mil Invencoes".

Required structure:
## Key Facts
- 5-9 bullets grounded in the excerpts.

## Narrative Uses
- 5-9 bullets about how this can create scenes, conflicts, constraints, or character decisions.

## Anachronism Risks
- 3-6 bullets about what not to overstate or modernize.

## Story Hooks
- 3-6 concrete hooks for Hyang, Sejong, ministers, scholars, artisans, or court institutions.

Excerpts:
{context}
"""
    content = ollama_chat(model, prompt, timeout)
    source_note = "\n\n## Source URLs Used\n" + "\n".join(f"- {url}" for url in sources[:10])
    return {
        "title": spec["title"],
        "path": spec["path"],
        "url": f"local://research/{corpus_name}#{spec['path']}",
        "keywords": spec["keywords"],
        "use_cases": [
            f"Use when planning {spec['focus']}",
            "Use when drafting chapters that need historically grounded constraints",
            "Use when checking plausibility before turning research into canon",
        ],
        "tags": spec["tags"],
        "priority": spec["priority"],
        "source_type": "research",
        "content": content + source_note,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--chunks-dir", required=True)
    parser.add_argument("--model", default="qwen3.6:latest")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="joseon-baseline")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()

    chunks = load_chunks(Path(args.chunks_dir))
    if not chunks:
        raise SystemExit("No chunks found")

    profile = PROFILES[args.profile]
    display_name = profile["display_name"]
    if args.profile == "featured-invention-history":
        topic_label = args.name.split("-")[-1].replace("-", " ").title()
        display_name = f"O Principe das Mil Invencoes - History of {topic_label}"
    sections = [
        build_section(args.model, spec, chunks, args.timeout, args.name)
        for spec in profile["sections"]
    ]

    corpus = {
        "name": args.name,
        "display_name": display_name,
        "version": "v1-local-ollama",
        "base_url": f"local://research/{args.name}",
        "sections": sections,
    }

    out = ROOT / ".king-context" / "data" / "research" / f"{args.name}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(corpus, indent=2, ensure_ascii=False), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

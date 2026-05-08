# Story Factory com King Context

Este projeto é um exemplo prático de uso do **King Context** com uma skill do Codex chamada `story-factory`.

A ideia é simples: em vez de gerar PDFs, o fluxo gera histórias em Markdown/JSON e mantém memória longa da obra dentro de um corpus próprio. Assim, cada capítulo novo pode consultar o que já aconteceu, quais regras foram criadas, quais personagens mudaram e quais pontas ainda estão abertas.

## O Que Fica No Projeto

```text
.codex/agents/skills/story-factory/
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

O arquivo `.king-context/.env` fica fora do Git. Use `.king-context/.env.example` como base.

## Como Funciona

O `story-factory` usa três camadas de contexto.

1. **Corpora permanentes de criação**

Ficam em `research` e servem como base geral para qualquer história:

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

2. **Corpora variáveis**

São criados quando a história precisa de pesquisa específica, como um período histórico, profissão, cultura, subgênero ou referência técnica.

Padrão de nome:

```text
story-variable-<work-slug>-<topic-slug>
```

3. **Corpus da obra**

Cada obra tem um corpus próprio em `works`:

```text
.king-context/data/works/<work-slug>.json
.king-context/works/<work-slug>/
```

Esse corpus guarda premissa, temas, personagens, regras, linha do tempo, estilo, capítulos, resumos, mudanças de cânone e riscos de continuidade.

## Exemplo Criado

A obra de teste é:

```text
a-margem-que-devora-o-heroi
```

Premissa: Davi Noh morre e acorda preso na margem textual de uma light novel/manhwa de regressão que ele ajudou a revisar. Ele não tem corpo, sistema ou status. Seu poder é editar frases, recuperar versões cortadas e disputar a agência narrativa com Kael, o herói regressor original.

Capítulos incluídos:

- `chapter-001-light-novel.md`: Davi acorda na margem, salva Yerin de virar gatilho emocional da entrada de Kael e descobre que Kael também consegue escrever comentários.
- `chapter-002-light-novel.md`: Kael usa comentários para bloquear Davi, o botão `resolver conversa` vira ameaça real, Yerin recebe uma fala cortada de volta e foge para o Pavilhão dos Arquivos.

## Passo A Passo Para Usar

No Windows/PowerShell, use os wrappers `.cmd`.

Listar os corpora permanentes:

```powershell
.\.king-context\bin\kctx.cmd list research
```

Listar obras:

```powershell
.\.king-context\bin\kctx.cmd list works
```

Buscar contexto da obra:

```powershell
.\.king-context\bin\kctx.cmd search "Yerin Kael resolver conversa" --doc a-margem-que-devora-o-heroi --source works
```

Ler uma seção específica:

```powershell
.\.king-context\bin\kctx.cmd read a-margem-que-devora-o-heroi chapter-002-light-novel-summary --source works
```

Verificar o texto completo de um capítulo no corpus:

```powershell
.\.king-context\bin\kctx.cmd read a-margem-que-devora-o-heroi chapter-002-light-novel-text --source works --preview
```

## Criando Um Novo Capítulo

O fluxo esperado da skill é:

1. Consultar os corpora permanentes em `research`.
2. Consultar o corpus da obra em `works`.
3. Escrever o capítulo em Markdown.
4. Criar um JSON do capítulo.
5. Criar um pacote de memória do capítulo.
6. Anexar esse pacote ao corpus da obra.
7. Reindexar a obra.
8. Fazer uma revisão de continuidade.

Exemplo para anexar a memória de um capítulo:

```powershell
python .codex\agents\skills\story-factory\scripts\append_chapter_memory.py `
  .king-context\data\works\a-margem-que-devora-o-heroi.json `
  output\a-margem-que-devora-o-heroi\chapter-002-light-novel.memory.json
```

Depois reindexe:

```powershell
.\.king-context\bin\kctx.cmd index .king-context\data\works\a-margem-que-devora-o-heroi.json --source works
```

Confirme a quantidade de seções:

```powershell
.\.king-context\bin\kctx.cmd list works
```

No teste final, a obra ficou com `29` seções. Cada capítulo adiciona 7 seções de memória:

```text
chapter-<id>-text
chapter-<id>-summary
chapter-<id>-canon-delta
chapter-<id>-character-states
chapter-<id>-timeline
chapter-<id>-threads
chapter-<id>-continuity
```

## Recriando Os Corpora Permanentes

Os corpora já estão incluídos neste projeto, mas a skill também sabe recriá-los quando necessário.

Configure `.king-context/.env` com:

```text
EXA_API_KEY=
OPENROUTER_API_KEY=
RESEARCH_PROVIDER=openrouter
ENRICH_PROVIDER=openrouter
```

Depois rode:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py
```

Para ver o que seria executado sem chamar APIs:

```powershell
python .codex\agents\skills\story-factory\scripts\bootstrap_research_corpora.py --dry-run
```

Também é possível usar Ollama local quando o OpenRouter estiver sem limite:

```powershell
$env:RESEARCH_PROVIDER='ollama'
$env:RESEARCH_MODEL='gpt-oss:20b'
$env:ENRICH_PROVIDER='ollama'
$env:ENRICH_MODEL='gpt-oss:20b'
$env:FILTER_PROVIDER='ollama'
$env:FILTER_MODEL='gpt-oss:20b'
```

## O Que Foi Testado

1. As skills originais foram adaptadas para `.codex/agents/skills`.
2. A skill `story-factory` foi criada com scripts, referências, seeds de corpora e workflow.
3. O King Context foi ajustado para suportar o store `works`, separado de `research`.
4. Foram criados 8 corpora permanentes de criação de histórias.
5. Foi criada a obra `a-margem-que-devora-o-heroi`.
6. O capítulo 1 foi gerado em estilo light novel/webnovel.
7. O capítulo 1 foi salvo no corpus da obra com memória estruturada.
8. O capítulo 2 foi gerado consultando:
   - corpus da obra;
   - `story-structure-plot`;
   - `story-character-arcs`;
   - `story-continuity-qa`.
9. O capítulo 2 foi salvo em Markdown, JSON e pacote de memória.
10. O corpus da obra foi enriquecido e reindexado.
11. A busca e leitura com `kctx` confirmaram que o capítulo 2 ficou recuperável.

## Resultado Do Teste

```powershell
.\.king-context\bin\kctx.cmd list research
```

Retorna 8 corpora permanentes.

```powershell
.\.king-context\bin\kctx.cmd list works
```

Retorna:

```text
a-margem-que-devora-o-heroi  29 sections
```

Isso confirma que o contexto da obra foi enriquecido com o capítulo 2 e que futuras continuações podem recuperar o estado da história sem depender apenas do chat atual.

## Observações Para Git

O `.gitignore` mantém fora:

```text
.env
.king-context/.env
.king-context/core/
.king-context/_temp/
.king-context/_learned/
*.zip
```

Os corpora em `.king-context/data`, `.king-context/research` e `.king-context/works` ficam versionáveis de propósito, porque são parte do exemplo.

O diretório `.king-context/core/` é runtime local do King Context e pode ser reinstalado ou copiado conforme o ambiente. Os dados importantes do exemplo são os corpora, a skill e os outputs.

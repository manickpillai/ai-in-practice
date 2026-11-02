# docs-helper

A MkDocs site, an auto-generated `llms.txt` index, and a AI skill that answers questions from the docs with links to the source sections.

## Background: the two building blocks

**MkDocs** is a static site generator for documentation. You write plain markdown files in a `docs/` folder, list them in a `mkdocs.yml` config, and MkDocs turns them into a searchable, navigable website (here with the Material theme). It's built for humans: people browse the navigation, read pages and use the search box. `uv run mkdocs serve` previews it locally.

**`llms.txt`** is the same idea for AI. It's a plain-text, markdown-formatted file at a site's root (`/llms.txt`) that gives an LLM a compact map of the site: a title, a short summary and a list of links to the important pages. It is the AI-friendly counterpart to `sitemap.xml`. Instead of making a model read every page or parse HTML, it can read this one small file, decide which links matter, and fetch only those. It's a community convention (proposed at [llmstxt.org](https://llmstxt.org)), not an enforced standard.

| | Audience | Format | Used for |
| --- | --- | --- | --- |
| MkDocs site | People | Rendered HTML pages | Browsing and reading |
| `llms.txt` | LLMs and agents | One markdown index | Finding the right page fast |

This project builds both from the same markdown files, so they never drift apart.

![The MkDocs site rendered with the Material theme](images/docs_helper_mkdocs_site.png)

## 1. Business problem

Docs have two kinds of readers: people who browse and read in full, and people with a specific question who want the answer now. A docs site serves the first group well and the second poorly. Missing or outdated docs also go unnoticed.

`docs-helper` serves both from one set of markdown files:

- **Readers** get the MkDocs site.
- **Quick-answer users** ask the skill in plain language and get a short answer with links to the exact sections.
- **Maintainers** get a list of documentation gaps. If the docs don't cover a question, the skill says so instead of answering from general knowledge. Add the missing section and the next person gets the answer.

## 2. The data

The data is a set of markdown files in [`docs/`](docs/): generic testing guides (overview, unit, integration, test data) and a FAQ (general, troubleshooting). Each page has one h1, several h2 sections and some h3 subsections.

Reading every page for every question is slow and wasteful, so the pages are summarised into an index first. The same markdown files feed both audiences:

```mermaid
flowchart LR
    DOCS["Documentation<br/>(markdown using mkdocs)"]
    SITE["Docs website"]
    INDEX["Quick-lookup index<br/>(llms.txt)"]
    SKILL["docs-helper skill"]
    READER(["Reader"])
    ASKER(["Quick-answer user"])
    MAINT(["Maintainer"])

    MAINT -->|updates| DOCS
    DOCS --> SITE --> READER
    DOCS -->|auto-generated| INDEX
    ASKER -->|asks a question| SKILL
    INDEX --> SKILL
    SKILL -->|short answer + links| ASKER
```

Each line in `llms.txt` links to a heading, with h3 entries indented under their h2:

```
- [Mocking dependencies](docs/testing/unit-testing.md#mocking-dependencies)
  - [Mocking a database](docs/testing/unit-testing.md#mocking-a-database)
```

## 3. Results

The skill is a single `SKILL.md` file. Each tool looks for it in its own folder:

| Tool | Skill location |
|---|---|
| Claude Code | [`.claude/skills/docs-helper/SKILL.md`](.claude/skills/docs-helper/SKILL.md) |
| GitHub Copilot | `.github/skills/docs-helper/SKILL.md` |

Claude Code works out of the box. For Copilot, copy the skill into place:

```bash
mkdir -p .github/skills
cp -r .claude/skills/docs-helper .github/skills/docs-helper
```

Run your tool from this folder (Claude Code in the terminal, or Copilot Chat in agent mode in VS Code) and invoke it:

```text
/docs-helper how do I mock a database in tests?
```

It refreshes the index, picks the best-matching headings, reads only those sections, and replies with a summary plus a Sources list of links.

| Query | Expected behaviour |
|---|---|
| `how do I mock a database in tests?` | Answers from "Mocking dependencies", links `docs/testing/unit-testing.md#mocking-dependencies` |
| `my tests are slow` | Answers from "Tests are slow", links `docs/faq/troubleshooting.md#tests-are-slow` |
| `how do I deploy to Kubernetes?` | Says the docs don't cover it, suggests adding a page under `docs/`, does not answer from general knowledge |

**Question the docs cover.** The skill reads `llms.txt`, pulls only the matching section, answers from it and links the sources. It also notes that the docs are thin on detail:

<img src="images/docs_helper_skill_demo_covered.png" alt="docs-helper answering a covered question about mocking a database" width="500">

**Question the docs don't cover.** The skill declines to answer from general knowledge, suggests where to add the missing page and lists related headings that don't answer it:

<img src="images/docs_helper_skill_demo_not_covered.png" alt="docs-helper declining a question about Kubernetes that the docs don't cover" width="500">

## 4. Limitations

- The index only holds h1-h3 headings; h4 and deeper are not indexed. If a section's useful content isn't reflected in its heading, the skill can miss it.
- Matching is done by the model reading `llms.txt`, not by a search engine. That works for small docs but won't scale to hundreds of pages without a bigger index.
- Anchors are generated to match MkDocs' default slugs. Custom heading ids or duplicate headings on one page can produce wrong links.
- Links are local markdown paths, not published site URLs.
- The sample docs are generic. Quality of answers depends entirely on the quality of the docs.

## Quick start

### Prerequisites

- **uv**: manages Python and the project's dependencies, so a separate Python install isn't needed.
- **Claude Code**: to use the `/docs-helper` skill.
- **Git**: to clone the repository.

Install commands by operating system (check the official guides for the latest: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Claude Code](https://docs.claude.com/en/docs/claude-code/setup), [Git](https://git-scm.com/downloads)):

| Tool | macOS | Linux | Windows (PowerShell) |
| --- | --- | --- | --- |
| uv | `brew install uv` or `curl -LsSf https://astral.sh/uv/install.sh \| sh` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` or `winget install --id=astral-sh.uv -e` |
| Claude Code | `curl -fsSL https://claude.ai/install.sh \| bash` or `brew install --cask claude-code` | `curl -fsSL https://claude.ai/install.sh \| bash` | `irm https://claude.ai/install.ps1 \| iex` or `winget install Anthropic.ClaudeCode` |
| Git | `brew install git` | `sudo apt install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora) | `winget install --id Git.Git -e` |

Confirm with `uv --version`, `claude --version` and `git --version`.

### Run it

```bash
git clone https://github.com/manickpillai/ai-in-practice.git
cd ai-in-practice/docs-helper
uv sync
uv run mkdocs serve        # http://127.0.0.1:8000, llms.txt at /llms.txt
claude                     # then: /docs-helper <your question>
```

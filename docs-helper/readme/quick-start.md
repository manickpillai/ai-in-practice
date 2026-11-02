# Quick start

[← Back to README](../README.md)

## Prerequisites

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

## Run it

1. Clone the repo:

   ```bash
   git clone https://github.com/manickpillai/ai-in-practice.git && cd ai-in-practice/docs-helper
   ```

2. Start Claude Code, then ask with `/docs-helper <your question>`:

   ```bash
   claude
   ```

To browse the MkDocs site locally:

1. Run:

   ```bash
   uv sync && uv run mkdocs serve
   ```

2. Open <http://127.0.0.1:8000>.

Works with GitHub Copilot too. See [using the skill](usage.md) for example queries.

# Using the skill

[← Back to README](../README.md)

The skill is a single `SKILL.md` file. Each tool looks for it in its own folder:

| Tool | Skill location |
|---|---|
| Claude Code | [`.claude/skills/docs-helper/SKILL.md`](../.claude/skills/docs-helper/SKILL.md) |
| GitHub Copilot | `.github/skills/docs-helper/SKILL.md` |

Claude Code works out of the box. For Copilot, copy the skill into place:

```bash
mkdir -p .github/skills
cp -r .claude/skills/docs-helper .github/skills/docs-helper
```

Run your tool from the `docs-helper` folder (Claude Code in the terminal, or Copilot Chat in agent mode in VS Code) and invoke it:

```text
/docs-helper how do I mock a database in tests?
```

It refreshes the index, picks the best-matching headings, reads only those sections, and replies with a summary plus a Sources list of links.

| Query | Expected behaviour |
|---|---|
| `how do I mock a database in tests?` | Answers from "Mocking dependencies", links `docs/testing/unit-testing.md#mocking-dependencies` |
| `my tests are slow` | Answers from "Tests are slow", links `docs/faq/troubleshooting.md#tests-are-slow` |
| `how do I deploy to Kubernetes?` | Says the docs don't cover it, suggests adding a page under `docs/`, does not answer from general knowledge |

Screenshots are in the [README](../README.md#see-it-in-action).

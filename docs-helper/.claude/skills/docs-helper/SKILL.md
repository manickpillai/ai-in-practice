---
name: docs-helper
description: Answer questions from this project's MkDocs documentation using the generated docs/llms.txt index. Use when the user asks how to do something, or what the docs say, about testing, the FAQ or troubleshooting.
argument-hint: <question about the docs>
---

Answer the user's question using only this project's documentation in `docs/`. The question is: $ARGUMENTS

All paths are relative to the `docs-helper/` project root (the folder containing `mkdocs.yml`). If the current directory is its parent, work in `docs-helper/`.

## Steps


1. Read `docs/llms.txt`. Each line is `- [Heading](docs/path.md#anchor)`, grouped under the page it belongs to.
2. Pick the headings most relevant to the question. Match on meaning, not just exact words (for example "mock a database" matches "Mocking dependencies"). Choose at most 3 or 4.
3. Read those sections from the linked markdown files. Read from the heading to the next heading of the same or higher level, not the whole file.
4. Reply in this shape:
   - A short summary that answers the question, based only on what you read.
   - A **Sources** list with one link per section used, as `[Heading](docs/path.md#anchor)`.

## If the docs do not cover it

If no heading is a reasonable match, or the sections you read do not answer the question:

- Say plainly that the documentation does not cover this.
- Do not answer from general knowledge, even if you know the answer.
- Suggest where it could go: name the closest existing page, or propose a new page, and tell the user to add it under `docs/` (running `uv run mkdocs serve` or the generator will refresh `llms.txt`).
- You may list the closest headings you found, labelled as related but not answering the question.

If the docs only partly answer it, give the part they cover, link it, and state what is missing.

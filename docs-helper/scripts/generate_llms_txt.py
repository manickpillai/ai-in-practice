"""Generate docs/llms.txt from the h1/h2 headings of every markdown file in docs/."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUTPUT = DOCS / "llms.txt"
HEADING = re.compile(r"^(#{1,2})\s+(.+?)\s*#*\s*$")


def slugify(heading: str) -> str:
    """Approximate the anchor ids that MkDocs (python-markdown toc) generates."""
    slug = re.sub(r"[^\w\s-]", "", heading.lower())
    return re.sub(r"[-\s]+", "-", slug).strip("-")


def headings(path: Path):
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and (m := HEADING.match(line)):
            yield len(m.group(1)), m.group(2)


def main() -> None:
    lines = ["# Docs Helper Demo", "", "> Index of documentation headings (h1/h2). Paths are relative to the project root.", ""]
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        found = list(headings(path))
        if not found:
            continue
        title = found[0][1]
        lines.append(f"## {title} ({rel})")
        for level, text in found:
            anchor = "" if level == 1 else f"#{slugify(text)}"
            lines.append(f"- [{text}]({rel}{anchor})")
        lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

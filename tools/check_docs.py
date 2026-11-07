#!/usr/bin/env python3
"""Read-only documentation checks; no network requests or publishing."""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "fe35b326188791cb5f9879de449010185dba42e7"


def heading_ids(text):
    found = set()
    occurrences = {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
        count = occurrences.get(slug, 0)
        occurrences[slug] = count + 1
        found.add(slug if not count else f"{slug}-{count}")
    return found


def normalized(text):
    return "\n".join(line.rstrip() for line in text.splitlines()).strip()


def main():
    documents = sorted(ROOT.rglob("*.md"))
    failures = []
    links = 0
    for path in documents:
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        label = str(path.relative_to(ROOT))
        if len(re.findall(r"^#\s+", content, re.MULTILINE)) != 1:
            failures.append(f"{label}: expected one document title")
        if len(re.findall(r"^```", content, re.MULTILINE)) % 2:
            failures.append(f"{label}: unclosed code fence")
        if any(line.rstrip() != line for line in content.splitlines()):
            failures.append(f"{label}: trailing whitespace")
        if re.search(r"/(?:Users|home)/[^\s)]+|\b(?:\d{1,3}\.){3}\d{1,3}\b", content):
            failures.append(f"{label}: review local path or address before public use")
        for destination in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_file():
                failures.append(f"{label}: missing link target {destination}")
            elif parsed.fragment and unquote(parsed.fragment) not in heading_ids(target.read_text(encoding="utf-8")):
                failures.append(f"{label}: missing heading {destination}")
    archive = ROOT / "docs/archive/README-2016-06-06.md"
    if (ROOT / ".git").exists():
        original = subprocess.check_output(["git", "show", f"{BASE}:README.md"], cwd=ROOT, text=True)
        body = archive.read_text(encoding="utf-8").split("## Original text\n", 1)[1]
        if normalized(body) != normalized(original):
            failures.append("Historical README text differs from its source commit")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"PASS: {len(documents)} Markdown files, {links} internal links, titles, fences, public-data hygiene and historical archive")
    print("External links and engineering/deployment values require separate review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

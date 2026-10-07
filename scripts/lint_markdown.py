#!/usr/bin/env python3
"""Catch Markdown that GitHub renders wrongly, and broken relative links.

GitHub runs Markdown escaping *before* math rendering, so inside plain $...$ or
$$...$$ math a backslash followed by punctuation (\\, \\; \\! \\{ \\} \\| \\\\) loses
its backslash, and `*` can start emphasis. Use $`...`$ for such inline math and a
```math fence for such display math (both are passed through untouched), or
rewrite with \\ (backslash-space), \\quad, \\lbrace, \\rbrace, \\Vert, \\ast.
GitHub also rejects \\operatorname (use \\mathrm). If a plain $...$ span still shows
as raw TeX on github.com (this happens next to parentheses, subscripts or emphasis),
rewrite it as $`...`$.
Inside table rows, a bare `|` in math splits the cell: write \\| or use \\lvert, \\rvert.
Raw NotebookLM outputs (any path containing a `notebooklm/` directory) are skipped.

Usage:
    python3 scripts/lint_markdown.py papers/<slug>      # or any files/directories
Exit code 1 if problems are found.
"""

import re
import sys
from pathlib import Path

ESCAPED = re.compile(r"\\[,;:!{}|\\]")
FENCE = re.compile(r"^(```|~~~)")


def math_spans(line):
    """Yield (kind, text) for $$..$$ and $..$ spans, skipping $`..`$ spans."""
    i = 0
    while i < len(line):
        if line.startswith("$`", i):
            end = line.find("`$", i + 2)
            i = len(line) if end < 0 else end + 2
            continue
        if line.startswith("$$", i):
            end = line.find("$$", i + 2)
            if end < 0:
                yield "display", line[i + 2:]
                return
            yield "display", line[i + 2:end]
            i = end + 2
            continue
        if line[i] == "$":
            end = line.find("$", i + 1)
            if end < 0:
                return
            yield "inline", line[i + 1:end]
            i = end + 1
            continue
        i += 1


def lint_file(md):
    problems = []
    in_code = False
    in_display = False
    for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(line.strip()):
            in_code = not in_code
            continue
        if in_code:
            continue
        is_table = line.lstrip().startswith("|")
        if is_table:
            # In GFM tables, \| is the correct way to write a literal pipe.
            line = line.replace("\\|", "")
        if in_display:
            if ESCAPED.search(line):
                problems.append((n, "escape inside $$ block; use a ```math fence"))
            if "$$" in line:
                in_display = False
            continue
        if line.count("$$") % 2 == 1:
            in_display = True
        for kind, text in math_spans(line):
            if ESCAPED.search(text):
                problems.append((n, f"backslash-punctuation in {kind} math: {ESCAPED.search(text).group()}"))
            if "\\operatorname" in text:
                problems.append((n, "GitHub's math renderer rejects \\operatorname; use \\mathrm{...}"))
            if kind == "inline" and "*" in text:
                problems.append((n, "`*` in inline math can trigger emphasis; use \\ast or $`...`$"))
            if is_table and "|" in text:
                problems.append((n, "`|` inside math in a table row; use \\lvert/\\rvert or \\mid"))
        for target in re.findall(r"\]\(([^)\s]+)\)", line):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (md.parent / target.split("#")[0]).exists():
                problems.append((n, f"broken relative link: {target}"))
    return problems


def main():
    paths = [Path(p) for p in sys.argv[1:]] or [Path(".")]
    files = []
    for p in paths:
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    total = 0
    for md in files:
        # CATALOG.md is generated; notebooklm/ holds raw outputs kept as produced.
        if md.name == "CATALOG.md" or "notebooklm" in md.parts:
            continue
        for n, msg in lint_file(md):
            print(f"{md}:{n}: {msg}")
            total += 1
    print(f"{total} problem(s) in {len(files)} file(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()

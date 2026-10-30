#!/usr/bin/env python3
"""Collate pandoc sources for the two PDFs (stdlib only).

  collate.py solutions OUT.md   -> all solutions/*.md in (chapter, exercise) order,
                                   '# Chapter N — Title' / '## Exercise N.M'
  collate.py errata    OUT.md   -> chapters/addendum.md as a standalone document

Chapter titles come from the first heading of chapters/chapter-NN.qmd.
Any character outside the main text font's coverage (Latin Modern Roman) is
mapped, via newunicodechar, to the Latin Modern Math font so it is not
silently dropped by xelatex ("Missing character" warnings).
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Characters Latin Modern Roman renders natively (ASCII + Latin-1 + Latin Ext-A
# + common punctuation). Everything else non-ASCII gets a math-font fallback.
SAFE = set(range(0x20, 0x7F)) | set(range(0xA0, 0x180)) | {
    0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D, 0x2026, 0x2020, 0x2021, 0x2022,
}


def chapter_titles():
    titles = {}
    for q in sorted((REPO / "chapters").glob("chapter-*.qmd")):
        first = q.read_text(encoding="utf-8").splitlines()[0]
        m = re.match(r"#\s+Chapter\s+(\d+)\s*(?:—\s*(.+))?$", first)
        if not m:
            sys.exit(f"cannot parse chapter heading in {q}: {first!r}")
        titles[int(m.group(1))] = m.group(2)
    return titles


def fallback_header(body):
    chars = sorted({c for c in body if ord(c) > 0x7F and ord(c) not in SAFE})
    if not chars:
        return []
    lines = [
        "header-includes:",
        "  - |",
        "    ```{=latex}",
        "    \\usepackage{newunicodechar}",
        "    \\newfontfamily\\lmmathfallback{latinmodern-math.otf}",
    ]
    for c in chars:
        code = f'{ord(c):04X}'
        lines.append(
            f"    \\newunicodechar{{{c}}}{{\\ifmmode\\text{{\\lmmathfallback\\char\"{code}\\relax}}"
            f"\\else{{\\lmmathfallback\\char\"{code}\\relax}}\\fi}}"
        )
    lines.append("    ```")
    print("font fallback for: " + " ".join(f"{c} U+{ord(c):04X}" for c in chars), file=sys.stderr)
    return lines


def yaml_front(title, subtitle, body):
    parts = ["---", f"title: {title}"]
    if subtitle:
        parts.append(f"subtitle: {subtitle}")
    parts.append("toc-title: Contents")
    parts += fallback_header(body)
    parts += ["---", "", ""]
    return "\n".join(parts)


def solutions():
    titles = chapter_titles()

    def key(p):
        ch, ex = p.stem.split("-", 1)
        return int(ch), int(ex)

    files = sorted((REPO / "solutions").glob("*.md"), key=key)
    body, cur = [], None
    for f in files:
        ch, ex = key(f)
        if ch != cur:
            cur = ch
            t = titles.get(ch)
            body += [f"# Chapter {ch} — {t}" if t else f"# Chapter {ch}", ""]
        body += [f"## Exercise {ch}.{ex}", "", f.read_text(encoding="utf-8").strip(), ""]
    text = "\n".join(body)
    head = yaml_front(
        "Worked Solutions to Concentration Inequalities (Boucheron, Lugosi, Massart)",
        "Solutions only --- no textbook problem statements reproduced",
        text,
    )
    print(f"collated {len(files)} solutions", file=sys.stderr)
    return head + text


def errata():
    src = REPO / "chapters" / "addendum.md"
    if not src.exists():
        sys.exit("chapters/addendum.md not found")
    text = src.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)   # any frontmatter
    text = re.sub(r"^# .*\n", "", text, count=1, flags=re.M)     # page H1 -> PDF title
    text = re.sub(r"^## ", "# ", text, flags=re.M)               # chapters top-level
    text = text.strip() + "\n"
    head = yaml_front(
        "Errata in the Textbook --- Boucheron, Lugosi \\& Massart, Concentration Inequalities (2013)",
        None,
        text,
    )
    return head + text


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("solutions", "errata"):
        sys.exit(__doc__)
    out = solutions() if sys.argv[1] == "solutions" else errata()
    Path(sys.argv[2]).write_text(out, encoding="utf-8")

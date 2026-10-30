#!/usr/bin/env bash
# Build script, used locally and by CI (.github/workflows). Produces, in the repo root:
#   concentration-inequalities-solutions.pdf   all solutions, TOC, 1in margins
#   concentration-inequalities-errata.pdf      chapters/addendum.md as its own PDF
#   docs/                                      Quarto HTML book (incl. the addendum)
#                                              (CI deploys it to GitHub Pages; not committed)
# Usage: ./build.sh [all|solutions|errata|html]     (default: all)
# Needs: python3, quarto (bundled pandoc), xelatex (TinyTeX). Override with
#   QUARTO=/path/to/quarto  TEXBIN=/path/to/texlive/bin/<arch>
set -euo pipefail
cd "$(dirname "$0")"

QUARTO="${QUARTO:-$HOME/workspace/tools/quarto/quarto-1.6.42/bin/quarto}"
TEXBIN="${TEXBIN:-$HOME/.TinyTeX/bin/x86_64-linux}"
command -v "$QUARTO" >/dev/null || QUARTO=quarto
export PATH="$TEXBIN:$PATH"
export TMPDIR="${TMPDIR:-$PWD/build/tmp}"
mkdir -p build "$TMPDIR"

PANDOC_ARGS=(--pdf-engine=xelatex -V geometry:margin=1in --toc --toc-depth=2)

pdf() {  # pdf <kind> <out.pdf>
  local kind=$1 out=$2 t0=$SECONDS
  python3 scripts/collate.py "$kind" "build/$kind.md"
  "$QUARTO" pandoc "build/$kind.md" -o "$out" "${PANDOC_ARGS[@]}" --verbose \
    > "build/$kind.log" 2>&1 || { tail -40 "build/$kind.log"; echo "FAILED: $out" >&2; exit 1; }
  local miss; miss=$(grep -c "Missing character" "build/$kind.log" || true)
  echo "built $out in $((SECONDS - t0))s (missing-glyph warnings: $miss; log build/$kind.log)"
  if [ "$miss" != 0 ]; then grep "Missing character" "build/$kind.log" | sort | uniq -c >&2; fi
}

html() {
  local t0=$SECONDS
  [ -f chapters/addendum.md ] || { echo "chapters/addendum.md missing" >&2; exit 1; }
  rm -rf docs
  "$QUARTO" render --to html > build/html.log 2>&1 || { tail -40 build/html.log; exit 1; }
  touch docs/.nojekyll
  echo "rendered docs/ in $((SECONDS - t0))s ($(find docs -name '*.html' | wc -l) html pages; log build/html.log)"
}

case "${1:-all}" in
  solutions) pdf solutions concentration-inequalities-solutions.pdf ;;
  errata)    pdf errata concentration-inequalities-errata.pdf ;;
  html)      html ;;
  all)       pdf solutions concentration-inequalities-solutions.pdf
             pdf errata concentration-inequalities-errata.pdf
             html ;;
  *) echo "usage: $0 [all|solutions|errata|html]" >&2; exit 2 ;;
esac

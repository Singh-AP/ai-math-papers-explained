#!/usr/bin/env python3
"""Render every page of a slide-deck PDF to slide-NN.png at full quality.

Usage:
    uv run --with pymupdf python scripts/render_slides.py slides.pdf out_dir [dpi=200]
"""

import sys
from pathlib import Path

import pymupdf


def main():
    pdf, outdir = sys.argv[1], Path(sys.argv[2])
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    outdir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    for i, page in enumerate(doc, 1):
        page.get_pixmap(dpi=dpi).save(outdir / f"slide-{i:02d}.png")
    print(f"rendered {doc.page_count} slides to {outdir}")


if __name__ == "__main__":
    main()

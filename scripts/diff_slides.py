#!/usr/bin/env python3
"""Report which slides differ between two versions of a deck.

`nlm slides revise` regenerates a whole deck, and it can garble slides you did
not ask to change. Run this to confirm only the intended slides changed.

Usage:
    uv run --with pymupdf python scripts/diff_slides.py original.pdf revised.pdf
"""

import sys

import pymupdf


def main():
    a, b = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    if a.page_count != b.page_count:
        print(f"page count differs: {a.page_count} vs {b.page_count}")
    for i, (pa, pb) in enumerate(zip(a, b), 1):
        xa, xb = pa.get_pixmap(dpi=40).samples, pb.get_pixmap(dpi=40).samples
        changed = sum(1 for u, v in zip(xa, xb) if abs(u - v) > 40) / max(len(xa), 1)
        print(f"slide {i:02d}: {'CHANGED' if changed > 0.01 else 'same   '} ({changed:.3f})")


if __name__ == "__main__":
    main()

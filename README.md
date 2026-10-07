# AI Math Papers, Explained

**Beginner-friendly explainers for the AI-generated research papers in [openai/math](https://github.com/openai/math).**

In autumn 2026 OpenAI released a collection of 722 mathematical manuscripts in 372 result families, produced by an internal model working on open research problems. They are written for specialists. This repository explains them to beginners in each field.

Every explainer answers the same questions:

1. **What does the paper actually say?** The result in plain language.
2. **What was the problem?** The question, with enough background to follow it.
3. **What's the history?** Who tried before, and what they achieved.
4. **Why does it matter?** Significance and consequences.
5. **What's the main idea?** How the proof works, at several zoom levels.
6. **Whose ideas does it build on?** The people behind the tools.
7. **What doesn't it prove?** Caveats, scope and verification status.

Each explainer comes with visual material generated with **Google NotebookLM**: slide decks, infographics, mind maps, reports and a short audio overview. All of it is checked against the paper, with known errors listed in each paper's errata.

## Explained so far

| Field | Paper | Explainer |
|---|---|---|
| Algebraic geometry | **The rational Hodge conjecture for CM abelian varieties** (family 032). On every complex abelian variety with complex multiplication, every rational Hodge class comes from algebraic cycles. This is a major case of the Hodge conjecture, a Millennium Prize problem | [Read it](papers/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/) |
| Number theory | **The Quasi-Riemann Hypothesis: a zero-free half-plane Re(s) > 7/8** (family 003). The Riemann zeta function and every Dirichlet $L$-function have no zeros with real part above 7/8 | [Read it](papers/The-Quasi-Riemann-Hypothesis-September-30-2026/) |
| Combinatorics | **Quasipolynomial bounds for arithmetic progressions** (family 159). Erdős's conjecture is true: every set of positive integers whose reciprocals sum to infinity contains arithmetic progressions of every length | [Read it](papers/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/) |
| Number theory | **The irrationality exponent of π is 2** (family 017). π cannot be approximated by fractions much better than a typical number can; as a consequence, the Flint Hills series $\sum 1/(n^3 \sin^2 n)$ converges | [Read it](papers/The-irrationality-exponent-of-pi-is-2-September-24-2026/) |
| Number theory / logic | **Hilbert's tenth problem over the rational numbers** (family 004). No algorithm can decide whether a polynomial equation with integer coefficients has a rational solution | [Read it](papers/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/) |
| Theoretical computer science | **The Unique Games Theorem** (family 102). Khot's Unique Games Conjecture is true: for unique games over a large enough alphabet, distinguishing almost-satisfiable instances from barely-satisfiable ones is NP-hard | [Read it](papers/The-Unique-Games-Theorem-September-23-2026/) |
| Theoretical computer science | **An upper bound of 9/4 for the matrix multiplication exponent** (family 107). Over the complex numbers, $n \times n$ matrices can be multiplied with $O(n^{9/4+\varepsilon})$ arithmetic operations for every $\varepsilon > 0$ | [Read it](papers/Matrix-Multiplication-Nine-Fourths-October-2-2026/) |
| Combinatorial geometry | **The Euclidean plane is not five-colorable** (family 158). However you color the plane with five colors, some two points at distance exactly 1 get the same color, so the chromatic number of the plane is 6 or 7 | [Read it](papers/The-Euclidean-plane-is-not-five-colorable-September-23-2026/) |
| Convex geometry | **The symmetric Mahler conjecture** (family 087). Every origin-symmetric convex body $K$ in $n$ dimensions has volume product $\lvert K\rvert\ \lvert K^\circ\rvert \ge 4^n/n!$, with equality exactly for Hanner polytopes | [Read it](papers/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) |
| Dynamical systems | **Hilbert's sixteenth problem: uniform bounds for limit cycles** (family 143). A planar polynomial vector field of degree $d$ has at most $B(d)$ limit cycles, a bound depending only on the degree | [Read it](papers/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/) |

The full list of all 722 papers and their status is in **[CATALOG.md](CATALOG.md)**.

## Repository layout

```
papers/
  <preprint-slug>/              # one directory per openai/math paper, same name as openai/math/preprints/<slug>/
    README.md                   # the explainer
    assets/
      README.md                 # inventory, notebook sources, errata
      figures/                  # hand-made diagrams
      notebooklm/               # NotebookLM outputs: slides, infographics, reports, mind maps, audio
CATALOG.md                      # every paper, grouped by discipline and family (generated)
PIPELINE.md                     # how an explainer is produced, step by step
scripts/
  build_catalog.py              # regenerates CATALOG.md from openai/math
  mindmap_to_markdown.py        # renders NotebookLM mind-map JSON as Markdown
```

Directory names match `openai/math/preprints/` exactly, so every explainer maps to exactly one manuscript.

## A note on trust

These are explainers, not peer review. The underlying papers were produced by an AI model, and openai/math itself notes that unformalized results may contain errors. Each explainer records what has been formally verified (for example in Lean) and what hasn't. NotebookLM outputs are AI-generated as well, so every paper's `assets/README.md` lists the mistakes found in them.

## Contributing

Pick a paper marked ⬜ in [CATALOG.md](CATALOG.md) and follow [PIPELINE.md](PIPELINE.md). Corrections to existing explainers are very welcome. Open an issue or a pull request.

## License

The explanations, figures and generated assets in this repository are licensed under [CC BY-SA 4.0](LICENSE). The papers belong to openai/math, which is released under the Apache 2.0 license; this repository links to them rather than copying them.

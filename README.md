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
| Number theory | **The Quasi-Riemann Hypothesis: a zero-free half-plane Re(s) > 7/8** (family 003). The Riemann zeta function and every Dirichlet $L$-function have no zeros with real part above 7/8 | [Read it](papers/The-Quasi-Riemann-Hypothesis-September-30-2026/) |

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

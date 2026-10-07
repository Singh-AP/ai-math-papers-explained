# How an explainer is made

This is the repeatable process used for each paper. It uses [`notebooklm-mcp-cli`](https://github.com/jacob-bd/gemini-notebook-mcp-cli), which provides both the `nlm` command-line tool and an MCP server (`gemini-notebook-mcp`) that Claude Code and other agents can call. The commands below use the CLI; the MCP tools (`notebook_create`, `source_add`, `studio_create`, `download_artifact`, …) do the same things.

## 0. One-time setup

```bash
uv tool install notebooklm-mcp-cli      # installs `nlm` and the MCP server
nlm setup add claude-code               # register the MCP server with Claude Code
nlm login --profile <name>              # sign in to Google in a browser window
nlm auth storage set protected          # keep the saved login encrypted in the OS keychain
```

If the automatic browser launch fails (for example inside a sandboxed agent shell), start a Chromium browser yourself with a dedicated profile and remote debugging, then attach:

```bash
"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
  --remote-debugging-port=9222 --user-data-dir="$HOME/.notebooklm-mcp-cli/chrome-profiles/<name>" \
  https://notebooklm.google.com/ &
nlm login --profile <name> --provider openclaw --cdp-url http://127.0.0.1:9222
```

Close that browser after the login succeeds. If Chromium's own sandbox fails because the agent shell is sandboxed (exit code -5, GPU process crashes), add `--no-sandbox` for this one sign-in only.

## 1. Pick the paper and fetch its sources

```bash
SLUG=The-Quasi-Riemann-Hypothesis-September-30-2026            # directory name in openai/math/preprints/
gh api repos/openai/math/contents/preprints/$SLUG --jq '.[].name'
curl -sLO https://raw.githubusercontent.com/openai/math/main/preprints/$SLUG/paper.pdf
curl -sLO https://raw.githubusercontent.com/openai/math/main/preprints/$SLUG/build/paper.tex   # when available
```

Also collect companion papers from the same family (see [CATALOG.md](CATALOG.md)), the Lean scope document `lean/docs/<family>.md` if one exists, and one background source for history, such as a Wikipedia article.

## 2. Build the notebook

```bash
NB=$(nlm notebook create "<Title> (OpenAI math <family>) — Beginner Explainer" --json | jq -r .notebook_id)
nlm source add $NB --file paper.pdf --wait
nlm source add $NB --file companion.pdf --wait
nlm source add $NB --url https://github.com/openai/math/blob/main/lean/docs/<family>.md --wait
nlm source add $NB --url https://en.wikipedia.org/wiki/<Background_topic> --wait
```

## 3. Generate the assets

Write each prompt for **beginners in the paper's field**, and name the topics that must be covered: problem, history, significance, main idea, people, and what the result does not prove.

**Budget the quota first.** Studio work is metered against a rolling window of about five hours (`nlm usage`). One paper with the standard set below uses roughly 20–25% of that window; every slide-deck revision costs about as much as a new deck. Check `nlm usage` before generating, and don't start a set if less than about 25% remains.

Standard set (one of each):

```bash
nlm slides create      $NB --format detailed_deck --focus "<beginner brief>" --confirm --json
nlm infographic create $NB --orientation portrait  --detail detailed --style instructional --focus "<overview brief>" --confirm --json
nlm infographic create $NB --orientation landscape --style sketch_note --focus "<history timeline brief>" --confirm --json
nlm report create      $NB --format "Create Your Own" --prompt "<sectioned beginner explainer>" --source-ids <paper ids> --confirm --json
nlm mindmap create     $NB --title "How the proof works" --source-ids <paper ids> --confirm --json
nlm audio create       $NB --format brief --focus "<beginner brief>" --confirm --json
nlm studio status      $NB --json   # wait until everything is "completed"; slide decks take 10–15 minutes
```

Save every artifact ID together with its **type and title** when it is created (the `--json` output). Never pair IDs with outputs by list position: `nlm studio status` does not list artifacts in creation order. After downloading a mind map, check its root `name` to confirm it is the map you meant.

Restrict reports and mind maps to the paper sources (`--source-ids`). Background sources such as Wikipedia pull in unrelated and unverifiable claims.
## 4. Download, keeping full quality

```bash
A=papers/$SLUG/assets/notebooklm; mkdir -p $A/slides
nlm download slide-deck  $NB --id <id> --output $A/slides.pdf
nlm download slide-deck  $NB --id <id> --format pptx --output $A/slides.pptx
nlm download infographic $NB --id <id> --output $A/infographic-overview.png
nlm download report      $NB --id <id> --output $A/beginner-explainer-report.md
nlm download mind-map    $NB --id <id> --output $A/mindmap-proof.json
nlm download audio       $NB --id <id> --output $A/audio-overview-brief.m4a
```

Do not recompress or downscale anything; GitHub handles the file sizes. Render slides as per-page PNGs and turn mind maps into Markdown:

```bash
uv run --with pymupdf python scripts/render_slides.py $A/slides.pdf $A/slides 200
python3 scripts/mindmap_to_markdown.py "How the proof works" $A/mindmap-proof.json > $A/mindmaps.md
```

## 5. Review every generated asset against the paper

Look at **every** slide image, both infographics and the report, and compare each with the paper. NotebookLM reliably gets the big picture right and sometimes gets details wrong. Errors seen so far:

- shading the wrong side of a boundary (a "zero-free zone" drawn on the side where zeros are still possible);
- swapping which half of an argument gives the upper bound and which gives the lower bound;
- inventing a proof mechanism (for example a positivity argument the paper never uses);
- typos inside formulas in images ($n^{-\varepsilon}$ for $n^{-s}$);
- importing unverified claims from background sources.

Then:

- Fix only clearly wrong slides with **one** `nlm slides revise <deck-id> --slide '<n> <instruction>' --confirm`, naming only the broken slides. A revision regenerates the whole deck and can garble slides it wasn't asked to touch, so download it and check with `uv run --with pymupdf python scripts/diff_slides.py old.pdf new.pdf`. Ship it only if the intended slides changed for the better and nothing else did.
- Record everything that stays wrong in `assets/README.md` under **Errata**, file by file.
- Mark claims that come only from background sources and can't be checked as **unverified**.
- The audio can't be reviewed by reading. Say so in the errata.

## 6. Write the explainer by hand

Write `papers/$SLUG/README.md` **from the paper itself**, using NotebookLM output only for structure and visuals. [The quasi-Riemann hypothesis explainer](papers/The-Quasi-Riemann-Hypothesis-September-30-2026/) is the reference: copy its structure and tone.

TL;DR → how to read → the problem → history → what the paper proves → why it matters → main idea (several zoom levels, with a Mermaid flowchart and one worked calculation where possible) → people → what it does not prove and caveats (provenance, Lean status, preprint status) → glossary → assets (with a collapsible slide gallery) → how it was made.

Rules that keep it trustworthy:

- Every factual claim about the paper must be traceable to the paper or its openai/math README / Lean docs. Check dates and attributions of historical results; leave out what you can't verify.
- State the Lean status exactly as `lean/docs/<family>.md` and `lean/formalization.yaml` describe it, and say that you did not re-run the build.
- Embed the most useful slides inline and put all of them in a `<details>` gallery.

GitHub math pitfalls (run `python3 scripts/lint_markdown.py papers/$SLUG` and fix everything it reports):

- Inside `$…$` / `$$…$$`, Markdown eats backslash-punctuation: `\,` `\;` `\!` `\{` `\}` `\\`. Use `\ ` (backslash-space), `\quad`, `\lbrace`/`\rbrace`, or write the formula as `` $`…`$ `` (inline) or in a ```` ```math ```` fence (display).
- `*` inside inline math can start emphasis. Write `^{\ast}`.
- In table rows, write `|` inside math as `\|`, `\lvert`/`\rvert` or `\mid`.
- A multi-line `>` header block needs a list (`> - **Paper:** …`), otherwise its lines run together.

## 7. Update the catalogue and publish

```bash
curl -sLO https://raw.githubusercontent.com/openai/math/main/CONTENTS.md
curl -sLO https://raw.githubusercontent.com/openai/math/main/overview.tex
python3 scripts/build_catalog.py CONTENTS.md overview.tex > CATALOG.md
```

Add the paper to the table in the top-level `README.md`, run `python3 scripts/lint_markdown.py papers README.md`, then commit and push. Finally, open the explainer on github.com and check that the math, Mermaid diagram, alerts and images render.

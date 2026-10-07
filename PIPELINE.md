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

```bash
nlm slides create      $NB --format detailed_deck --focus "<beginner brief>" --confirm
nlm infographic create $NB --orientation portrait  --detail detailed --style instructional --focus "<overview brief>" --confirm
nlm infographic create $NB --orientation landscape --style sketch_note --focus "<history timeline brief>" --confirm
nlm report create      $NB --format "Create Your Own" --prompt "<sectioned beginner explainer>" --confirm
nlm report create      $NB --format "Study Guide" --confirm
nlm mindmap create     $NB --title "How the proof works" --source-ids <paper source ids> --confirm
nlm audio create       $NB --format brief --focus "<beginner brief>" --confirm
nlm studio status      $NB          # wait until everything is "completed"; slide decks take longest
```

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

Do not recompress images. Render slides as per-page PNGs at 200 DPI, for example with `pymupdf`. Turn mind maps into Markdown with `scripts/mindmap_to_markdown.py`.

## 5. Review every generated asset against the paper

Read every slide, infographic and report, and compare it with the paper. NotebookLM reliably gets the big picture right and sometimes gets details wrong, for example by shading the wrong side of a boundary or inventing a proof mechanism. Then:

- Fix slides with `nlm slides revise <deck-id> --slide '<n> <instruction>' --confirm` and re-download.
- Record anything that stays wrong in `assets/README.md` under **Errata**.
- Mark claims that come only from background sources and can't be checked as **unverified**.

## 6. Write the explainer by hand

Write `papers/$SLUG/README.md` **from the paper itself**, using NotebookLM output only for structure and visuals. Use the same sections as the existing explainers:

TL;DR → how to read → the problem → history → what the paper proves → why it matters → main idea (several zoom levels) → people → what it does not prove and caveats → glossary → assets → how it was made.

## 7. Update the catalogue and publish

```bash
curl -sLO https://raw.githubusercontent.com/openai/math/main/CONTENTS.md
curl -sLO https://raw.githubusercontent.com/openai/math/main/overview.tex
python3 scripts/build_catalog.py CONTENTS.md overview.tex > CATALOG.md
```

Add the paper to the table in the top-level `README.md`, then commit and push.

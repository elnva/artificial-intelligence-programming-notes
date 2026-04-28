# AI Programming with Python — Study Notes

This repository is a hand-typed study companion to Perry Xiao's *Artificial Intelligence Programming with Python: From Zero to Hero*. The book itself is not included in this repository; you bring your own copy.

## How we work (the workflow contract)

These rules govern every session. Claude reads this file and follows it.

1. **One stage equals one book chapter.** A stage lives in `stages/stage-NN-<slug>/`, and its tutorial lives in `docs/stages/stage-NN-<slug>.md`.

2. **Each stage starts when the user brings the relevant chapter content into the session.** Claude does not guess content from the book.

3. **Tutorials are walked one step at a time.** The tutorial document lists numbered steps. Claude introduces ONE step at a time, waits for the user to confirm completion, then moves to the next. No dumping the whole chapter at once. Each step includes:
   - What to do
   - Why it matters
   - Expected output / how to know it worked
   - A clear "tell me when done" cue

4. **The user types every example by hand.** Claude shows code only inside chat replies or inside the tutorial document as fenced snippets; the user transcribes them into `stages/stage-NN-<slug>/examples/`. Claude **never creates `.py` files for the user, never runs Python, and never executes the user's code.** Verifying that something works is the user's job — that is part of the learning.

5. **Each tutorial is a small teach-and-do.** Every step explains the concept first (a sentence or two — the "teach"), then states the action (the "do"). The user finishes a stage with deep understanding, not just a copied folder.

6. **Notes are the user's voice.** `stages/stage-NN-<slug>/notes.md` is for the user's own observations, questions, and "aha" moments. Claude does not write into it unless asked.

7. **Each stage ends with three things done:** examples transcribed, exercises attempted, and `docs/plan.md` status updated to `done`.

8. **Tutorial tone is normal prose.** Chat replies may be terse / caveman style; the tutorials in `docs/stages/` are teaching material and read in full sentences.

## Layout

- `docs/` — this README, the roadmap (`plan.md`), and per-stage tutorials.
- `stages/` — one folder per chapter, holding hand-typed examples, exercises, and the user's notes.
- `src/` — reusable modules. Anything written for one stage that turns out to be useful across stages graduates to here.
- `tests/` — pytest tests, mirroring the `src/` layout.
- `shared/` — shared datasets and helper utilities.
- `pyproject.toml` — single source of truth for project metadata, dependencies, and tool config (ruff, pytest).
- `requirements.txt` — flat dependency list for fast `pip install -r`.

## Starting a new stage

Use the `/new-stage` slash command:

```
/new-stage 01 intro-ai
```

This scaffolds the folder, the tutorial template, and a row in `docs/plan.md`. Then share the chapter pages and Claude fills in the steps.

## Environment

- Python `3.10` (pinned in `.python-version`)
- Virtual env: `python3.10 -m venv .venv && source .venv/bin/activate`
- Dependencies are added per stage as the book introduces them. The current cumulative list lives in `requirements.txt` and the pinned section of `pyproject.toml`.

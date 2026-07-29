# AI Programming with Python — Study Notes

This repository is a hand-typed study companion to Perry Xiao's *Artificial Intelligence Programming with Python: From Zero to Hero*. The book itself is not included in this repository; you bring your own copy.

## How we work (the workflow contract)

These rules govern every session. Claude reads this file and follows it.

1. **One folder equals one book chapter.** A chapter lives in `src/chapters/chapter-NN-<slug>/` and its `README.md` is the tutorial. Folder numbers match book chapter numbers.

2. **Each chapter starts when the user brings the relevant chapter content into the session.** Claude does not guess content from the book.

3. **Tutorials are walked one step at a time.** The tutorial `README.md` lists numbered steps. Claude introduces ONE step at a time, waits for the user to confirm completion, then moves to the next. No dumping the whole chapter at once. Each step includes:
   - What to do (the "do")
   - Why it matters (the "teach")
   - Expected output / how to know it worked
   - A clear "tell me when done" cue

4. **The user types every example by hand.** Claude shows code only inside chat replies or inside the tutorial document as fenced snippets; the user transcribes them into `src/chapters/chapter-NN-<slug>/examples/` (or `exercises/`). Claude **may create empty placeholder `.py` files** as scaffolding (zero bytes, no code, no comments) so the user has the right filename to open and type into; Claude **never writes code into those files, never runs Python, and never executes the user's code**. Verifying that something works is the user's job — that is part of the learning.

5. **Each tutorial is a small teach-and-do.** Every step explains the concept first (a sentence or two — the "teach"), then states the action (the "do"). The user finishes a chapter with deep understanding, not just a copied folder.

6. **Notes are the user's voice.** `src/chapters/chapter-NN-<slug>/notes.md` is for the user's own observations, questions, and "aha" moments. Claude does not write into it unless asked. Book content is never copied into `notes.md` or `README.md`.

7. **Each chapter ends with three things done:** examples transcribed, exercises attempted, and the row in `docs/plan.md` updated to `done`.

8. **Tutorial tone is normal prose.** Chat replies may be terse / caveman style; the tutorial `README.md` files are teaching material and read in full sentences.

## Layout

- `docs/` — repo-level documentation only: this workflow contract and the chapter roadmap (`plan.md`).
- `src/chapters/` — one folder per book chapter (`chapter-NN-<slug>/`). Each folder holds the chapter's tutorial `README.md`, the user's `notes.md`, an `examples/` folder for follow-along scripts, and an `exercises/` folder for the book's exercises.
- `tests/` — pytest tests when needed (currently empty).
- `pyproject.toml` — single source of truth for project metadata, dependencies, and tool config (ruff, pytest).
- `requirements.txt` — flat dependency list for fast `pip install -r`.

## Starting a new chapter

Use the `/new-chapter` slash command:

```
/new-chapter 03 machine-learning
```

This scaffolds `src/chapters/chapter-03-machine-learning/` with `README.md` (tutorial template), `notes.md`, and empty `examples/` and `exercises/` folders, and updates `docs/plan.md`. Then bring the chapter content into the session and Claude fills in the steps.

## Environment

- Python `3.10` (pinned in `.python-version`, resolved by pyenv to `3.10.20`)
- Virtual env: `python -m venv .venv && source .venv/bin/activate`
- Dependencies are added per chapter as the book introduces them. The current cumulative list lives in `requirements.txt` and the optional sections of `pyproject.toml`.

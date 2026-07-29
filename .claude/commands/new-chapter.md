---
description: Scaffold a new chapter folder under src/chapters/ with tutorial, notes, and examples/exercises subfolders
argument-hint: <chapter-number> <slug>
---

You are scaffolding a new chapter for the Perry Xiao "AI Programming with Python" notes repo.

Arguments: `$ARGUMENTS` — expected as `<NN> <slug>`, for example: `03 machine-learning`.

The command runs in two phases. **Phase A** runs immediately when the slash command is invoked (folder + tutorial template). **Phase B** runs later in the same session, AFTER the user shares the chapter content and Claude fills in the tutorial steps — Phase B creates empty `.py` stubs for every example and exercise the tutorial mentions.

## Phase A — folder scaffold (run on slash invocation)

1. Parse the two arguments. Pad the chapter number to two digits. Build `CHAPTER_DIR=src/chapters/chapter-<NN>-<slug>`.
2. If `$CHAPTER_DIR` already exists, stop and tell the user it exists — do not overwrite.
3. Create the chapter folder structure:
   - `$CHAPTER_DIR/README.md` — the tutorial (template below)
   - `$CHAPTER_DIR/notes.md` — empty headings for the user's own thoughts
   - `$CHAPTER_DIR/examples/.gitkeep`
   - `$CHAPTER_DIR/exercises/.gitkeep`
4. Use this tutorial template for `README.md`:
   - `# Chapter <NN> — <Title TBD>`
   - blockquote noting the book chapter
   - `## Goal`
   - `## Prerequisites`
   - `## How to read the steps` (Teach / Do / Expected / Tell me when done)
   - `## Steps` (numbered, ONE action per step — leave placeholders for now)
   - `## Exercises`
   - `## Recap`
5. Use this notes template for `notes.md`:
   - `# Notes — Chapter <NN> (<Title TBD>)`
   - `## Open questions`
   - `## Insights`
   - `## Vocabulary`
6. Update the matching row in `docs/plan.md` from `todo` to `in-progress` and replace the scaffold hint with the real path: `[chapter-<NN>-<slug>/README.md](../src/chapters/chapter-<NN>-<slug>/README.md)`.
7. Print a short summary of what was created and remind the user to bring the chapter content into the session so the tutorial steps can be filled in.

## Phase B — stub empty example/exercise files (run after the tutorial steps are filled in)

Once Phase A is done and the user has shared the chapter content and the tutorial `README.md` has its concrete numbered steps written, do this:

1. Read the chapter `README.md`.
2. Extract every filename of the form `NN-<slug>.py` (examples) and `ex-<chapter>-<num>-<slug>.py` (exercises).
3. For each filename:
   - If the file does NOT yet exist under `examples/` or `exercises/`, create it as a zero-byte file.
   - If the file already exists, leave it alone — the user may have started typing.
4. Remove `examples/.gitkeep` if `examples/` now has any `.py` files; same for `exercises/`.
5. Print a short list of created stubs and skipped (already-present) files.

Hard rules for both phases:

- Never write code, comments, or docstrings into the stub files. Stubs are zero bytes.
- Never copy passages or examples from the book into any file in the repo.
- The tutorial `README.md` is the ONLY place code snippets appear, as fenced markdown blocks the user transcribes by hand.

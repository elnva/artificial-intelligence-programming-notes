---
description: Scaffold a new chapter folder under src/chapters/ with tutorial, notes, and examples/exercises subfolders
argument-hint: <chapter-number> <slug>
---

You are scaffolding a new chapter for the Perry Xiao "AI Programming with Python" notes repo.

Arguments: `$ARGUMENTS` — expected as `<NN> <slug>`, for example: `03 machine-learning`.

Steps:

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

Do NOT write book code into `examples/` or `exercises/` — the user transcribes those by hand. The tutorial `README.md` is where snippets live as they are introduced step by step. Never copy long passages from the book into any file.

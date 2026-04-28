---
description: Scaffold a new stage (one per book chapter) with notes, examples, exercises, and tutorial doc
argument-hint: <stage-number> <slug>
---

You are scaffolding a new learning stage for the Perry Xiao "AI Programming with Python" notes repo.

Arguments: `$ARGUMENTS` — expected as `<NN> <slug>`, for example: `01 intro-ai`.

Steps:

1. Parse the two arguments. Pad the stage number to two digits. Build `STAGE_DIR=stages/stage-<NN>-<slug>` and `DOC_FILE=docs/stages/stage-<NN>-<slug>.md`.
2. If `$STAGE_DIR` already exists, stop and tell the user it exists — do not overwrite.
3. Create the stage folder structure:
   - `$STAGE_DIR/README.md` — chapter title placeholder, link to `$DOC_FILE`
   - `$STAGE_DIR/notes.md` — empty heading "# Notes — Stage NN" for the user's own thoughts
   - `$STAGE_DIR/examples/.gitkeep`
   - `$STAGE_DIR/exercises/.gitkeep`
4. Create `$DOC_FILE` using the tutorial template:
   - `# Stage NN — <Chapter title TBD>`
   - `## Goal`
   - `## Prerequisites`
   - `## Steps` (numbered, ONE action per step, each with: what to do, why, expected output, "tell me when done")
   - `## Exercises`
   - `## Recap`
5. Append a row to the table in `docs/plan.md`: `| NN | TBD | <slug> | todo | docs/stages/stage-NN-slug.md |`.
6. Print a short summary of what was created and remind the user to share the chapter pages so the tutorial steps can be filled in.

Do NOT write book code into `examples/` — the user transcribes those by hand. The tutorial file in `docs/stages/` is where code snippets live as they are introduced step by step.

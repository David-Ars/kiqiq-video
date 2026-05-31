---
name: kiqiq-produce
description: Run the whole KiqIQ video pipeline end to end for one player, fully automated, pausing only at the two approval gates. Triggers: produce, make the video, run the pilot, full video for [player].
---

# KiqIQ produce (full auto)

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude orchestrates the pipeline autonomously. See `Videos/_context/RUNBOOK.md`. This is STEP TWO: it assumes kiqiq-researcher (the full research role: competitive scan + fact sheet) has already produced `output/<slug>/working-doc.md` section 1 and `output/<slug>/fact-sheet.md`. If the fact sheet is missing, STOP and tell David to run kiqiq-researcher first.

Take the player or team from David (or, if asked, pick one from the strongest archive coverage). Then run, invoking each role skill in turn and passing the working-doc and fact-sheet along: archivist check; confirm the research scan in working-doc section 1 was a LIVE Chrome scan with real channels, view counts and URLs (if it is missing or marked approximate, run the live scan now via Chrome before proceeding); an INDEPENDENT fact-check of the researcher's fact sheet (do NOT trust the compiled values: re-derive every thesis-critical figure from a primary or higher-tier source, confirm scope on every appearance and card total, confirm any never/zero/only superlative career-wide, correct the sheet and note each change, and bar any figure that cannot be verified from reaching the script); angle strategist; then GATE 1 (present the angle AND the fact-check result, wait for David's approval); chart builder, scriptwriter, art director, shot planner; then narration (render via `tts.py` on David's PC, or drive ElevenLabs in Chrome); then assemble with Remotion (`_system/remotion`); packager; then GATE 2 (present the final cut); publisher. Run autonomously between gates with no step-by-step narration. The only human touches are: pick the player, approve at the two gates, confirm the publish click. If David says 'no gates', proceed straight through and present the finished upload for a single final confirm.

## Next step (always end with this)

When this step finishes, end the reply by telling David exactly what to run next:

> Next: run no separate next skill; resume this same run after David clears each gate, and report the published video at the end.

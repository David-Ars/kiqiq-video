---
name: kiqiq-art-director
description: Generate the stylized, consistent player imagery via the Gemini image tool. Triggers: generate the art, make the player images, render the reference.
---

# KiqIQ art director

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude generates the imagery with the Gemini image tool. SOP Role 5.

Read `Videos/_context/ART-STYLE-GUIDE.md` and working-doc sections 4 and 8. Generate one hero reference render in the chosen style, lock it, then derive every other shot from it with image-to-image, holding the style line constant. Player mode: show the figure but keep the face abstract and non-literal (simplified, geometric, masked, posterised or gestural). Identity comes from build, height, hair, posture, kit colours, era and context, never an exact face and never the player's name. Team mode: no single face; use kit colours, a stylised original emblem if needed (never the real crest), the crowd, the stadium and era. Use the prompt skeletons in ART-STYLE-GUIDE.md. Plain kit, no logos. Remove the visible Gemini/nano-banana watermark by inpainting it out (content-aware fill via the nano-banana edit tool, or generate at a larger canvas and reconstruct the covered area), NOT a simple crop that loses composition. Check at 100% zoom: it must not be noticeable at all, no smudge or repeated-texture artefact where the mark was. SynthID stays embedded and the YouTube AI-content disclosure still applies, so removing the visible mark does not hide that the image is AI. Save to `<slug>/art/`, references to `Videos/input/reference-art/`.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run **kiqiq-shot-planner** — input: the same player.

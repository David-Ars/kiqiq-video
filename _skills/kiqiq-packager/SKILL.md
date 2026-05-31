---
name: kiqiq-packager
description: Produce titles, thumbnail, description and tags. Triggers: package the video, make the thumbnail, write the title and description.
---

# KiqIQ packager

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude packages the video. SOP Role 7.

Use `Videos/_system/thumb.py` with the episode preset, hero stat, label and a 3 to 4 word title. Title is the promise; thumbnail shows the proof and never duplicates the title. Check the 120px preview. Write title options, description, tags and chapters into working-doc section 9. For title and tag signal you may consult David's free VidIQ web account via Claude in Chrome (leads only, never overriding the analytical thesis or the anti-hype voice). Save thumbnails to `<slug>/thumbnails/`. `thumb.py` runs in bash, so confirm the PNGs actually landed in the episode `thumbnails/` folder; if the mount has not synced, write them to the outputs area and surface them with present_files so David can save the chosen one.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run after David approves the final cut (gate 2), **kiqiq-publisher** — input: the same player.

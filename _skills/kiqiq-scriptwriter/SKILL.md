---
name: kiqiq-scriptwriter
description: Write the ElevenLabs narration script for a player video. Triggers: write the script, draft the narration.
---

# KiqIQ scriptwriter

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude writes the narration for ElevenLabs. SOP Role 4.

Read working-doc sections 3 and 4 and the locked fact sheet. Target length: aim for the runtime of the strong performers found in the research scan (section 1); default to 8 to 12 minutes (about 1,200 to 1,800 words at the ElevenLabs pace) unless the scan shows the niche rewards shorter. If a draft lands short, do NOT pad: add another genuine analytical turn (a new figure, a counter-point, a confound) to reach length. Open in the first 10 seconds with the payoff or stakes and the thumbnail's promise; no logo intro. Write for the ear: short declarative sentences, numbers spelled for reading aloud, pauses marked with ElevenLabs break tags. Every on-screen figure traces to a fact-sheet ID. Open a loop early, pay it off, end pointing to the next video. Re-hook roughly every 60 to 90 seconds with a genuine turn in the argument: a new piece of evidence, a counter-point, a number that complicates the thesis. These are analytical turns, never clickbait teases or hype; the re-hook earns attention by advancing the case, in keeping with the KiqIQ anti-hype constitution. (Source: competitor technique review, logged in RUNBOOK.) Run the writing-tells sweep, then save to working-doc section 6 and `<slug>/script/`.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run **kiqiq-art-director** — input: the same player.

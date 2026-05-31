---
name: kiqiq-angle-strategist
description: Choose the counterintuitive thesis and the art style for a player video. Triggers: pick the angle, what's the thesis, decide the art style.
---

# KiqIQ angle strategist

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude chooses the thesis and art style. SOP Role 2.

Read the locked fact sheet, working-doc section 1, `Videos/_context/ANGLE-STYLE-MAP.md` and `ART-STYLE-GUIDE.md`. Pick one counterintuitive, falsifiable thesis carried by two or three thesis-critical figures, beating the competitive gap. Set the angle cluster, then the ART ERA (the primary style driver, from ART-STYLE-GUIDE.md) and the single art style line for the whole video, then the harmonising chart preset (one of: data_native, blueprint, engraving, deco, faded, pop). Write working-doc sections 3 and 4. Do not overclaim causation: if the spine is a single-provider counting-stat trend (a stat falling over time), name the obvious confound (age, a deeper role, team dominance, fewer minutes) and address it on screen, and prefer a thesis with at least one Tier 1 or Tier 2 anchor figure or a descriptive framing ('the numbers were always modest and fell away') over a causal claim ('proof the job was never about X'). This is GATE 1: present the angle for David's approval before downstream steps.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run after David approves the angle (gate 1), **kiqiq-chart-builder** — input: the same player. Then kiqiq-scriptwriter and kiqiq-art-director can also run.

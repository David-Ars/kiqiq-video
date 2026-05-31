---
name: kiqiq-archivist
description: Check and report the KiqIQ API-Football archive. Use when David asks about the data pull, archive status, or what football data has been downloaded.
---

# KiqIQ data archivist

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude reports on the API-Football archive feeding the channel.

Read `Videos/_context/API-FOOTBALL-ARCHIVE.md`. List `Videos/_data/apifootball/`, report file counts and which leagues/seasons have landed (read the `parameters` field in sample JSONs). The pull runs on David's PC via a scheduled task; the sandbox cannot reach the API. Flag if it looks stalled.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run **kiqiq-competitive-analyst** — input: the player name.

---
name: kiqiq-researcher
description: The full research role for a player or team. Maps existing YouTube coverage to find the open angle (leads only), then builds the logged, verified fact sheet. Triggers: research [player], competitive scan, what's been done on [player], find the gap, verify the stats, build the fact sheet.
---

# KiqIQ researcher (scan + verified fact sheet)

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude does the full research stage: the competitive scan, then the verified fact sheet. SOP Role 1. This is the two parts of research in one role, with a hard firewall between them: scan output is leads only and never becomes a fact on the sheet.

**Part A, competitive scan (leads only).** Map the YouTube landscape for the subject via the Claude in Chrome extension: titles, thumbnails, view and like counts, chapters, top comments. Record the REAL channel name, view count and URL for each row from the live page. To read a rival's transcript, open the video in a controlled tab and use its transcript panel (no audio download). For niche-trend and idea signal, also drive David's FREE VidIQ web account through Chrome (the chosen route, NOT the paid VidIQ MCP); treat all VidIQ output as leads only. Copy no wording or structure. If Claude in Chrome is not connected, do NOT invent rows: label section 1 'approximate, from prior knowledge, not a live scan' and flag the gap claim as unverified until a live scan runs. Fill working-doc section 1: the table, saturated angles to avoid, the open gap to own, and the length of strong performers. Save captures to `<slug>/leads/`.

**Part B, verified fact sheet.** Copy `Videos/_system/templates/fact-sheet-template.md` into the episode as `fact-sheet.md`. Log every figure with value, scope, source tier, URL, access date and confidence. Pull candidates from the archive with `_system/archive_query.py` (commands: coverage, find, player, leaderboard, scorers, standings; archive is Tier 3) and from free sources (FBref, Transfermarkt, Understat, official league/club, FIFA, UEFA). Cross-check contested numbers to the highest tier; confirm thesis-critical figures against Tier 1 or 2. Where a metric did not exist in the era, say so; never invent precision. CAREER TOTALS (appearances, goals, cards, minutes) come from FBref or Transfermarkt full career as the LOCKED figure; the API-Football archive is era-limited (2010-2022) and must NEVER be presented as a career total, use it only for per-season event detail (tackles, interceptions, fouls drawn, ratings) it uniquely covers. Any 'never', 'zero' or 'only' superlative (e.g. 'never sent off', 'zero red cards') must be cross-checked career-wide against FBref/Transfermarkt before it becomes a claim; if it is only true for a partial window, scope it explicitly on screen or drop it. State the exact scope (e.g. 'La Liga, 2010-2023') on every appearance/card figure. For honours/trophy counts, prefer the official club or federation tally over fan-aggregated totals (counts often differ, e.g. 32 vs 33); if contested, log both and prefer leading with the uncontested per-competition breakdown over a bare total. Lock the sheet.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run **kiqiq-produce** — input: the same subject. kiqiq-produce is an independent second pass that fact-checks this compiled fact sheet, then builds the rest of the video.

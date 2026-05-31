# KiqIQ video SOP, role by role

Each video moves through roles in order. You open a fresh Cowork chat per role, paste that role's kickoff prompt, and the chat reads only the files that role needs. Every role works inside one episode folder: `Videos/output/<player-slug>/`.

## Default operation (automation)

By default Claude runs these roles in sequence and you approve at two gates only: the angle/thesis, and the final cut before upload. See `AUTOMATION-AND-ACCESS.md` for who runs what and the accesses to set up. Run roles as separate chats only if you prefer to drive them one at a time. The role sections below still define each job, its files and its output.

## The ask-first rule (every role)

A role chat must never assume which player or file you mean. The first action of every role is:

1. List the contents of that role's folder (named under "Confirm first" in each role below).
2. Ask you which file or episode you are referring to.
3. If it is a new player, create the episode folder by copying `Videos/output/_EPISODE-TEMPLATE/` to `Videos/output/<player-slug>/`.
4. Only then start the work.

## Before any role (read once)

Every role reads:
- `Videos/_context/VIDEO-CHANNEL-BRIEF.md` (the channel, the three hard rules, the decided settings)
- `Videos/_context/PRODUCTION-FLOW.md` (the full pipeline this SOP splits into roles)
- `CLAUDE.md` at the project root

Every role that writes text also reads `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md` and applies it. That folder is separate from this project, so connect it in the chat if needed.

The three hard rules apply to every role: verify and log every stat with its source and flag league-only vs all-competitions; competitor videos are leads only, never facts and never copied; AI imagery is a stylized original by attributes, never a face clone, plain kit, no logos.

The shared episode files are `working-doc.md` and `fact-sheet.md`, copied from `Videos/_system/templates/`. Each role fills only its own sections and leaves the rest intact.

Per-episode folders inside `Videos/output/<slug>/`: `leads/` (competitor captures), `research/` (source captures), `charts/`, `art/`, `script/`, `thumbnails/`.

---

## Role 0. Data archivist (ops, runs until 10 June 2026)

- Purpose: pull the API-Football archive locally before access ends.
- Confirm first: list `Videos/_data/apifootball/` and report what has landed, then proceed.
- Reads: `Videos/_context/API-FOOTBALL-ARCHIVE.md`, `Videos/_system/apifootball_archive.py`.
- Output: JSON in `Videos/_data/apifootball/`.
- Kickoff prompt: "You are the KiqIQ data archivist. First list Videos/_data/apifootball/ and tell me what has been pulled so far. Then read Videos/_context/API-FOOTBALL-ARCHIVE.md and confirm today's run."

## Role 1. Research (competitive scan + verified fact sheet)

- Purpose: the full research stage in one role. Part A maps existing YouTube coverage to find the open angle (leads only, never facts, never copied). Part B builds the logged, verified fact sheet. A hard firewall sits between them: scan output never becomes a fact on the sheet.
- Confirm first: list `Videos/output/` and ask which player or team. Create the episode folder from the template if new.
- Reads: PRODUCTION-FLOW steps 2-3, `Videos/_system/templates/fact-sheet-template.md`, the evidence hierarchy in the brief, the archive at `Videos/_data/apifootball/`. Tool: the Claude in Chrome extension reads YouTube (open a rival video in a controlled tab and use its transcript panel; no audio download) and drives David's free VidIQ web account for niche trends and idea signal (free account via Chrome, not the paid VidIQ MCP).
- Steps: Part A, fill working-doc section 1 with the real channel/views/URL table, saturated angles to avoid, the open gap to own, and strong-performer length; leads only, copy no wording or structure. Part B, build `fact-sheet.md`: log every figure with value, scope, source tier, URL, access date, confidence; flag league-only vs all-competitions; cross-check contested numbers to the highest tier; archive is Tier 3, cross-check thesis-critical numbers against Tier 1 or 2; career totals come from FBref/Transfermarkt (the archive is era-limited and is never a career total); verify any never/zero/only superlative career-wide; state exact scope on every appearance/card figure. Lock the sheet.
- Output: working-doc section 1, locked `<slug>/fact-sheet.md`, captures in `<slug>/leads/`.
- Kickoff prompt: "You are KiqIQ research. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 1) and run both parts: the Chrome competitive scan into working-doc section 1 (leads only, no facts), then the verified fact-sheet.md. Verify and log everything."

## Role 2. Angle strategist

- Purpose: choose the counterintuitive thesis and the art style it dictates.
- Confirm first: list `Videos/output/` and ask which player or team, then open that episode's working-doc and fact-sheet.
- Reads: `Videos/_context/ANGLE-STYLE-MAP.md`, `Videos/_context/ART-STYLE-GUIDE.md`, the locked fact sheet, working-doc section 1.
- Output: working-doc sections 3 and 4.
- Kickoff prompt: "You are the KiqIQ angle strategist. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 2), the angle-style map and the art-style guide, and fill sections 3 and 4."

## Role 3. Chart builder

- Purpose: build the data charts.
- Confirm first: list `Videos/output/` and ask which player or team, then work in that episode's `charts/`.
- Reads: `Videos/_system/example_charts.py`, `Videos/_system/brand.py`, the angle-style map, the locked fact sheet.
- Steps: set the chosen preset, build each chart from fact-sheet figures only. Simple charts are live `bar`/`stat` Remotion scenes (numbers go straight into the episode props), not PNGs; use matplotlib (example_charts.py) only for genuinely complex or static charts placed as `image` scenes; use a D3 Remotion scene for richer data stories (bar-race, draw-on line, pass/heat map, node diagram).
- Output: chart inputs in the episode props (plus any matplotlib PNGs in `<slug>/charts/`), working-doc section 5 filled.
- Kickoff prompt: "You are the KiqIQ chart builder. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 3), copy example_charts.py into that episode's charts/, set the preset from the working doc, and build the charts."

## Role 4. Scriptwriter (ElevenLabs)

- Purpose: write the narration script.
- Confirm first: list `Videos/output/` and ask which player or team, then open that episode's working-doc and fact-sheet.
- Reads: working-doc section 6, the locked fact sheet, `AI-WRITING-TELLS.md`, the brief.
- Steps: hook in the first 10 seconds, write for the ear, every figure traces to a fact-sheet ID, re-hook every 60 to 90 seconds with a genuine analytical turn (never a clickbait tease), run the writing-tells sweep.
- Output: script in working-doc section 6 and `<slug>/script/`.
- Kickoff prompt: "You are the KiqIQ scriptwriter. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 4) and AI-WRITING-TELLS.md, and draft the script. Hook in the first 10 seconds."

## Role 5. Art director (Gemini imagery)

- Purpose: generate the stylized player imagery, consistent across shots.
- Confirm first: list `Videos/output/` and ask which player or team, then work in that episode's `art/` and check `Videos/input/reference-art/`.
- Reads: `Videos/_context/ART-STYLE-GUIDE.md`, `Videos/_context/AI-SAFEGUARDS-CHECKLIST.md`, working-doc sections 4 and 8.
- Steps: generate one hero reference render, lock it, derive every other shot with image-to-image, one style for the whole video. Stylized original, never a face clone, plain kit, no logos. Inpaint out the visible Gemini/nano-banana watermark seamlessly (content-aware fill, not a crop), checked at 100% zoom so it is not noticeable; SynthID stays embedded and the YouTube AI disclosure still applies.
- Output: renders in `<slug>/art/`, references in `Videos/input/reference-art/`.
- Kickoff prompt: "You are the KiqIQ art director. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 5) and the art-style guide, generate the locked reference, then derive the shots. One style for the whole video."

## Role 6. Shot planner and editor

- Purpose: turn script, charts and art into a shot list and motion plan, plus Shorts cuts.
- Confirm first: list `Videos/output/` and ask which player or team, then open that episode's working-doc, charts/ and art/.
- Reads: working-doc section 7, the script, `<slug>/charts/`, `<slug>/art/`.
- Steps: map each line to a visual, set on-screen text, and the motion. Motion typography is the main device: number count-ups, chart draw-ons, kinetic hook text, one move per beat (see PRODUCTION-FLOW, Motion and typography). Time each scene's duration to where its line falls in the rendered narration mp3 so count-ups land on the spoken number. Write a one-line still mock-up per scene to confirm the look before the heavy local render. Use the motion-path-from-a-drawn-line trick for traced movement and flag transparent (alpha) scenes for charts/title cards that sit over art. Plan a reveal as the pattern interrupt. No real footage. Write the Remotion episode props at `_system/remotion/episodes/<slug>.json` (scene types title, bar, stat, image). Mark Shorts cut points with hooks.
- Output: working-doc section 7 shot table.
- Kickoff prompt: "You are the KiqIQ shot planner. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 6) and build the shot list in section 7."

## Role 7. Packager

- Purpose: titles, thumbnail, description, tags, chapters.
- Confirm first: list `Videos/output/` and ask which player or team, then work in that episode's `thumbnails/`.
- Reads: `Videos/_system/thumb.py`, working-doc section 9, the packaging notes in PRODUCTION-FLOW.
- Steps: title states the promise; thumbnail shows the proof in 3 to 4 words, never duplicating the title. Build with thumb.py using the episode preset and the locked art. Check at the 120px preview. For title and tag signal, Claude in Chrome may consult David's free VidIQ web account (leads only); never let it pull the analytical spine off-strategy.
- Output: thumbnails in `<slug>/thumbnails/`, working-doc section 9 filled.
- Kickoff prompt: "You are the KiqIQ packager. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 7) and produce titles and the thumbnail in section 9."

## Role 8. Publisher and QC

- Purpose: final check, disclosure, upload, and the growth set-up.
- Confirm first: list `Videos/output/` and ask which player or team, then open that episode's working-doc section 10.
- Reads: `Videos/_context/AI-SAFEGUARDS-CHECKLIST.md`, working-doc section 10.
- Steps: run the pre-upload QC and the AI-safeguards checklist. Tick YouTube's synthetic-content box if any image could read as realistic. Confirm every figure traces to a fact-sheet ID and no real footage was used. Then set up the growth items in Studio via Chrome: upload an accurate `.srt` built from the script and its timings (`<slug>/script/<slug>.srt`); add an end screen over the last ~20s (subscribe + next-video/playlist); load the packager's 2-3 thumbnails into Test & Compare; add the video to the right thematic playlist; and a few days later pull the retention curve and write the drop-off lessons into working-doc section 10 for the scriptwriter.
- Output: published video, working-doc section 10 ticked.
- Kickoff prompt: "You are the KiqIQ publisher. First list Videos/output/ and ask me which player or team. Then read Videos/_context/SOP-ROLES.md (Role 8), run the QC and AI-safeguards checklist, set up subtitles, end screen, thumbnail A/B test and playlist, and confirm the episode is ready."

---

## Order and handoff

archivist (ongoing) -> research (scan + fact sheet) -> angle strategist -> chart builder and scriptwriter and art director (parallel) -> shot planner -> packager -> publisher.

The working doc and fact sheet carry the episode between roles.

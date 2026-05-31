# KiqIQ video runbook (start to finish)

How one video gets made. Default mode is hands-off: Claude runs the steps and you approve at two gates. You can instead run any step as its own chat using the kickoff prompts.

Where the roles live:
- Full role definitions: `_context/SOP-ROLES.md`
- Copy-paste prompts (one per role): `_context/ROLE-KICKOFF-PROMPTS.md`
- Who runs what and why: `_context/AUTOMATION-AND-ACCESS.md`
- The pipeline in prose: `_context/PRODUCTION-FLOW.md`

One-time setup (done): folders, chart and thumbnail engine, Inter fonts, logo, API-Football daily task, ElevenLabs key, Chrome connected.

## Per-video steps

| # | Step | Role (where to find it) | Who runs it | Output |
|---|------|--------------------------|-------------|--------|
| 0 | Pick the subject (player or team) and a one-line hunch | Pick (PRODUCTION-FLOW step 1) | YOU (or ask Claude to pick from the backlog) | the player |
| 1 | Create the episode folder from the template | (automation) | Claude | `output/<slug>/` |
| 2 | Competitive scan on YouTube, find the gap | Research part A (kiqiq-researcher), SOP Role 1 | Claude, via Claude in Chrome | working-doc section 1 |
| 3 | Build the verified fact sheet | Research part B (kiqiq-researcher), SOP Role 1 | Claude, from the archive + web | `fact-sheet.md` |
| 4 | Choose the counterintuitive thesis | Angle strategist, SOP Role 3 | Claude proposes. GATE 1: YOU approve | working-doc sections 3, 4 |
| 5 | Lock the art style (angle decides it) | Angle strategist + ANGLE-STYLE-MAP / ART-STYLE-GUIDE | Claude | working-doc section 4 |
| 6 | Build the data charts | Chart builder, SOP Role 4 | Claude | `charts/` |
| 7 | Write the narration script | Scriptwriter, SOP Role 5 | Claude, AI-tells swept | working-doc section 6, `script/` |
| 8 | Render the narration audio | (tts.py) | `python tts.py script.txt` on your PC (sandbox cannot reach ElevenLabs) | `script/*.mp3` |
| 9 | Generate the stylized imagery | Art director, SOP Role 6 | Claude, via the Gemini tool | `art/` |
| 10 | Plan shots and motion typography | Shot planner, SOP Role 7 | Claude | working-doc section 7 |
| 11 | Assemble the video (animated charts + motion text + narration) | `_system/remotion` (Remotion). `assemble_video.py` is the no-deps fallback | Claude builds the scene props, you render on your PC | `_system/remotion/out/<slug>.mp4` |
| 12 | Thumbnail, title, description, tags | Packager, SOP Role 7 | Claude | `thumbnails/`, working-doc section 9 |
| 13 | Review the final cut | (final review) | GATE 2: YOU approve | go / no-go |
| 14 | Upload, AI disclosure, subtitles, end screen, thumbnail A/B, playlist | Publisher, SOP Role 8 | Claude drives YouTube Studio in Chrome. YOU confirm publish | published video |

Ongoing in the background: the archivist (SOP Role 0) keeps pulling API-Football data daily until 10 June.

## Your total involvement per video

Pick the player. Approve the angle (gate 1). Run one tts command. Approve the final cut (gate 2). Confirm publish. Nothing else.

## Two ways to run it

1. Recommended two-stage: first run **kiqiq-researcher** for the subject and review its fact sheet. Then run **kiqiq-produce**, which independently fact-checks that sheet (re-verifying the numbers from primary sources) before it builds the scan, angle, charts, script, art and cut, pausing at the two gates.
2. Per-role chats: open a new chat per step and paste that role's prompt from `ROLE-KICKOFF-PROMPTS.md`. Each role asks which player first.

## Step 11 assembler usage

Primary: Remotion (`_system/remotion`). Charts are live animated components, plus count-ups, kinetic text and Ken Burns. Setup once: `cd _system/remotion && npm install`. Preview and tweak (gate 2): `npx remotion studio`. Render: `npx remotion render KiqIQVideo out\<slug>.mp4 --props=episodes\<slug>.json`. The shot planner writes `episodes/<slug>.json`. See `_system/remotion/README.md`.

Fallback (no dependencies): the ffmpeg script below.

`python assemble_video.py <episode_dir>`. It reads `<slug>/shotlist.json` (or auto-builds shots from `charts/*.png`), applies Ken Burns motion, burns in on-screen text in Inter, and lays the first mp3 in `script/` over the top.

## Competitor technique review (2026-05-31)

Read the full transcripts of the leading "Claude + Remotion" / AI-video tutorials (Andy Lo, the Scalable Creator OS "what-if history" build, the four-phase "train Claude to edit" video, Matt Par / Higgsfield, the VidIQ-MCP walkthrough, the three-levels skill-stacking video, and the Claude Design one). Most of what they teach we already do: Remotion as the motion layer, ElevenLabs narration, live animated charts, count-ups / kinetic text, Ken Burns, AI imagery, a Chrome-driven workflow, CLAUDE.md as a persistent brain, and prompt-to-iterate loops.

Adopted (wired into the skills/tools):

- **Audio loudness normalization.** Several channels pay for Auphonic. `tts.py` now runs every render through ffmpeg `loudnorm` to -14 LUFS for free (YouTube's normalization target, so we play level with rivals; `--raw` to skip; no-op if ffmpeg absent).
- **Zod schema on the Remotion composition.** `_system/remotion/src/schema.ts` is now the single source of truth for episode props; Root.tsx passes it as `schema`, so Remotion Studio shows editable controls at gate 2 and rejects malformed episode JSON instead of rendering a broken video. The example episode validates. Run `npm install` locally once (pulls `zod`) then `npx remotion studio` to confirm on your PC.
- **D3 for advanced animated charts** (Andy Lo). When a basic bar/stat scene cannot tell the data story, build a D3 Remotion scene (bar-race, draw-on line, pass/heat map, node diagram). Added to **kiqiq-chart-builder**. "The data is the content" fits KiqIQ exactly.
- **Time scenes to the narration audio** (four-phase video). The shot planner now sets each scene's duration from where its line falls in the rendered mp3, so count-ups land on the spoken number. Added to **kiqiq-shot-planner**.
- **Mock up before the heavy render** (four-phase video). The shot planner now writes a one-line still description per scene to confirm the look cheaply before the local Remotion render — a cheap design gate ahead of gate 2. Added to **kiqiq-shot-planner**.
- **Motion-path-from-a-drawn-line** and **transparent (alpha) scene rendering** (Andy Lo's tips). Both added to **kiqiq-shot-planner** for traced movement and for compositing charts/title cards over stylized art.
- **Analytical re-hook cadence** (Matt Par's hook/rehook structure, de-clickbaited). The scriptwriter now turns the argument every ~60-90s with new evidence or a counter-point — never a hype tease. Added to **kiqiq-scriptwriter**.

- **VidIQ via the free web account, driven by Claude in Chrome** (not the paid MCP). David has a free VidIQ account (150 AI credits/month: niche trends, data-backed ideas, AI coach). The competitive analyst and packager now use it through the browser for trend and title/tag signal, leads only. Rival transcripts come from each video's YouTube transcript panel opened in a controlled tab (no audio download), which also removes the need to paste transcripts manually. Wired into kiqiq-competitive-analyst, kiqiq-packager, PRODUCTION-FLOW, SOP-ROLES and AUTOMATION-AND-ACCESS.

Also adopted (2026-05-31, second pass):

- **Music bed per art style + SFX (shipped).** One original, KiqIQ-owned, licence-free ambient bed per chart preset lives in `public/` (`music_<preset>.mp3`: data_native, blueprint, engraving, deco, faded, pop), each a 40s seamless loop tuned to that preset's mood. The composition auto-selects the bed from the episode `preset` and loops it at `musicVolume` (default 0.12; set 0 to silence). Plus `sfx_tick.mp3` and `sfx_whoosh.mp3` for count-up lands and reveals. All generated in-house; swap any file to use your own.
- **Native KiqIQ logo sting.** A `sting` scene type plus `components/LogoSting.tsx` animate the wordmark (no Lottie dependency). Open and close with one. Swap the wordmark for the logo image once it's in `public/`.
- **Audio at -14 LUFS.** `tts.py` now targets YouTube's normalization level so we play level with rivals.
- **Research role merged.** kiqiq-competitive-analyst folded into kiqiq-researcher (scan = Part A, fact sheet = Part B); downstream SOP roles renumbered to 1-8.
- **YouTube growth set-up** added to the publisher: subtitles (.srt), end screen, thumbnail A/B test, playlists, post-publish retention loop. (Pinned-source comment intentionally NOT added, per David.)

Could add but did not (your call):
- **Parallel generation sessions** (the what-if-history build ran three videos at once). Would raise throughput for the weekly cadence, but one accurate episode at a time matches our accuracy-first discipline; revisit only if the backlog grows.
- **claude.md self-updating "brain"** (the three-levels video appends learnings to CLAUDE.md automatically). We already keep CLAUDE.md plus the _skills set plus persistent memory; an auto-append rule risks drift, so left manual.
- **Lottie logo sting and vanilla three.js 3D moments** (Andy Lo). Noted in the Remotion README as optional; not core to data essays, so not wired into the default flow.
- **Pinterest-style inspiration gathering and an auto-built brand style guide** (Claude Design / four-phase videos). Our art system (ANGLE-STYLE-MAP, ART-STYLE-GUIDE, the six presets) is already locked, so this would only add noise.

Deliberately rejected as off-strategy for KiqIQ: AI-generated video footage (Higgsfield / Seedance / Kling / Key.ai-fal) — we are footage-free by design and built on charts + stylized stills, and these models are a recurring cost for moving b-roll we do not want; silence-trimming / best-take selection with Whisper (we narrate from a written script, there is no raw take); Hyperframes and Claude Design (we chose Remotion); Framer Motion / React Three Fiber (interactive/abstraction layers that fight Remotion's deterministic frames — prefer vanilla three.js if we ever need 3D); and auto-post-to-social (publishing stays a human gate).
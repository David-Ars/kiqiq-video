# KiqIQ video production flow

Footage-free, data-driven player and team essays. Visuals are charts built from verified stats and stylized AI imagery of the player. Motion comes from editing over stills. No real match footage at any point. The channel edge is accuracy and analytical insight, not borrowed clips.

This doc is the per-video pipeline. Copy the episode template, then work top to bottom.

## The pipeline

### 1. Pick
You choose the subject (a player or a team) and a one-line hunch. The hunch is a hypothesis to test against the data, not a conclusion to defend.

### 2. Competitive scan (leads only)
Map what already exists on YouTube for this player: angles, saturation, what performs, how long the strong videos run. This is a leads source only. It is never a source of facts, and the wording and structure of the script never model a competitor video.

You run this with the Claude in Chrome extension: it opens YouTube and reads titles, thumbnails, view and like counts, chapters, top comments and native transcripts directly. To read a rival's transcript, open the video in a controlled tab and use its transcript panel; do not download audio, which keeps it clear of YouTube's terms and avoids absorbing a competitor's structure. For trend and idea signal, Claude in Chrome also drives David's free VidIQ web account (150 AI credits/month: niche trends, data-backed content ideas, AI-coach tips) rather than the paid VidIQ MCP. Treat VidIQ output as leads only, never as facts. Capture notes go in the episode `leads/` folder.

### 3. Research and verify
Build the fact sheet. Every figure logged with value, scope, source tier, URL, access date and confidence. League-only versus all-competitions stated every time. Contested numbers cross-checked and resolved to the highest-tier source. Where a metric did not exist in the player's era, the sheet says so and the script acknowledges the gap rather than inventing precision. See the fact-sheet template and the KiqIQ evidence hierarchy.

### 4. Angle and thesis
Propose a distinct thesis built on the research and the competitive gap. One counterintuitive, falsifiable claim, carried by two or three thesis-critical figures.

### 5. Art style (decided by the angle)
The angle sets the style. Look it up in `ANGLE-STYLE-MAP.md`, which fixes the chart preset and the one art style line used for every render in the video.

### 6. Charts, script, production
Copy `_system/example_charts.py`, set the preset, build the charts from fact-sheet figures. Write the script for AI text-to-speech. Plan the shot list. Generate the AI art from the locked references. Package and run pre-upload QC.

## Motion and typography

No footage means motion has to come from somewhere, and typography is the answer. It is the channel's main motion device, not decoration.

Use, kept clean and analytical, never flashy:
- Number count-ups on hero stats (the figure ticks up to its value).
- Chart draw-on reveals: bars grow, lines draw, dots land. Simple data goes in live `bar`/`stat` Remotion scenes; richer data stories (a bar-race over seasons, a draw-on line, a pass or heat map, a node diagram) use a D3-driven scene, since for KiqIQ the data is the content.
- Kinetic text on the hook and each key claim: a short slide or fade as the line is spoken. One move per beat, not constant motion.
- Source lines and lower-thirds animate in under the figure they support.
- A reveal on a regular beat doubles as the retention pattern interrupt.

Scene craft (from the competitor technique review, logged in RUNBOOK):
- Time each scene to the narration: set durations from where the line actually falls in the rendered mp3, so a count-up lands on the spoken number.
- Mock up before the heavy render: a one-line still description per scene confirms the look cheaply before the local Remotion render (a cheap design gate ahead of gate 2).
- Use the motion-path-from-a-drawn-line trick for any traced movement (a run, a pass), and render charts or title cards that sit over stylized art as transparent (alpha) scenes so they composite cleanly.

Engine: Remotion (React to video) at `_system/remotion`, which renders animated charts, count-ups, kinetic text and Ken Burns to MP4 from an episode's scene props. It reads the same six brand presets as brand.py. The ffmpeg `assemble_video.py` remains a no-dependency fallback. Both run on David's PC.

Restraint rule: the motion serves comprehension. If an animation does not help the viewer read the data faster, cut it.

## Hard rules (enforced every video)

1. Every stat is verified against reliable primary sources and logged with its source. Flag league-only versus all-competitions. Cross-check contested numbers. Note where data does not exist for the era rather than inventing precision.
2. Other YouTube videos are a leads source only. Never a source of facts. Never copied in script wording or structure.
3. Player imagery shows the figure with an abstract, non-literal face (identity via build, hair, posture, kit colours, era, context, never an exact face or the name). Team imagery uses no single face and no real crest or sponsor logo. Editorial and analytical use, plain kits.

## Narration: ElevenLabs text-to-speech

- Script craft: write for the ear and for the engine. Short declarative sentences. Numbers and abbreviations spelled the way they should be read. Pauses set with ElevenLabs break tags and punctuation. A natural-sounding read depends more on the script than the voice. Re-hook roughly every 60 to 90 seconds with a genuine turn in the argument (new evidence, a counter-point, a number that complicates the thesis), never a clickbait tease, in keeping with the anti-hype constitution.
- Audio polish: `tts.py` loudness-normalises every render to -14 LUFS via ffmpeg (YouTube's normalization target, the free Auphonic equivalent), so episodes play at the same level as rivals. `--raw` skips it.
- Monetization risk: a channel of AI voice plus AI imagery plus no footage sits in the zone YouTube scrutinises for inauthentic or mass-produced content. The defence is heavy original analysis, verified data with every figure sourced on the fact sheet, a consistent point of view, and clear value beyond narration of public facts. Keep the analytical density high. This is a flag, not a blocker.

Channel voice: ElevenLabs "George" (warm, mature British documentary narrator), locked as the single narrator across episodes. Audition in the ElevenLabs library and swap only if it does not fit. Suggested settings: stability ~50, similarity ~80, style low, speaker boost on, model eleven_multilingual_v2.

## Character consistency across shots

The unsolved-by-default problem in this format. Proposed method, to confirm:

1. Generate one hero reference render of the stylized player in the video's art style. Iterate until right. This is the canonical reference.
2. Lock 1 to 2 references (for example a front and a three-quarter view).
3. Generate every later shot from those references using image-to-image or reference-conditioned generation, holding the style line and seed discipline constant, varying only pose, crop and composition.
4. Run a consistency check before the edit: same face structure, same kit, same palette across all shots.

Generator: Gemini, confirmed. One hero reference render, then image-to-image for every other shot, holding the style line constant.

Likeness: players are shown as a recognisable figure with an abstract, non-literal face. Identity reads from build, hair, posture, kit colours, era and context, not from facial detail, and the prompt never uses the player's name. Teams have no single face. This keeps publicity-rights exposure low.

## Data sources

Two sources, in this order.

1. The local API-Football archive. We are pulling as much API-Football data as possible into a local store now, before access ends. This becomes the fast, offline dataset for player season stats, fixtures and squad data, which is what makes a weekly cadence possible without live calls. API-Football is a third-party aggregator, so it sits at Tier 3 on the evidence hierarchy. Use it freely for chart inputs, but any thesis-critical figure still gets cross-checked against a Tier 1 or Tier 2 source on the fact sheet.
2. Free, 100% verified data only, after that. FBref, Transfermarkt, Understat, official league and club records, FIFA and UEFA, read and cited by hand. No paid feeds. `mplsoccer` is used only where real event data exists in the archive or a free source.

See `API-FOOTBALL-ARCHIVE.md` for the download plan, scope and rate budget.

## Cadence: weekly

One published video per week. At one person on this pipeline, weekly only works if research and chart building are largely automated, which is the point of the local API-Football archive and the copy-and-edit chart scripts. Time the first episode end to end, then move the slowest manual stage into a template or script. If verification depth ever has to give way to hit the date, the date gives way instead. Accuracy is the channel.

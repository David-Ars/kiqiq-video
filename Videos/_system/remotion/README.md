# KiqIQ Remotion layer (step 11: motion + animated charts)

Turns an episode's scenes into a finished 1920x1080 MP4 with real motion:
count-ups, bars that grow, kinetic text, Ken Burns on stills. Charts are live
animated React components, not static images, and read the KiqIQ brand theme so
they match the rest of the channel. Replaces the ffmpeg `assemble_video.py` for
animated output (that script stays as a no-dependency fallback).

Runs on your machine (Node is installed). The Cowork sandbox cannot render here.

## One-time setup

```
cd "C:\Users\david\Documents\Claude\Projects\KiqIQ\Videos\_system\remotion"
npm install
```

Copy the KiqIQ logo and any narration mp3 / AI art into `public/` (Remotion's
`staticFile()` reads from there).

## Preview and render

```
npx remotion studio
```
Opens the visual studio: timeline, live preview, click-to-edit. This is your
gate-2 tweak surface.

```
npx remotion render KiqIQVideo out\<slug>.mp4 --props=episodes\<slug>.json
```
Renders the MP4. Drop the `--props` flag to render the built-in example.

## How an episode is described

An episode is JSON props: `{ subject, preset, source, audioSrc, scenes[] }`.
`preset` is one of the six brand presets (data_native, blueprint, engraving,
deco, faded, pop). `scenes` play in order; each has a `durationInFrames` (30 fps).

The shape is validated by a Zod schema in `src/schema.ts` (the single source of
truth; the TS prop types are inferred from it). The studio renders editable
controls from it, and a malformed `episodes/<slug>.json` fails loudly instead of
rendering a broken video. After editing the schema, restart the studio.

Scene types:
- `title`  : kinetic headline lines + optional sub.
- `bar`    : animated horizontal bar chart. `data: [{label, value, highlight}]`.
- `stat`   : big count-up numbers in a row. `stats: [{value, label, suffix, highlight}]`.
- `image`  : an AI-art still or any PNG with a slow Ken Burns. `src` is a file in `public/`.
- `sting`  : the native KiqIQ logo bumper (no Lottie). Use one at the open and one at the close.

Audio options:
- music bed   : auto-selected by the episode `preset` — the composition plays `public/music_<preset>.mp3` and loops it to cover the runtime at `musicVolume` (default 0.12). Override with an explicit `music` field, or set `musicVolume: 0` to silence it.
- per-scene `sfx`: optional one-shot (a file in `public/`) played at that scene's start, e.g. a soft tick as a count-up lands or a low whoosh on a reveal. Use sparingly.

`public/` ships with original, KiqIQ-owned, licence-free audio generated for the channel. One ambient bed per art-style preset (each a 40s seamless loop, ~-17 LUFS), tuned to the preset's mood:
- `music_data_native.mp3` cool, modern, neutral-confident
- `music_blueprint.mp3` clinical and measured, with a quiet metronomic pulse
- `music_engraving.mp3` solemn, classical, organ/strings
- `music_deco.mp3` warm golden-age glamour (jazzy maj7)
- `music_faded.mp3` cold, wistful, tape-warble minor
- `music_pop.mp3` bright and celebratory, with a gentle major arpeggio

Plus a neutral `music_bed.mp3` fallback. Swap in your own tracks by replacing any file.

### SFX library (set a scene's `sfx` to one of these)

All original, KiqIQ-owned, licence-free, baked at a level that sits under narration (played at volume 0.6). Map each to the video aspect it serves:

| File | Sound | Use it for |
|---|---|---|
| `sfx_tick.mp3` | soft tick | a count-up number landing on its value |
| `sfx_dot.mp3` | short pop/blip | a data point or dot landing on a chart |
| `sfx_riser.mp3` | rising sweep | bars growing / a chart drawing on |
| `sfx_impact.mp3` | low thud | a big stat slamming in for emphasis |
| `sfx_whoosh.mp3` | airy whoosh | a reveal / pattern interrupt |
| `sfx_swell.mp3` | building noise into a cut | the moment just before a reveal |
| `sfx_transition.mp3` | stereo swoosh | a scene cut / section change |
| `sfx_boom.mp3` | deep sub hit | opening a new section / chapter |
| `sfx_logo_chime.mp3` | brand bell arpeggio | the opening/closing logo sting |
| `sfx_ping.mp3` | bright bell ping | highlighting a key point or callout |
| `sfx_chime_soft.mp3` | gentle single bell | a soft confirm / quiet emphasis |
| `sfx_uplift.mp3` | upward gliss | a positive beat (vindication, triumph) |
| `sfx_downer.mp3` | downward tone | a negative beat (decline, fall-off) |
| `sfx_tension.mp3` | low pulsing hold | a suspense / hold-the-question moment |
| `sfx_type.mp3` | soft key clicks | kinetic text typing on |
| `sfx_click.mp3` | tiny click | a small UI accent / lower-third snap |

Keep SFX sparing — one or two per beat, never on every scene.

See `src/example-episode.json` for a worked placeholder example.

## Where it fits the pipeline

The shot planner writes `episodes/<slug>.json` from the script and the locked
fact-sheet figures (so every animated number traces to a fact-sheet ID). The
chart builder no longer needs to pre-render bar and stat charts as PNGs; those
are now `bar` and `stat` scenes. Use `image` scenes for the stylized AI art and
for any complex chart you still build in matplotlib.

## Scene techniques (from the competitor technique review, logged in RUNBOOK)

- **D3 for richer data stories.** When `bar`/`stat` cannot tell it, build a D3-driven scene: a bar-race over seasons, a line that draws on, a pass or heat map, a node diagram. For KiqIQ the data is the content, so this is the main place to invest. Keep it readable at 120px and trace every number to a fact-sheet ID.
- **Time durations to the narration.** Set each scene's `durationInFrames` from where its line falls in the rendered mp3 (probe the mp3, or use ElevenLabs word timings) so a count-up lands on the spoken number, instead of eyeballing frame counts.
- **Mock up before rendering.** Confirm the look from the one-line still description the shot planner writes per scene before running the local render; renders are the expensive step.
- **Transparent (alpha) output.** For a chart or title card that composites over stylized art, render that scene as a PNG image sequence with alpha rather than a flattened frame.
- **Motion-path trick.** For a traced movement (a run, a pass), hand the build a plain image with the path drawn on it; it traces far more precisely than a worded description.
- If a 3D moment is ever needed, prefer vanilla three.js over React Three Fiber — the abstraction layer can introduce timing drift in Remotion's deterministic frames.

## Brand theme

`src/theme.ts` mirrors `_system/brand.py` presets. Keep them in sync: same six
names, same colours. CONSTANTS (the KiqIQ wordmark, the accent border, the
footer) live in `Frame.tsx` and do not change per video.

## Optional motion libraries (enhancement, not required)

Source: common Claude + Remotion setups (Andy Lo's "Claude Code + Remotion" breakdown; the same adapters HyperFrames lists). Remotion accepts these on top of the base components:

- GSAP: richer easing and timelines for count-ups and kinetic text, beyond spring/interpolate. Use for polish on hero-stat reveals.
- Lottie: vector motion graphics. Use for an animated KiqIQ logo sting and small iconography or scene transitions.
- Three.js: 3D. The natural fit for the "low-poly geometric / the machine" art style and any 3D chart moment.

Keep them optional and restrained, the readability and accuracy rules still win. Add a library only when it earns its place in a specific scene.

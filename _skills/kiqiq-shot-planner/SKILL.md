---
name: kiqiq-shot-planner
description: Turn script, charts and art into a shot list with motion typography and Shorts cuts, and write the shotlist.json the assembler reads. Triggers: plan the shots, build the shot list.
---

# KiqIQ shot planner and editor

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude builds the shot list and motion plan, and the machine-readable shotlist. SOP Role 6.

Read working-doc section 7, the script, `<slug>/charts/` and `<slug>/art/`. Map each script beat to a visual, set on-screen text and the motion. Motion typography is the main device: number count-ups, chart draw-ons, kinetic hook text, one move per beat. Plan a reveal as the pattern interrupt. No real footage. Fill working-doc section 7, and write the Remotion episode props at `_system/remotion/episodes/<slug>.json` ({subject, preset, source, audioSrc, scenes[]}; scene types title, bar, stat, image, sting; durations in frames at 30fps). Open and close with a `sting` (the native KiqIQ logo bumper). The music bed is auto-selected from the episode `preset` (one bundled ambient loop per art-style preset in `public/`), so no `music` field is needed unless you want to override it; keep `musicVolume` ~0.1, or set it to 0 to silence. Add a per-scene `sfx` one-shot from the SFX library in `_system/remotion/README.md` (tick=count-up land, dot=data point, riser=bars grow, impact=stat slam, whoosh=reveal, swell=pre-reveal, transition=scene cut, boom=section open, logo_chime=sting, ping=highlight, chime_soft=soft confirm, uplift=positive beat, downer=decline beat, tension=suspense hold, type=kinetic text, click=UI accent). One or two per beat, never on every scene. Every animated number traces to a fact-sheet ID. This JSON is the ONLY video deliverable. Do NOT build an in-chat ffmpeg preview or matplotlib bar/stat PNGs for the cut; gate-2 review happens in Remotion studio on David's PC (`npx remotion studio`). Only touch `assemble_video.py`/`shotlist.json` if David explicitly asks for the ffmpeg fallback. Mark Shorts cut points.

### Techniques from the competitor review (logged in RUNBOOK)
- **Time scenes to the narration, not to guesses.** The script is already rendered to mp3 by `tts.py` before this step. Set each scene's `durationInFrames` from where its line actually falls in the audio (probe the mp3 length, or use the ElevenLabs word timings if present), so a count-up lands on the number as it is spoken. Do not eyeball durations when the audio exists.
- **Mock up before the heavy render.** In working-doc section 7, give a one-line still description of each scene (layout, on-screen text, the single move) so the look is confirmed cheaply before David runs the local Remotion render at gate 2. This is the cheap design gate that sits before the expensive one.
- **Motion-path trick** for any traced movement (a run, a pass, a trajectory): draw the line on a plain image and hand that to the build rather than describing the curve in words; it traces far more precisely.
- **Transparent scenes** when a chart or title card must sit over stylized art: flag those scenes to render as PNG with alpha (image sequence), not flattened, so they composite cleanly.

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run render the narration (`tts.py` on the script), assemble with Remotion (`_system/remotion`, render the episode props), then **kiqiq-packager** — input: the same player.

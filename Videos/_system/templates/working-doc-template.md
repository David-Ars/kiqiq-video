# Working doc: [SUBJECT NAME]

Episode slug: [player-slug]  ·  Started: [YYYY-MM-DD]  ·  Owner: David

One doc per video. It carries the episode from pick to upload. The fact sheet lives beside it as a separate file.

## 0. Pick

- Subject: [name]   Mode: player or team
- Why now: [reason: anniversary, transfer, resurfaced debate, gap in coverage]
- One-line hunch: [the counterintuitive idea before research, to be tested not assumed]

## 1. Competitive scan (leads only, never facts)

Source for what angles exist and what is saturated. Not a source of figures, and never copied in wording or structure.

| Video | Channel | Views | Age | Angle / thesis | Length | What it does well | Gap it leaves |
|-------|---------|-------|-----|----------------|--------|-------------------|---------------|
|  |  |  |  |  |  |  |  |

- Saturated angles to avoid: [list]
- Open gap we can own: [the angle nobody has done well]
- Length read from top performers: [range, with the videos it came from]

## 2. Research and verification

- Fact sheet: `../fact-sheet-[slug].md` (status: in progress / locked)
- Thesis-critical figures verified: yes / no
- Data gaps acknowledged: [list]

## 3. Angle and thesis (chosen)

- Thesis (one sentence, counterintuitive, falsifiable): [text]
- The figures that prove it: [F-ids from fact sheet]
- Supporting angles, if any: [text]
- Why this over the alternatives: [from the competitive gap]

## 4. Art style (the angle dictates this)

See `_context/ANGLE-STYLE-MAP.md` (player table or team table) and `ART-STYLE-GUIDE.md`.

- Subject mode: player / team
- Angle cluster: [from the matching table]
- Art era / style: [the one style for the whole video]
- Chart preset: [data_native / blueprint / engraving / deco / faded / pop]
- AI art style line: [the fixed descriptor reused for every render]
- Reference images: [paths in art/ folder, 1 to 2 locked refs]

## 5. Charts

| # | Chart | Figures used (F-ids) | Type | Preset | Built |
|---|-------|----------------------|------|--------|-------|
| 01 |  |  |  |  | no |

Built with a copy of `_system/example_charts.py`, `set_preset()` set to the style above. Output to `charts/`.

## 6. Script (written for ElevenLabs text-to-speech)

Target length: [minutes] at roughly 150 wpm gives [word count].

Hook rule: the first 10 seconds open with the payoff or the stakes and deliver the thumbnail's promise. No logo intro, no "welcome back". State an open loop early and pay it off later.

Write for the ear. Short declarative sentences. Spell numbers and abbreviations the way they should be read aloud ("nineteen ninety-eight", "per ninety"). Mark pauses with ElevenLabs break tags and punctuation. Run the AI-WRITING-TELLS pass before locking.

```
[COLD OPEN, 0-10s: payoff or stakes, deliver the thumbnail promise]
...

[SECTION 1]
...
```

- Word count: [n]  ·  AI-tells pass done: no  ·  Original wording confirmed: no

## 7. Shot / visual plan

| Shot | Time | Visual (chart # or art) | On-screen text | Motion (pan/zoom/reveal) | Source line shown |
|------|------|-------------------------|----------------|--------------------------|-------------------|
| 1 |  |  |  |  |  |

Motion comes from editing over stills. No real match footage at any point.

## 8. Character consistency

- Method: [locked reference + img2img variations / seed lock / character sheet]. See production flow doc.
- Hero reference render: [path]
- Per-shot renders derived from it: [count]
- Consistency check passed: no

## 9. Packaging

- Title options: [3 to 5]  (title = the promise)
- Thumbnail: hero stat [value], label [text], title 3 to 4 words, built with `_system/thumb.py`. Title shows the proof, never duplicates the video title.
- Description: [text]
- Tags: [list]
- Chapters: [list]

## 10. Pre-upload QC

- [ ] Every on-screen figure traces to a locked fact-sheet ID
- [ ] League-only vs all-comps stated wherever relevant
- [ ] Contested numbers resolved and sourced
- [ ] No real footage used
- [ ] AI art is attribute-based, plain kit, no logos or sponsor marks
- [ ] Script passes the AI-WRITING-TELLS sweep
- [ ] Wording and structure original, not modelled on a competitor video
- [ ] Channel mark, footer and frame present and unchanged
- [ ] Passes the AI-safeguards checklist (`_context/AI-SAFEGUARDS-CHECKLIST.md`)

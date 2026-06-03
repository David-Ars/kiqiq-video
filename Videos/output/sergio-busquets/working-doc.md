# Working doc: Sergio Busquets

Episode slug: sergio-busquets  ·  Started: 2026-06-02  ·  Owner: David

One doc per video. It carries the episode from pick to upload. The fact sheet lives beside it as a separate file.

## 0. Pick

- Subject: Sergio Busquets   Mode: player
- Why now: retired from football in December 2025 (final appearance 6 Dec 2025 for Inter Miami), so the full career is now closed and countable. A clean moment to settle what the numbers actually say about him.
- One-line hunch: the player every essay calls a genius is the one the box score makes look idle, and the real proof of his value is in the things the highlight reel cannot show. To be tested, not assumed.

## 1. Competitive scan (leads only, never facts)

Live scan via Claude in Chrome on youtube.com, 2026-06-02. Queries: "Sergio Busquets", "Sergio Busquets tactical analysis", "why Busquets was irreplaceable Barcelona stats". Channel names, view counts and URLs read from the live result pages. Leads only, no wording or structure copied.

| Video | Channel | Views | Age | Angle / thesis | Length | What it does well | Gap it leaves |
|-------|---------|-------|-----|----------------|--------|-------------------|---------------|
| The Barcelona 'Pivot' - How Busquets mastered football's hardest role (youtube.com/watch?v=lEmz3dGqe24) | The Purist Football (verified) | 2.4m | 2 yr | Positional essay: the pivot role, Cruyff lineage, Guardiola system | 10:58 | Best-produced analytical essay; chapters Cruyff's vision / Guardiola paradox / the heir / genius / more than a position; cites FBref | Story of the role, not a built-from-data case. Charts are illustrative, not the spine |
| How Sergio Busquets Tricked EVERYONE Into Thinking He Doesn't Do Anything (youtube.com/watch?v=gRovQdZ6IHw) | Raymar Football (verified) | 1.3m | 2 yr | "Invisible work" biographical narrative | 10:17 | Closest to the invisible-value angle; strong hook and title | Biography chapters (childhood, golden generation), not a verified stat profile. Claims the invisibility, never quantifies it |
| Learn to Play Center Mid: A Pro's Analysis of Busquets (youtube.com/watch?v=21Kwovy2gws) | Become Elite (verified) | 1.9m | 8 yr | Coaching tutorial, off-ball positioning | 7:42 | Practical, ex-pro breakdown of positioning | Instructional, not an essay; no career data |
| The Genius of Sergio Busquets (youtube.com/watch?v=m_OS1ki3qX0) | JTQBR | 123k | 2 yr | Short "genius" essay, QB analogy | 6:48 | Accessible framing | Thin; no verified figures |
| Sergio Busquets: When Football Becomes Art (youtube.com/watch?v=umYwNBp65WY) | AJcompsHD | 365k | 11 mo | Tribute / highlight compilation | 22:00 | Long-form montage, music led | Pure footage, no analysis |
| Sergio Busquets Skills, The Genius of Simplicity (youtube.com/watch?v=shee2rLaoq4) | Soccer World | 1.2m | 2 yr | Skills compilation | 5:11 | High views, clean cuts | Footage only |
| Sergio Busquets, Absolute Genius, Amazing Skillshow HD (youtube.com/watch?v=Q6wGyzHjNJo) | GS9 Football | 1.6m | 6 yr | Skills compilation | 10:06 | Reach | Footage only |
| SERGIO BUSQUETS: La Brujula en el centro del campo (youtube.com/watch?v=aD0uh6OwIjU) | LALIGA EA SPORTS (verified) | 759k | 8 mo | Official highlight reel (Spanish) | 20:00 | Official source, clean assists reel | Highlights, no thesis |

- Saturated angles to avoid: the "genius / maestro / art of simplicity" tribute; the skills compilation; the pivot-role tactical essay built on Cruyff-Guardiola lineage (The Purist owns this at scale); the "he makes it look easy" framing with no numbers behind it.
- Open gap we can own: the verified-data case for the invisible man. Every strong competitor asserts that Busquets did unseen work or made the hard role look simple, but none builds the argument from a logged stat profile. The KiqIQ lane: quantify the signature that makes him look idle (low tackle volume for a holding midfielder, high interception count, the metronome who controls the game without lunging or fouling), set against a discipline record that is rare for the position but, crucially, not the "never sent off" myth. Receipts, not reverence. Raymar made the claim as story; KiqIQ proves it as data.
- Length read from top performers: 10 to 11 minutes is the analytical sweet spot (The Purist 10:58, Raymar 10:17, GS9 10:06). Target roughly 10 to 12 minutes. The 22-minute and 20-minute entries are montage formats, not comparable.

## 2. Research and verification

- Fact sheet: `fact-sheet.md` (status: locked)
- Thesis-critical figures verified: yes (career totals cross-checked Wikipedia career table vs Transfermarkt headline; honours per Wikipedia honours list; per-season detail from API-Football archive, Tier 3)
- Data gaps acknowledged:
  - The API-Football archive covers La Liga only and only 2010 to 2022. It undercounts even his La Liga career (424 archive apps vs 481 full La Liga apps) and must never be presented as a career total. Use it only for per-season event detail (tackles, interceptions, ratings) that the free career tables do not carry.
  - Advanced possession and progression metrics (progressive passes, pass completion under pressure, packing) are not in the archive and are not logged here. Acknowledge their absence rather than invent precision.
  - The "never sent off" superlative is FALSE and is killed. See fact sheet F20 to F22. Busquets was dismissed more than once. Any discipline framing must be scoped to "rare for the position," never "never."

## 3. Angle and thesis (chosen)

- Thesis (one sentence, counterintuitive, falsifiable): by the box score Sergio Busquets did almost nothing, fewer than twenty goals in more than seven hundred Barcelona games and a tackle count that kept falling, yet he was the fixed pivot of one of the most decorated trophy cores in the sport; the numbers that show his value are not the ones the box score keeps.
- Framing is descriptive and structural, not a single-provider causal claim. We say "the counting stats were always modest and the obvious ones fell away," not "proof the job was never about tackling." The defensive-action trend is supporting colour, scoped and confounded, never the spine.
- The figures that prove it:
  - F2, F3: fewer than twenty goals in more than seven hundred Barcelona appearances (the low box-score output). Phrase as "fewer than twenty in more than seven hundred."
  - F30 to F37: the trophy core built around him as the single pivot, nine La Liga titles, three Champions Leagues, a World Cup and a European Championship, first-choice for roughly fourteen years. These are competition-record honours, the strongest tier anchor.
  - F21 to F23: dismissed only a handful of times across more than eight hundred career games as the deepest midfielder. Scoped "rarely," never "never."
  - F15 to F19d (supporting only): interceptions standing up while tackles fall, La Liga 2015 to 2022, per API-Football. On-screen scope line required; confounds named (age, deeper role, Barcelona possession dominance, fewer minutes late).
- Confound to address on screen: the falling tackle and defensive-action numbers are single-provider and have innocent explanations (he aged, the role deepened, Barcelona dominated the ball so fewer defensive actions were needed). The video names this rather than implying the drop alone proves anything.
- Why this over the alternatives: the competitive gap. The Purist owns the positional-role essay and Raymar owns the invisible-work biography, both as narrative. Nobody builds the case from a logged stat profile. KiqIQ's lane is receipts: the same "he looks idle, he was essential" idea, proven with charts, with the discipline myth corrected rather than repeated.

## 4. Art style (the angle dictates this)

See `_context/ANGLE-STYLE-MAP.md` (player table) and `ART-STYLE-GUIDE.md`.

- Subject mode: player
- Angle cluster: Stats lie / underrated
- Art era / style: Cubist figurative sports poster. The fragmented geometric planes carry the thesis visually, the player you can never quite pin down, while still rendering Busquets recognisably through build, posture, features and era kit; stylized in Cubist planes, not photoreal.
- Chart preset: `data_native` (KiqIQ home palette, deep navy and cyan; the cool, modern, analytical skin that harmonises with the flat Cubist poster). This is the flagship look for the pilot.
- AI art style line (fixed descriptor, reuse for every render): "Cubist figurative sports poster: fragmented geometric planes, flat limited palette of deep navy, garnet red and a cyan signal accent, matte printed-poster finish. A tall, upright defensive midfielder, slim build, fair complexion, short dark hair and light stubble, a calm half-turn on the ball, in a plain blue and garnet kit with no logos, recognisable as Sergio Busquets but rendered in Cubist stylisation with the face broken into geometric planes. Single centered figure, generous negative space. Stylised, not a photograph, not a photoreal face-clone, no text."
- Reference images: to be generated by the art director (1 to 2 locked hero refs in `art/`), then image-to-image for every other shot to hold the look.

## 5. Charts

| # | Chart | Figures used (F-ids) | Type | Preset | Built |
|---|-------|----------------------|------|--------|-------|
| 01 | La Liga defensive actions per season, 2015-16 to 2022-23 (tackles vs interceptions, both fading) | F15 to F19d | static line (matplotlib) -> image scene | data_native | yes (`charts/01-defensive-actions-by-season.png`) |
| - | Barcelona games vs goals (722 / 18) | F2, F3 | live `stat` scene in episode JSON | data_native | in JSON |
| - | Red cards by competition (2 / 1 / 1) | F21, F22, F23 | live `stat` scene | data_native | in JSON |
| - | Barcelona trophies (9, 7, 7, 3, 3, 3) | F30 to F35 | live `bar` scene | data_native | in JSON |
| - | Spain caps + tournaments (143, 1, 1) | F7, F36, F37 | live `stat` scene | data_native | in JSON |

Per the chart-builder rule, headline counting numbers are live animated bar/stat scenes in the episode JSON, not pre-rendered PNGs. Only the genuinely complex season-trend chart is a matplotlib PNG. No source line on the chart (KiqIQ mark only); sources live on the fact sheet.

## 6. Script

- File: `script/script.txt` (ElevenLabs-ready, break tags in place). Regenerated fresh 2026-06-03 under re-run hygiene; prior draft discarded.
- Word count: roughly 1,100, about 9 minutes at the ElevenLabs pace once the break tags are counted, inside the 8 to 12 minute band the scan rewards.
- Cold open delivers the thumbnail promise in the first lines (eighteen goals, seven hundred games, did almost nothing), before any branding.
- Re-hook cadence: a genuine analytical turn roughly every 60 to 90 seconds (the goals case, the league-only scope check at 481, the early-trust detail, the defensive-fade chart, the interceptions-held-while-tackles-fell read, the discipline myth correction, the durability beat at 36 starts / 3,200+ minutes, the "box score cannot keep it" point, the trophy core, the system-confound steelman and its Spain/Miami rebuttal). Builds to the World Cup / 143-cap payoff held near the end.
- Every on-screen figure traces to a fact-sheet ID. The discipline section states "rarely," never "never." The defensive-trend section states scope and names the confounds on screen.
- AI-writing-tells sweep: done. No em dashes, no flagged vocabulary, sentence-case, no compulsory summary, no triplet padding.

## 7. Shot / visual plan

The machine-readable plan is the episode JSON at `_system/remotion/episodes/sergio-busquets.json` (regenerated 2026-06-03: 24 scenes, about 8.5 minutes of motion at 30 fps, structure-validated, preset data_native). LEADS with the cold-open hook title (not the logo); the logo sting sits only at the CLOSE. No two same-type scenes are adjacent; every title/stat/bar scene carries a dimmed `bg` Cubist texture and a full-bleed art `image` lands every 20-30s (8 image moments). One motion per scene; sfx are sparse one-shots. The trophy bar and the Spain 143-cap stat are held for the climactic reveal near the end. Durations are pre-mp3 estimates derived from each scene's narration length; fine-tune them against `narration.mp3` in Remotion studio at gate 2 (`make.ps1 -Preview`). No real footage anywhere.

One-line mockups (the cheap design gate before the local render):

| Scene | Type | On-screen | Single move |
|-------|------|-----------|-------------|
| 1 | sting | KiqIQ wordmark | logo bumper in |
| 2 | title | "Eighteen goals. / Seven hundred games." | kinetic lines, boom |
| 3 | image | hero-reference.png, caption "Fourteen years..." | slow Ken Burns in |
| 4 | title | the question | type-on |
| 5 | stat | 722 games / 18 goals (18 highlit) | count-ups land |
| 6 | image | hero-reference.png, "Promoted at twenty" | Ken Burns |
| 7 | title | "So judge the defensive work." | cut |
| 8 | image | 01-defensive-actions-by-season.png | chart Ken Burns, riser |
| 9 | title | "The numbers fell. His place never did." | kinetic |
| 10 | title | "First, kill a myth." | swell |
| 11 | stat | red cards 2 / 1 / 1, "Not never" | count-ups, impact |
| 12 | image | shot-territory.png, "He was already there" | Ken Burns |
| 13 | title | "No column for the pass he stopped..." | kinetic, whoosh |
| 14 | title | "The most important thing he did was never counted." | kinetic, downer |
| 15 | bar | Barcelona trophies 9/7/7/3/3/3 (La Liga highlit) | bars grow, riser |
| 16 | title | "But did the system make him?" | tension |
| 17 | stat | Spain 143 caps / 1 WC / 1 Euro | count-ups, uplift |
| 18 | title | "The goals were never the point." | cut |
| 19 | image | hero-reference.png, "The quietest line in the database." | Ken Burns |
| 20 | title | "The box score asked the wrong question." + next-video sub | boom |
| 21 | sting | KiqIQ wordmark | logo bumper out |

Shorts cut points: scene 2 (the eighteen-goals hook) as a standalone 30 second Short; scene 11 (the red-card myth correction) as a second Short; scene 15 to 17 (trophies plus the Spain rebuttal) as a third.

Assets the render needs in `_system/remotion/public/`:
- `narration.mp3` (produced by `make.ps1` -> tts.py on David's PC).
- `01-defensive-actions-by-season.png` (BUILT and already copied into `public/`).
- The Cubist art set, NOT yet generated (nano-banana key still dead, AI Studio still blocked; must be made in Midjourney via Claude in Chrome on David's account, see section 8). The episode JSON references exactly these 9 files, which must land in `public/`:
  - player shots (6): `hero.png`, `pose-organising.png`, `pose-midpass.png`, `pose-on-ball.png`, `pose-walking.png`, `face-crop.png`
  - background textures (3): `bg-cubist-01.png`, `bg-cubist-02.png`, `bg-cubist-03.png`
Until these nine exist in `public/`, the PRE-RENDER GATE blocks the render (no placeholders).

## 8. Character consistency and art prompts

- STATUS 2026-06-03: all nine prompts were generated in Midjourney via Claude in Chrome (account "finbar"), 16:9 --style raw, on-brand Cubist figures in the navy/garnet/cyan palette. They sit in the Midjourney "Today" feed, NOT yet downloaded (Midjourney saves to David's unmounted Downloads). David downloads the best variant of each, renames to the nine filenames below, and drops them into `_system/remotion/public/` (and copies to `art/`). CAVEAT: some player-shot variants show a faint sponsor swoosh on the kit; pick the cleanest-kit variant and inpaint out any small mark (check at 100%), since the brand rule is no logos/sponsor.
- Method: one locked Cubist hero reference, then image-to-image derivations so the look holds across the set. GENERATION ROUTE for this run (2026-06-03): the nano-banana MCP key is still invalid (re-tested, Gemini returns API_KEY_INVALID) and AI Studio is still permission-blocked, so the sandbox CANNOT generate the art. It must be made in **Midjourney** via Claude in Chrome on David's logged-in account (`--ar 16:9 --style raw`). Midjourney downloads land in David's Downloads (unmounted), so after generating, drop the nine PNGs into `art/` AND `_system/remotion/public/` (the render reads `public/`). Generate `hero.png` first, lock it, then re-upload it as the image reference for each pose to hold the likeness; the three `bg-*` textures are figure-free abstracts in the palette.
- Watermark: inpaint any visible mark out seamlessly (content-aware fill, not a crop), check at 100 percent. SynthID stays; the YouTube AI disclosure still applies.

Locked style line (reuse on every render):
> Cubist figurative sports poster, flat printed-poster finish, no photographic realism. A tall, upright defensive midfielder, slim build, short dark hair, calm composed posture, in a plain deep navy and garnet kit with no logos, no crest, no text and no numbers. Face broken into abstract geometric planes, masked and posterised, no literal likeness and no name. Limited flat palette of deep navy, garnet red and a single bright cyan signal accent. Fragmented angular planes, overlapping shards, matte risograph print texture. Single centered figure, generous negative space. Stylised, graphic, not a photograph.

Per-file prompts (player shots derive image-to-image from the locked `hero.png`):
- `hero.png` (hero, lock FIRST): [style line], half-turn on the ball as if shielding it, centered full figure, generous negative space. Lock, then derive the rest from it.
- `pose-organising.png`: same figure and style, upright, one arm raised directing teammates, calm authority, mid-shot, negative space to one side.
- `pose-midpass.png`: same figure and style, caught mid-pass, planted standing leg, body open, the ball just leaving his foot, wide framing.
- `pose-on-ball.png`: same figure and style, close on the ball with the sole resting on top, composed, head up scanning, three-quarter view.
- `pose-walking.png`: same lone figure and style, walking slowly across midfield, very wide shot, vast empty negative space around him to suggest the territory he controls.
- `face-crop.png`: tight crop of the same geometric face turned slightly away, the abstract posterised planes prominent, heavy negative space on one side.
- `bg-cubist-01.png` (NO figure): abstract Cubist texture, fragmented overlapping planes, navy-led palette with a cyan signal accent, matte risograph grain, for use dimmed behind text scenes.
- `bg-cubist-02.png` (NO figure): same abstract Cubist treatment, garnet-led variation, sparse, low-contrast so on-screen text stays legible.
- `bg-cubist-03.png` (NO figure): same abstract Cubist treatment, cool navy-cyan variation, even sparser, near-monochrome.

Thumbnail art (for the packager's right-hand panel): a tight crop of the hero, the geometric face turned slightly away, heavy negative space on one side for the hero stat and title. A copy of `face-crop.png` works.

## 9. Packaging

Title options (the title is the promise; it never duplicates the thumbnail proof):
1. The footballer the stats could not explain
2. Sergio Busquets and the numbers that lied
3. He scored eighteen goals in seven hundred games. He was irreplaceable.
4. The most important player nobody could measure
5. Why the box score was wrong about Sergio Busquets

Lead candidate: option 1 or 3. Option 3 front-loads the proof for the feed; option 1 is the cleaner KiqIQ promise.

Thumbnails (rebuilt 2026-06-03, preset data_native, proof not title, 120px preview checked; placed in `thumbnails/` and the outputs area):
- `thumb-A-goals.png`: hero "18 / goals in 700+ games", title block "THE NUMBER THAT LIED". Lead.
- `thumb-B-trophies.png`: hero "9 + 3 / leagues + European cups", title block "BUILT AROUND A GHOST".
- `thumb-C-discipline.png`: hero "800+ / games, deepest role", title block "HE BARELY FOULED".
- Drop the locked Cubist still into the right-hand art panel of the chosen one. A/B test A against B on upload.

Description (draft):
> Sergio Busquets scored fewer than twenty goals in more than seven hundred games for Barcelona, and his tackle numbers fell year on year. By the box score he did almost nothing. Yet he was first choice for fourteen years across nine league titles, three Champions Leagues, a World Cup and a European Championship, and two completely different teams built their midfield around him. This is the data case for the most important player the numbers kept underrating, with the discipline myth corrected along the way.
>
> Every figure is sourced from public records. Per-season La Liga defensive numbers are from API-Football and are labelled on screen.
>
> Chapters (approximate; finalise against narration.mp3 at gate 2):
> 0:00 The number that lied
> 0:30 The case against him
> 1:15 Trusted at twenty-one
> 1:50 So judge the defensive work
> 2:45 The actions fell, his place did not
> 3:30 The read held, the challenge fell
> 4:10 The red-card myth, corrected
> 5:00 What the box score cannot keep
> 5:45 What the team won with him
> 6:30 Did the system make him?
> 7:05 It travelled: Spain, and a third team
> 7:55 The wrong question
>
> This video uses AI-generated still imagery and AI narration. No real match footage is used.

Tags: sergio busquets, busquets, busquets barcelona, busquets spain, defensive midfielder, the pivot, pivote, barcelona midfield, la liga analysis, football data analysis, football tactics, why busquets was so good, busquets stats, spain 2010 world cup, xavi iniesta busquets, KiqIQ.

Spotify / podcast title (audio version): The footballer the stats could not explain: Sergio Busquets.

## 10. Pre-upload QC (gate 2 checklist)

- [x] Every on-screen figure traces to a locked fact-sheet ID (stat/bar/image scenes mapped to F-ids in section 5).
- [x] League-only vs all-comps stated: 722 and 18 flagged all-comps; defensive per-season flagged La Liga and per API-Football on screen.
- [x] Contested numbers resolved: red cards scoped to "rarely, not never"; trophy figures given per competition, not as a disputed aggregate.
- [x] No real footage used (charts, stylised stills, motion typography only).
- [ ] AI art is attribute-based, plain kit, no logos: PENDING this run. The 9-file Cubist set (6 player shots + 3 bg textures, section 8) is NOT yet generated; the sandbox image route is dead so it must be made in Midjourney via Chrome on David's account. Abstract geometric faces, no real likeness, plain navy/garnet kit, no crest or sponsor. Drop into `public/` before render. PRE-RENDER GATE blocks until done.
- [x] Script passes the AI-writing-tells sweep.
- [x] Wording and structure original, not modelled on a competitor video.
- [x] Channel mark, footer and frame present (charts and thumbnails carry the KiqIQ mark; Remotion opens and closes on the logo sting).
- [ ] Final cut reviewed in Remotion studio and durations tuned to the narration (David, gate 2).
- [ ] AI-safeguards checklist pass (`_context/AI-SAFEGUARDS-CHECKLIST.md`) before publish.

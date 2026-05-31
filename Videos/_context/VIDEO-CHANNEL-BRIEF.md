# KiqIQ video channel brief

## What this is

A YouTube channel of data-driven football video essays under the KiqIQ brand. Each video is about one subject, a player or a team, built around a single counterintuitive thesis backed by verified data. No real match footage. Visuals are charts from researched stats and stylized AI imagery of the player, moved by editing over stills.

## Brand decision on record

This channel is KiqIQ. The essay format is punchier and more narrative than the KiqIQ constitution's "Authoritative Practitioner" voice, and David has accepted that tension on purpose. The packaging and hooks can carry energy the core brand usually avoids.

What still holds from the KiqIQ constitution, because it protects the brand's reason to exist:
- The evidence hierarchy. Federations and leagues first, official clubs second, reputable databases third, journalism fourth. Wikipedia is a map, never the destination.
- Accuracy over flourish. The selling point is that the numbers are right and the insight is real.
- The AI-writing-tells sweep on all text. See `kiqiq/docs/AI-WRITING-TELLS.md`. No em dashes outside a genuine need, en dashes for ranges, none of the flagged vocabulary, no negation parallelism, no triplet flourishes, no compulsory summary.

## Identity

- Name and logo: KiqIQ. The wordmark sits on every asset. On thumbnails it is a prominent fixed element in the accent colour. On charts it is a quiet footer mark. Drop a real logo image in by setting `LOGO_PATH` in `brand.py`.
- Home palette (KiqIQ): deep navy `#0B1F3A`, cyan high-signal accent `#29C5F6`, secondary purple `#8B5CF6`, white lines `#FFFFFF`. This is the `data_native` preset.
- Per-video styles: the angle picks the skin. `data_native` is home. `engraving` and `faded` are deliberate departures for legend and decline angles. The frame, logo, footer and layout never change.
- Fonts: Inter, the KiqIQ site face (Inter Variable on the site, via next/font). Wired into the chart presets, with a DejaVu Sans fallback. Thumbnail hero stat and title render in Inter Black for feed punch. Drop Inter TTFs into `_system/fonts/` (the app repo already ships `Inter-Regular.ttf` and `Inter-Bold.ttf`). The engraving preset keeps a serif on purpose, as an art departure.

## Voice and narration

AI text-to-speech via ElevenLabs. Scripts are written for the ear and the engine: short declarative sentences, numbers spelled for reading aloud, pauses set with ElevenLabs break tags and punctuation. Analytical density stays high to keep the channel clearly on the authentic, value-adding side of YouTube's content rules.

## The three hard rules

1. Verify every stat against primary sources and log it. Flag league-only versus all-competitions. Cross-check contested figures. Acknowledge era data gaps instead of inventing precision.
2. Competitor videos are leads only. Never facts. Never copied in wording or structure.
3. Player imagery shows the figure but keeps the face abstract and non-literal: identity reads from build, hair, posture, kit colours, era and context, never an exact face and never the player's name. Team imagery uses no single face and no real crest or sponsor logo (kit colours, crowd, stadium, era). Editorial use, plain kit.

## Decided (2026-05-30)

- Font: Inter (site face), Inter Black on thumbnails.
- Narration: ElevenLabs TTS.
- Image generator: Gemini / nano-banana (via the image tool here, free tier). The visible watermark is inpainted out seamlessly (content-aware fill, not a crop) so it is not noticeable at all; SynthID stays embedded and the YouTube AI disclosure still applies, so this removes only the brand mark, not the fact that the image is AI.
- Cadence: weekly. This forces heavy automation of research and chart building. The local API-Football archive (below) is what makes weekly realistic.
- Data: archive as much API-Football data as possible now, before access ends. After that, free 100% verified data only.

## Still open

- Character-consistency method confirmation (proposed: locked reference plus image-to-image).
- ElevenLabs voice choice.
- Logo image file for thumbnails, or keep the wordmark.
- Legal posture on player likeness for a monetized channel across the target markets.

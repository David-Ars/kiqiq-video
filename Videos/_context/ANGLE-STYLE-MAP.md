# Angle to style map

The angle decides the whole video look. Pick the subject mode (player or team), find the angle cluster, take its art style and chart preset, and hold both for every shot and chart. Full art direction and the prompt skeletons are in `ART-STYLE-GUIDE.md`.

## How to use it

1. Lock the thesis on the working doc. Note the subject mode: player or team.
2. Find the angle cluster in the matching table.
3. Take the art style (or an alternate that fits the specific subject) and write the one art style line for the video.
4. Take the chart preset and pass it to `set_preset()`.
5. Record subject mode, art style and preset in working-doc section 4.

## Players (figure shown, face abstract and non-literal)

| Angle | Art style (primary / alternates) | Chart preset |
|---|---|---|
| Stats lie / underrated | Cubist poster / Swiss typographic, flat | `data_native` |
| Engine / relentless work-rate | Futurism / Abstract Expressionist gesture | `data_native` / `blueprint` |
| Tactical / role oddity | tactical blueprint / patent drawing, Bauhaus | `blueprint` |
| Legend / monumental | Constructivist poster / Art Deco, WPA | `deco` |
| Decline / what happened | Abstract Expressionist / airbrush faded | `faded` |
| Enigma / mystery | Dada photomontage / collage, Op Art, Surrealism | `faded` |
| Vindication / triumph | gig poster / Pop art, Y2K | `pop` |
| Villain / controversy | Brutalist / Soviet-severe, Dada | `faded` / `pop` dark |
| Overrated / hype over substance | Corporate Memphis | `data_native` |
| Nostalgia / era piece | 90s broadcast and Panini / GeoCities, vaporwave, airbrush | `pop` / `data_native` |
| Flair / luxury player | Rococo illustration / Art Nouveau (flat face) | `deco` / `engraving` |
| National treasure / folk hero | William Morris figure / WPA | `engraving` / `deco` |
| Underused role / quiet operator | minimalist silhouette | `data_native` |
| Value / rating / market | trading-card / FUT-style card, Swiss typographic | `data_native` or `pop` |
| Cult hero / idol | stained glass and gold icon / street stencil graffiti | `deco` or `pop` |
| Clutch / big-game / pressure | film-noir spotlight / neon synthwave | `faded` (dark) or `pop` |
| Physical toll / injury arc | X-ray and anatomical / glitch | `faded` |
| The machine / pure system | low-poly geometric / contour movement map | `data_native` or `blueprint` |

## Teams (no single face; kit, crowd, stadium, era)

| Angle | Art style (primary / alternates) | Chart preset |
|---|---|---|
| Dynasty / golden era | Renaissance, Baroque / Art Deco, Greco-Roman | `deco` / `engraving` |
| Tactical revolution | Constructivism, Bauhaus / Swiss, blueprint | `blueprint` |
| Collapse / the fall | Romanticism / Expressionism, faded | `faded` |
| Rivalry / the clash | Soviet poster / Pop art split | `pop` / `data_native` |
| One-season miracle | Pop art / 90s broadcast | `pop` |
| Identity / club philosophy | William Morris / Art Nouveau, mid-century | `engraving` / `data_native` |
| Origins / history piece | Victorian engraving / Impressionism, illuminated | `engraving` |
| Dynasty (monument cut) | Roman or Byzantine mosaic | `deco` |
| Club as religion / identity | stained glass cathedral | `engraving` or `deco` |

## The six chart presets

`data_native` cool modern navy and cyan; `blueprint` technical navy with a visible grid; `engraving` antique cream and oxblood; `deco` premium gold on near-black; `faded` cold desaturated steel; `pop` bold celebratory on dark. All keep the KiqIQ frame, logo and footer.

## Music bed (auto-selected by preset)

Each preset has a matching original ambient bed in `_system/remotion/public/` (`music_<preset>.mp3`), tuned to its mood: data_native cool/modern, blueprint clinical with a quiet pulse, engraving solemn/classical, deco golden-age warmth, faded cold/wistful, pop bright/celebratory. The Remotion composition plays it automatically from the episode preset, so the score always matches the look. No action needed beyond choosing the preset; override only if a specific episode wants a different track.

## Notes

- The art style is the expressive layer; the chart preset is the readable layer that harmonises with it.
- Face-realism eras are reserved for team videos, where there is no single likeness to abstract.
- If an angle does not match a cluster, pick the nearest, then choose the preset by warmth and energy.

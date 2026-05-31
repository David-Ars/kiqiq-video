# Art style per angle

The angle drives the whole video look. The art era is the primary expression of the angle; the chart preset is the smaller, readable skin that harmonises with it. One era and one preset per video, fixed from the start.

KiqIQ videos have two subject modes:
- PLAYER: a single footballer. Show the figure, keep the face abstract and non-literal.
- TEAM: a club or national side. No single face. Identity comes from kit colours, the collective, the stadium and the era.

## Rules that never change

- One style per video. Every non-data image shares the chosen art era, generated from 1 to 2 locked references. Charts use the paired preset. Frame, KiqIQ logo and footer never change.
- Player face is abstract. Make the player recognisable through build, height, hair, posture, kit colours, era and context, but keep the face non-literal: simplified, geometric, masked, posterised or gestural. Never an exact likeness. Never put the player's name in the prompt.
- Teams use no real marks. No real club crest, badge or sponsor logo (these are trademarked). Build team identity from kit colours, a stylised original emblem if needed, the crowd, the stadium silhouette and the era. Any human figures are generic, not identifiable people.
- Plain kit in era colours. Editorial and analytical use. Inpaint out the visible Gemini/nano-banana watermark seamlessly (content-aware fill, not a crop), checked at 100% zoom so it is not noticeable at all; SynthID stays embedded.
- Charts stay readable. The art can be expressive; the charts cannot trade legibility for style.

## Prompt skeletons (fill once per video, reuse for every shot)

Player:
> [ART STYLE look: medium, line or shape quality, palette, finish]. A [position] footballer, [build and height], [hair style and colour], [posture or motion], in a plain [colour] kit with no logos. Face kept abstract and non-literal: [simplified / geometric planes / masked / posterised / gestural]. [composition]. Stylised, not a photograph, no text.

Team:
> [ART STYLE look]. A [club or nation] scene in [kit colours], no real crest or sponsor logo. [collective: crowd, eleven silhouettes, the stadium, an era detail]. [composition]. Stylised, not a photograph, no text.

Generate one hero reference, lock it, derive the rest with image-to-image so the look stays identical.

## Player angle clusters

| Angle | Art styles (pick one) | Chart preset |
|---|---|---|
| Stats lie / underrated | Cubist figurative poster, Swiss typographic, contemporary flat | `data_native` |
| The engine / relentless work-rate | Futurism (speed lines, fragmented limbs), Abstract Expressionist gesture | `data_native` or `blueprint` |
| Tactical / role oddity | Tactical blueprint figure, Technical manual / patent drawing, Bauhaus figure study | `blueprint` |
| Legend / monumental | Constructivist sports poster, Art Deco figure, WPA poster | `deco` |
| Decline / what happened | Abstract Expressionist figure, Airbrush 80s poster abstracted (faded) | `faded` |
| Enigma / mystery | Dada photomontage, Collage cutout, Op Art figure, Surrealism | `faded` |
| Vindication / triumph | Concert / gig poster, Pop art, Y2K / Frutiger Aero | `pop` |
| Villain / controversy | Brutalist / anti-design, Soviet-poster severe, Dada (obscured face) | `faded` or `pop` (dark) |
| Overrated / hype over substance | Corporate Memphis human figure | `data_native` (cool) |
| Nostalgia / era piece | 90s/00s broadcast and Panini, Early internet / GeoCities, vaporwave, Airbrush 80s | `pop` or `data_native` |
| Flair / luxury player | Rococo sports illustration, Art Nouveau (flattened face) | `deco` or `engraving` |
| National treasure / folk hero | Arts and Crafts / William Morris figure, WPA | `engraving` or `deco` |
| Underused role / quiet operator | Minimalist silhouette poster | `data_native` |
| Value / rating / market | Trading-card / FUT-style card, Swiss typographic | `data_native` or `pop` |
| Cult hero / idol | Stained glass and gold icon, street stencil graffiti | `deco` or `pop` |
| Clutch / big-game / pressure | Film-noir spotlight (face in shadow), neon synthwave | `faded` (dark) or `pop` |
| Physical toll / injury arc | X-ray and anatomical, glitch / databending | `faded` |
| The machine / pure system | Low-poly geometric, contour movement map | `data_native` or `blueprint` |

## Team angle clusters

| Angle | Art styles (pick one) | Chart preset |
|---|---|---|
| Dynasty / golden era | Renaissance, Baroque, Art Deco, classical Greco-Roman (collective grandeur, no single face) | `deco` or `engraving` |
| Tactical revolution | Constructivism, Bauhaus, Swiss typographic, tactical blueprint | `blueprint` |
| Collapse / the fall of a great side | Romanticism, Expressionism (faded) | `faded` |
| Rivalry / the clash | Soviet poster (two-sided), Pop art split-panel | `pop` or `data_native` |
| One-season miracle | Pop art, 90s/00s broadcast | `pop` |
| Identity / club philosophy | Arts and Crafts / William Morris pattern, Art Nouveau, mid-century modern | `engraving` or `data_native` |
| Origins / history piece | Victorian engraving, Impressionism, medieval illuminated manuscript | `engraving` |
| Dynasty (monument cut) | Roman or Byzantine mosaic | `deco` |
| Club as religion / identity | Stained glass cathedral, gold icon | `engraving` or `deco` |

The face-realism eras (Renaissance, Baroque, Romanticism, Greco-Roman, Victorian portraiture, Impressionism, Art Nouveau) live in the team table on purpose: with no single player to render, a literal hand reads as period grandeur, not a likeness.

## Style shelf (tag shows where each is used)

Player, face stays abstract: Futurism, Cubist figurative, Constructivist poster, Bauhaus figure, WPA poster, Op Art, Minimalist silhouette, tactical blueprint, technical/patent drawing, Swiss typographic, Y2K/Frutiger Aero, GeoCities, Abstract Expressionist, Dada photomontage, collage cutout, gig poster, William Morris figure, Rococo illustration, Corporate Memphis, airbrush 80s, Pop art, Surrealism, vaporwave, Memphis, Risograph, psychedelia, grunge, contemporary flat, Brutalist, mid-century modern, 90s/00s broadcast and Panini. Trading-card / FUT card, stained glass and gold icon, graphic-novel ink with halftone, film-noir spotlight, neon synthwave, low-poly geometric, glitch / databending, tabloid halftone newsprint, street stencil graffiti, contour movement map, X-ray anatomical, Roman and Byzantine mosaic.

Team, literal faces allowed: Renaissance, Baroque, Romanticism, classical Greco-Roman, Victorian engraving, Impressionism, Art Nouveau, medieval illuminated, plus any of the player-mode styles used collectively.

When a style is not one of the six chart presets, pick the preset closest in warmth and energy: `data_native` cool and modern, `blueprint` technical, `engraving` antique and warm, `deco` premium and dark, `faded` cold and melancholic, `pop` bright and celebratory.

## New look notes (what the added styles are)

- Trading-card / FUT-style card: a framed player card with a rating block and stat strip. The face stays stylised. Strong for value, rating and breakout angles.
- Stained glass / gold icon: leaded glass segments or a Byzantine halo. Reverent, iconic, no literal face needed. Idol and cult-hero angles.
- Graphic-novel ink + halftone: heavy black ink, dramatic shadow, dot screens. Origin and rise arcs.
- Film-noir spotlight: a single hard light, the face dropping into shadow. Built-in abstraction. Clutch, pressure, lone-figure and villain angles.
- Neon synthwave: night, glow, light trails, under-the-lights energy. Big-game and modern-superstar angles.
- Low-poly geometric: faceted 3D planes, no literal face. The machine and analytical angles.
- Glitch / databending: torn scanlines, channel shift, breakdown. Decline and chaos angles.
- Tabloid halftone newsprint: back-page print, coarse dots, headline energy. Media storm and scrutiny.
- Street stencil graffiti: spray stencil, terrace and ultras energy. Cult fan-favourite.
- Contour movement map: the player drawn as topographic contours of the ground they cover. Coverage and territory angles.
- X-ray / anatomical: a clinical anatomical study. Physical toll and injury arcs.
- Roman / Byzantine mosaic: tiled, ancient, monumental. Team dynasty and origins.

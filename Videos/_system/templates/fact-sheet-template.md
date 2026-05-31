# Fact sheet: [SUBJECT NAME]  (player or team)

Episode: [slug]  ·  Compiled: [YYYY-MM-DD]  ·  Status: in progress / locked

Every figure that reaches the script must appear here first, with a source and a confidence call. If a number is not on this sheet, it does not go in the video.

## Evidence hierarchy (KiqIQ)

Trust federations and leagues first, official clubs second, reputable databases third, quality journalism fourth. Wikipedia is a map to a source, never the source itself. Record the tier for every figure.

- T1: federation or league (FIFA, UEFA, Premier League, official competition record)
- T2: official club site or official player record
- T3: reputable database (FBref, Transfermarkt, Understat, Opta-derived)
- T4: quality journalism (named outlet, named author)

## Figure log

| ID | Claim / figure | Value | Scope | Tier | Source name | URL | Accessed | Confidence | Cross-check notes |
|----|----------------|-------|-------|------|-------------|-----|----------|------------|-------------------|
| F1 | e.g. PL tackles 2015-16 | 175 | league-only, single season | T1 | Premier League | [url] | 2026-05-30 | verified (2 sources) | matches FBref 175 |
| F2 |  |  |  |  |  |  |  |  |  |
| F3 |  |  |  |  |  |  |  |  |  |

Scope values: `league-only`, `all-comps`, `single season`, `career`, `international`. Always state which. A league-only number presented as a career number is the most common error in this genre.

Confidence values:
- `verified`: two or more independent sources agree.
- `single-source`: only one source found. Flag in script if used.
- `contested`: sources disagree. Record each value and which source gives it. Do not average. Pick the highest-tier source and say so on screen.
- `no data exists`: the figure was not tracked in this player's era. Say that in the script. Do not invent precision (for example, do not quote "expected goals" for a 1990s player).

## Contested numbers

List any figure where sources disagree, with each value and its source, and the resolution.

- [claim]: source A says X (Tier _), source B says Y (Tier _). Using X because [reason].

## Era and data gaps

Note metrics that do not exist for this player's period, so the script can acknowledge the gap rather than fabricate a number.

- [metric]: not tracked before [year]. Use [proxy] or state the absence.

## Thesis-critical figures

The two or three numbers the whole video rests on. These get the hardest cross-check and an on-screen source line.

1. [figure] (ID Fx)
2. [figure] (ID Fx)

## Image / likeness notes

- Subject mode: player / team.
- Player: recognisable figure (build, hair, kit colours, posture, era), face kept abstract and non-literal, no name in the prompt.
- Team: no single face, no real crest or sponsor logo; kit colours, crowd, stadium, era.
- Usage is editorial and analytical.

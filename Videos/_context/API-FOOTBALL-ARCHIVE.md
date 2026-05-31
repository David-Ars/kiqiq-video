# API-Football archive plan

Goal: pull as much useful API-Football data as possible into a local store before access ends, then rely on free verified data afterward. The archive becomes the offline dataset behind weekly chart production.

## Why you run it, not me

The API-Football host is not reachable from the Cowork sandbox (blocked at the network layer). So the ingester runs on your machine, where the key and open network already live. This also matches how you ship.

## Run it

PowerShell:

```
$env:APIFOOTBALL_KEY="your-api-football-key"; python "C:\Users\david\Documents\Claude\Projects\KiqIQ\Videos\_system\apifootball_archive.py"
```

Stop and re-run any time. A manifest at `_data/apifootball/_manifest.json` records every completed request, so a re-run skips finished calls and continues. Run it across the days you have left; it stops at the daily cap and you continue the next day.

## What it pulls, in priority order

1. Status and the full leagues catalogue.
2. Per league and season, the cheap high-value data first: standings, top scorers, top assists, cards, teams.
3. The bulk: player season statistics per league and season (paginated).
4. Fixtures metadata per league and season (flag `PULL_FIXTURES`).
5. Player career context: transfers, trophies, injuries/sidelined (flag `PULL_PLAYER_CAREER`).
6. Per-fixture events, lineups and player stats (flag `PULL_FIXTURE_EVENTS`, off by default, very expensive).

## Scope you can edit at the top of the script

- `LEAGUES`: currently the big five plus UCL, UEL, Eredivisie, Primeira, Championship.
- `SEASONS`: currently 2010 to 2025.
- The three flags above.
- `DAILY_CAP`: default 7500. Set to your real daily limit.
- `DELAY`: seconds between calls, default 0.4 (about 150/min).

## Budget reality

The big-five plus Europe across 2010 to 2025 is a large pull, dominated by paginated player statistics. At 7500 calls/day it spans several days. The priority order means standings, scorers and player season stats land before fixtures and player-career calls, so if you run out of days you still keep the most useful data. Turn on `PULL_FIXTURE_EVENTS` only if you have clear budget headroom.

## Evidence-hierarchy note

API-Football is a third-party aggregator, Tier 3 on the KiqIQ hierarchy. Use it freely for chart inputs and discovery. Any thesis-critical figure still gets cross-checked against a Tier 1 or Tier 2 source on the fact sheet.

## Storage

JSON under `Videos/_data/apifootball/`, one folder per endpoint, plus `_manifest.json`. Raw responses are kept as-is so they can be reshaped later without re-pulling.

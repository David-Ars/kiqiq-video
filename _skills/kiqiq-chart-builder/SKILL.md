---
name: kiqiq-chart-builder
description: Build the branded data charts from the verified fact sheet. Triggers: build the charts, make the graphics, chart the stats.
---

# KiqIQ chart builder

## How Claude runs this
- Claude runs this step autonomously. The player comes from the kiqiq-produce run or the request; if missing, take the active episode under `Videos/output/`, and ask David only if the player is genuinely unclear. Create the episode folder from `Videos/output/_EPISODE-TEMPLATE/` if it does not exist.
- Obey the three hard rules in `Videos/_context/VIDEO-CHANNEL-BRIEF.md`: verify and log every stat (flag league-only vs all-comps); competitor videos are leads only, never copied; player imagery keeps the face abstract and non-literal (identity via build, hair, kit, posture, context, never an exact face or the name), team imagery uses no single face and no real crest or sponsor logo, plain kit.
- Apply the writing-tells doc to all text: `C:\Users\david\Documents\Kiqiq\kiqiq\docs\AI-WRITING-TELLS.md`. No em dashes, no flagged vocabulary, sentence-case headings.
- Update only this step's sections of `working-doc.md` / `fact-sheet.md`. Work without step-by-step narration; report the result.

## What Claude does

Claude builds the data charts. SOP Role 3.

Copy `Videos/_system/example_charts.py` into `<slug>/charts/`. Call `brand.set_preset()` with the chosen preset (one of: data_native, blueprint, engraving, deco, faded, pop) from working-doc section 4. Build each chart only from locked fact-sheet figures (use `_system/archive_query.py` to pull or recompute the numbers behind them, e.g. leaderboards and per-season rows). NOTE: bar and stat charts are now LIVE animated Remotion components, supplied as `bar` and `stat` scenes in the episode props (`_system/remotion/episodes/<slug>.json`), not pre-rendered PNGs. Do NOT pre-render bar or stat charts as matplotlib PNGs; that throws away the animation. Put their verified numbers straight into `bar`/`stat` scenes in the episode props. Use matplotlib (example_charts.py) only for genuinely complex or static charts (e.g. a pitch map) that then go in as `image` scenes. Every animated number still traces to a fact-sheet ID. Run it (set PYTHONPYCACHEPREFIX to a temp dir if a stale cache blocks import). Fill working-doc section 5. Layout, footer and the KiqIQ mark come from `brand.py`; do not change them. Do NOT add any "Data:" or source line to a chart (use only `brand.footer(fig)`, which draws the KiqIQ mark and no source); sources live on the fact sheet, by David's rule.

### Advanced animated charts (D3) — optional, when a bar or stat scene is not enough
For data stories the basic `bar`/`stat` scenes cannot tell, build a D3-driven Remotion scene: a bar-race over seasons, an animated line that draws on, a pass/heat map, or a node diagram whose links draw themselves. D3 is the right tool because for KiqIQ the data IS the content. Rules: still readable at 120px, labels legible, each data point gets enough screen time before the next enters, palette from the chosen `brand.py` preset, and every number traces to a fact-sheet ID. Reference a D3 example, describe what it must communicate, and let the build follow; keep it simple and iterate in the same session rather than over-specifying up front. (Source: competitor technique review, logged in RUNBOOK.)

## Next step (always end with this)

Do ONLY this step. When it finishes, STOP. Do not begin the next skill or any other step yourself. End the reply by telling David exactly what to run next, and wait:

> Next: run **kiqiq-scriptwriter** — input: the same player.

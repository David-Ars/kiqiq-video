# Videos system

The reusable engine for KiqIQ player video essays. Read `../_context/` first for the brand brief, the production flow and the angle-to-style map.

## Folder layout

```
Videos/
  _context/                 brand brief, production flow, angle-style map
  _system/                  the engine (this folder)
    brand.py                fixed CONSTANTS + per-video PRESETS, all helpers
    example_charts.py       worked chart script (the Kante example), the pattern to copy
    thumb.py                thumbnail builder, fixed frame + KiqIQ logo, per-video skin
    templates/
      fact-sheet-template.md
      working-doc-template.md
    out/ , thumb_out/        sample renders from the example scripts
  input/
    leads/                  competitor media you drop in for the rip step
    reference-art/          locked 1 to 2 AI reference renders per player
  output/
    _EPISODE-TEMPLATE/      copy this per video
      charts/  thumbnails/  art/  script/
```

## Start a new episode

1. Copy `output/_EPISODE-TEMPLATE/` to `output/<player-slug>/`.
2. Copy `templates/working-doc-template.md` and `templates/fact-sheet-template.md` into it, renamed for the player.
3. Work the pipeline in `_context/PRODUCTION-FLOW.md` top to bottom.
4. For charts: copy `example_charts.py` into the episode `charts/` folder, call `set_preset()` with the style the angle dictates (see the angle-style map), edit the data, run it.
5. For the thumbnail: call `thumbnail()` in `thumb.py` with the episode's preset, hero stat, label and title lines.

## brand.py model

- `CONSTANTS` are the channel signature and do not change per video: layout anchors, footer, logo position, the KiqIQ wordmark.
- `PRESETS` are the swappable skin chosen per video: palette, font, fill style, texture. `data_native` is the KiqIQ home palette. `engraving` and `faded` are angle-driven.
- `set_preset("name")` once at the top of a chart script. Everything reads the active preset through `P()`.
- The rule: the image flexes, the frame never does. The KiqIQ logo is on every thumbnail regardless of style.

## Render the samples

```
cd Videos/_system
python3 example_charts.py      # writes 4 charts to ./out
python3 thumb.py               # writes 2 thumbnails to ./thumb_out
```

## Notes

- Set `LOGO_PATH` in `brand.py` to use a real logo image on thumbnails instead of the wordmark text.
- `mplsoccer` is only for modern players with real event data. Install it when first needed.
- For the competitor-rip step, yt-dlp and Whisper are not preinstalled in the sandbox. ffmpeg is.

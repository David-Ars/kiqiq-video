"""
KiqIQ video channel: multi-preset branded chart template.

MODEL
  CONSTANTS  : fixed across the whole series. The channel signature
               (chart structure, layout logic, footer, mark position).
  PRESETS    : the per-video skin matching the angle's art style.
  set_preset("name") once at the top of a video's chart script. Everything
               downstream reads the active preset through P().

HOUSE PALETTE
  data_native is the KiqIQ home skin (deep navy, cyan accent, purple secondary).
  engraving and faded are angle-driven departures. Frame, logo and footer stay
  constant so the brand still reads.
"""
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Register any .ttf/.otf in _system/fonts/ so brand fonts (Inter) resolve.
# Falls back to DejaVu Sans if none are present, so scripts still render.
_FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
def _register_local_fonts():
    if not os.path.isdir(_FONT_DIR):
        return
    for f in os.listdir(_FONT_DIR):
        if f.lower().endswith((".ttf", ".otf")):
            try:
                font_manager.fontManager.addfont(os.path.join(_FONT_DIR, f))
            except Exception:
                pass
_register_local_fonts()

# =====================================================================
# CONSTANTS. Fixed channel identity. Do not change per video.
# =====================================================================
CHANNEL_MARK = "KiqIQ"          # channel wordmark printed on every asset
LOGO_PATH = os.path.join(os.path.dirname(__file__), "assets", "logo_transparent.png")  # real KiqIQ logo (navy keyed out);
                                # thumbnails; falls back to the wordmark text
FOOTER_PREFIX = "Data:"         # footer always starts the same way
FIG_DPI = 200

TITLE_XY  = (0.04, 0.92)        # title anchor
SUB_DY    = 0.055               # subtitle sits this far below the title
FOOTER_XY = (0.012, 0.012)      # source line, constant corner
MARK_XY   = (0.988, 0.012)      # channel mark, constant corner

# =====================================================================
# PRESETS. Pick one with set_preset(). Every preset defines the same keys.
# =====================================================================
PRESETS = {
    "data_native": {
        "bg":        "#0B1F3A",
        "panel":     "#102A4C",
        "text":      "#EAF2FA",
        "muted":     "#8AA0B8",
        "grid":      "#1C3656",
        "neutral":   "#33445C",
        "accent":    "#29C5F6",
        "accent_d":  "#1A8FBC",
        "accent2":   "#8B5CF6",
        "font":      "Inter",
        "fill":      "flat",
        "texture":   None,
        "label_dark_on_accent": True,
    },
    "engraving": {
        "bg":        "#EFE7D3",
        "panel":     "#E7DCC2",
        "text":      "#231C12",
        "muted":     "#6E5F49",
        "grid":      "#C9BC9E",
        "neutral":   "#B8A98A",
        "accent":    "#7B2D26",
        "accent_d":  "#54201B",
        "accent2":   "#3F5740",
        "font":      "DejaVu Serif",
        "fill":      "hatch",
        "texture":   "paper",
        "label_dark_on_accent": False,
    },
    "faded": {
        "bg":        "#15171C",
        "panel":     "#1C1F26",
        "text":      "#C9CDD4",
        "muted":     "#6B7280",
        "grid":      "#23262E",
        "neutral":   "#33373F",
        "accent":    "#5B7A99",
        "accent_d":  "#3E5670",
        "accent2":   "#7C6F86",
        "font":      "Inter",
        "fill":      "flat",
        "texture":   None,
        "label_dark_on_accent": False,
    },

    # ---- BLUEPRINT : tactical / role-oddity angles. Navy with visible grid. ----
    "blueprint": {
        "bg":"#0A2540","panel":"#0E2E4E","text":"#EAF2FA","muted":"#7FA8C9",
        "grid":"#1E4B73","neutral":"#284E73","accent":"#29C5F6","accent_d":"#1A8FBC",
        "accent2":"#9AD8F2","font":"Inter","fill":"flat","texture":None,
        "label_dark_on_accent":True,
    },

    # ---- DECO : legend / monument angles. Gold on near-black, premium. ----
    "deco": {
        "bg":"#11100C","panel":"#1A1812","text":"#F3ECD9","muted":"#B9A77C",
        "grid":"#2A2517","neutral":"#3A3320","accent":"#C8A24A","accent_d":"#8C6F2E",
        "accent2":"#B9A77C","font":"DejaVu Serif","fill":"flat","texture":None,
        "label_dark_on_accent":True,
    },

    # ---- POP : vindication / triumph angles. Bold, celebratory, high-energy. ----
    "pop": {
        "bg":"#101418","panel":"#1A2030","text":"#FFFFFF","muted":"#8A93A6",
        "grid":"#232A3A","neutral":"#333B4D","accent":"#FFC400","accent_d":"#C99A00",
        "accent2":"#29C5F6","font":"Inter","fill":"flat","texture":None,
        "label_dark_on_accent":True,
    },
}

_active = {"name": "data_native", "p": PRESETS["data_native"]}


def set_preset(name):
    if name not in PRESETS:
        raise ValueError(f"Unknown preset '{name}'. Options: {list(PRESETS)}")
    _active["name"] = name
    _active["p"] = PRESETS[name]
    plt.rcParams.update({"font.family": [PRESETS[name]["font"], "DejaVu Sans"],
                         "figure.dpi": FIG_DPI})
    return PRESETS[name]


def P():
    return _active["p"]


def active_name():
    return _active["name"]


def new_fig(w=9, h=5):
    p = P()
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor(p["bg"])
    ax.set_facecolor(p["bg"])
    if p["texture"] == "paper":
        _paper(fig, p)
    return fig, ax


def style_axes(ax):
    p = P()
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=p["muted"], length=0, labelsize=11)
    return ax


def apply_base(ax):
    return style_axes(ax)


def title(fig, text, sub=None):
    p = P()
    fig.text(*TITLE_XY, text, color=p["text"], fontsize=19, fontweight="bold", ha="left")
    if sub:
        fig.text(TITLE_XY[0], TITLE_XY[1] - SUB_DY, sub, color=p["muted"], fontsize=11, ha="left")


def footer(fig, source=None):
    # Source line removed from visuals by request; sources live on the fact sheet.
    # Only the KiqIQ channel mark stays.
    p = P()
    fig.text(*MARK_XY, CHANNEL_MARK, color=p["muted"], fontsize=8, ha="right", alpha=0.7)


def bar_fill_kwargs(color):
    p = P()
    if p["fill"] == "hatch":
        return dict(color=p["bg"], edgecolor=color, hatch="////", linewidth=1.2)
    return dict(color=color)


def label_color_on_accent():
    p = P()
    return p["bg"] if p["label_dark_on_accent"] else p["text"]


def _paper(fig, p):
    import numpy as np
    ax_bg = fig.add_axes([0, 0, 1, 1], zorder=-10)
    ax_bg.axis("off")
    rng = np.random.default_rng(7)
    n = 1400
    ax_bg.scatter(rng.random(n), rng.random(n), s=rng.random(n) * 1.2,
                  c=p["muted"], alpha=0.06, linewidths=0)

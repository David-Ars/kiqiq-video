"""
Worked example: the four Kante charts, rebuilt on the preset API.

This is the reference for how a per-video chart script should look. Copy it
into an episode's charts folder, call set_preset() with the style the angle
dictates, then edit the data and copy. All structure (title position, footer,
mark, fills) comes from brand.py, so charts stay on-brand across videos.

Run:  python3 example_charts.py [output_dir]
Default output dir is ./out beside this file.
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

import brand
from brand import set_preset, P, style_axes, title, footer, bar_fill_kwargs, label_color_on_accent

# The angle here is "stats lie / measured", so the KiqIQ home skin fits.
set_preset("data_native")
p = P()

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

# ============================================================
# CHART 1: THE MARGIN (tackles + interceptions, 2015-16)
# Example data only. Verify every figure on the fact sheet first.
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5.2))
fig.patch.set_facecolor(p["bg"]); ax.set_facecolor(p["bg"])
style_axes(ax)
cats = ["Tackles", "Interceptions"]
hero = [175, 157]
nextbest = [144, 142]
y = np.arange(len(cats)); h = 0.34
ax.barh(y + h / 2, nextbest, height=h, color=p["neutral"], label="Next-best PL player")
ax.barh(y - h / 2, hero, height=h, label="N'Golo Kante", **bar_fill_kwargs(p["accent"]))
ax.set_yticks(y); ax.set_yticklabels(cats, color=p["text"], fontsize=13)
ax.invert_yaxis(); ax.set_xlim(0, 200); ax.xaxis.set_visible(False)
for vals, ypos, col in [(hero, y - h / 2, label_color_on_accent()), (nextbest, y + h / 2, p["text"])]:
    for v, yy in zip(vals, ypos):
        ax.text(v - 5, yy, str(v), va="center", ha="right", color=col, fontsize=12, fontweight="bold")
ax.text(178, y[0] - h / 2, "+31", va="center", ha="left", color=p["accent"], fontsize=14, fontweight="bold")
ax.text(160, y[1] - h / 2, "+15", va="center", ha="left", color=p["accent"], fontsize=14, fontweight="bold")
title(fig, "He didn't win the race. He lapped it.",
      "Premier League 2015-16. Kante vs the next-best player in each category")
leg = ax.legend(loc="lower right", frameon=False, fontsize=10)
for t in leg.get_texts():
    t.set_color(p["text"])
footer(fig)
plt.subplots_adjust(top=0.84, bottom=0.10, left=0.13, right=0.97)
plt.savefig(f"{OUT}/01_margin.png", facecolor=p["bg"], bbox_inches="tight")
plt.close()

# ============================================================
# CHART 2: THE DISCIPLINE PARADOX (stat card)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor(p["bg"]); ax.set_facecolor(p["bg"]); ax.axis("off")
fig.text(0.04, 0.92, "The destroyer who never got sent off", color=p["text"],
         fontsize=19, fontweight="bold", ha="left")
cards = [("0", "red cards", p["accent"]), ("31", "yellow cards", p["text"]), ("222", "PL appearances", p["text"])]
for i, (num, lab, col) in enumerate(cards):
    cx = 0.18 + i * 0.32
    ax.text(cx, 0.52, num, transform=ax.transAxes, ha="center", va="center",
            fontsize=64, fontweight="bold", color=col)
    ax.text(cx, 0.24, lab, transform=ax.transAxes, ha="center", va="center",
            fontsize=13, color=p["muted"])
ax.text(0.02, 0.06, "Chelsea + Leicester City, Premier League",
        transform=ax.transAxes, ha="left", color=p["muted"], fontsize=10)
footer(fig)
plt.subplots_adjust(top=0.82, bottom=0.08)
plt.savefig(f"{OUT}/02_discipline.png", facecolor=p["bg"], bbox_inches="tight")
plt.close()

# ============================================================
# CHART 3: TWO CLUBS, TWO TITLES (timeline)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 4.6))
fig.patch.set_facecolor(p["bg"]); ax.set_facecolor(p["bg"]); ax.axis("off")
fig.text(0.04, 0.92, "Two seasons. Two clubs. Two titles.", color=p["text"],
         fontsize=19, fontweight="bold", ha="left")
ax.plot([0.1, 0.9], [0.5, 0.5], color=p["grid"], lw=3, transform=ax.transAxes, zorder=1)
nodes = [(0.28, "2015-16", "LEICESTER CITY", "Champions"),
         (0.72, "2016-17", "CHELSEA", "Champions")]
for x, season, club, res in nodes:
    ax.scatter([x], [0.5], s=420, color=p["accent"], transform=ax.transAxes, zorder=3)
    ax.scatter([x], [0.5], s=120, color=p["bg"], transform=ax.transAxes, zorder=4)
    ax.text(x, 0.70, season, transform=ax.transAxes, ha="center", color=p["muted"], fontsize=12)
    ax.text(x, 0.36, club, transform=ax.transAxes, ha="center", color=p["text"], fontsize=15, fontweight="bold")
    ax.text(x, 0.26, res, transform=ax.transAxes, ha="center", color=p["accent"], fontsize=12, fontweight="bold")
ax.annotate("", xy=(0.66, 0.5), xytext=(0.34, 0.5), transform=ax.transAxes,
            arrowprops=dict(arrowstyle="->", color=p["muted"], lw=2))
ax.text(0.5, 0.58, "transfer", transform=ax.transAxes, ha="center", color=p["muted"], fontsize=10, style="italic")
ax.text(0.02, 0.06, "First outfield player to win back-to-back English titles with different clubs since Cantona",
        transform=ax.transAxes, ha="left", color=p["muted"], fontsize=10)
footer(fig)
plt.subplots_adjust(top=0.82, bottom=0.08)
plt.savefig(f"{OUT}/03_two_titles.png", facecolor=p["bg"], bbox_inches="tight")
plt.close()

# ============================================================
# CHART 4: WORLD CUP 2018 (minutes played)
# ============================================================
fig, ax = plt.subplots(figsize=(9, 4.6))
fig.patch.set_facecolor(p["bg"]); ax.set_facecolor(p["bg"]); ax.axis("off")
fig.text(0.04, 0.92, "France's World Cup, 2018: barely came off", color=p["text"],
         fontsize=19, fontweight="bold", ha="left")
pct = 575 / 630
x0, x1, ty = 0.08, 0.92, 0.5
ax.plot([x0, x1], [ty, ty], color=p["neutral"], lw=22, transform=ax.transAxes, solid_capstyle="round")
ax.plot([x0, x0 + (x1 - x0) * pct], [ty, ty], color=p["accent"], lw=22, transform=ax.transAxes, solid_capstyle="round")
ax.text(0.08, 0.74, "575", transform=ax.transAxes, ha="left", color=p["text"], fontsize=42, fontweight="bold")
ax.text(0.30, 0.74, "of 630 minutes", transform=ax.transAxes, ha="left", color=p["muted"], fontsize=14, va="center")
ax.text(0.92, 0.28, "7 of 7 matches started", transform=ax.transAxes, ha="right", color=p["accent"], fontsize=12, fontweight="bold")
footer(fig)
plt.subplots_adjust(top=0.82, bottom=0.08)
plt.savefig(f"{OUT}/04_worldcup.png", facecolor=p["bg"], bbox_inches="tight")
plt.close()

print("charts generated in", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f)

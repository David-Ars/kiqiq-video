"""
KiqIQ episode chart: Sergio Busquets, La Liga defensive actions by season.
Only complex/static chart for this episode -> image scene. Bar/stat headline
numbers are LIVE Remotion scenes in the episode JSON, not pre-rendered here.
Every figure traces to a locked fact-sheet ID (F15-F19d). data_native preset.
"""
import os, sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "_system")))
# fallback path resolve for sandbox
SYS = "/sessions/sleepy-elegant-heisenberg/mnt/KiqIQ/Videos/_system"
if SYS not in sys.path: sys.path.insert(0, SYS)
import brand
from brand import set_preset, P, style_axes, title, footer

set_preset("data_native")
p = P()
OUT = os.path.dirname(__file__)

# La Liga per-season, API-Football archive (Tier 3). F15..F19d.
seasons = ["15/16","16/17","17/18","18/19","19/20","20/21","21/22","22/23"]
tackles      = [103, 84, 88, 90, 80, 63, 93, 59]   # F15..F19d tackles col
interceptions= [ 67, 47, 51, 54, 44, 53, 45, 27]   # F15..F19d interceptions col
x = np.arange(len(seasons))

fig, ax = plt.subplots(figsize=(9, 5.2))
fig.patch.set_facecolor(p["bg"]); ax.set_facecolor(p["bg"])
style_axes(ax)
ax.grid(axis="y", color=p["grid"], linewidth=0.8, alpha=0.7)
ax.set_axisbelow(True)

# Tackles: the falling challenge count (cyan accent, the headline line)
ax.plot(x, tackles, color=p["accent"], lw=3.2, marker="o", markersize=7,
        markerfacecolor=p["accent"], markeredgecolor=p["bg"], zorder=4, label="Tackles")
# Interceptions: the read (purple accent2)
ax.plot(x, interceptions, color=p["accent2"], lw=3.2, marker="o", markersize=7,
        markerfacecolor=p["accent2"], markeredgecolor=p["bg"], zorder=4, label="Interceptions")

# endpoint value tags
ax.text(x[0], tackles[0]+5, "103", ha="center", color=p["accent"], fontsize=12, fontweight="bold")
ax.text(x[-1], tackles[-1]-9, "59", ha="center", color=p["accent"], fontsize=12, fontweight="bold")
ax.text(x[0], interceptions[0]+5, "67", ha="center", color=p["accent2"], fontsize=12, fontweight="bold")
ax.text(x[-1], interceptions[-1]-9, "27", ha="center", color=p["accent2"], fontsize=12, fontweight="bold")

ax.set_xticks(x); ax.set_xticklabels(seasons, color=p["text"], fontsize=11)
ax.set_ylim(0, 120); ax.set_yticks([0,30,60,90,120])
ax.tick_params(axis="y", labelcolor=p["muted"])

title(fig, "The actions fell. His place never did.",
      "Sergio Busquets, La Liga defensive actions per season, per API-Football")
leg = ax.legend(loc="upper right", frameon=False, fontsize=11)
for t in leg.get_texts(): t.set_color(p["text"])
footer(fig)
plt.subplots_adjust(top=0.83, bottom=0.10, left=0.08, right=0.97)
path = os.path.join(OUT, "01-defensive-actions-by-season.png")
plt.savefig(path, facecolor=p["bg"], bbox_inches="tight")
plt.close()
print("wrote", path)

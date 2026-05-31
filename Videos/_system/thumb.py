"""
KiqIQ thumbnail system. Same preset logic as the charts.

THE RULE: the image flexes, the frame never does.
  Fixed frame, identical on every thumbnail:
    - oversized hero stat, top-left, in the accent colour
    - stat label directly beneath it
    - title block lower-left, fixed font and casing
    - KiqIQ logo bottom-left
    - accent colour as the border

Best-practice guards (2026):
  - Title text capped at MAX_TITLE_WORDS (3-4 words). Warns if exceeded.
  - Text kept upper/left, clear of the bottom-right timestamp and the bottom
    progress bar (logo sits above the progress-bar zone).
  - A 120px-wide preview is saved next to each thumbnail for the legibility
    test: if it does not read at that size, the design fails.

Run:  python3 thumb.py [output_dir]
"""
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import brand

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "thumb_out")
os.makedirs(OUT, exist_ok=True)

MAX_TITLE_WORDS = 4   # hard guidance: keep thumbnail title to 3-4 words


def thumbnail(preset_name, hero_stat, hero_label, title_lines, art_label, filename=None):
    words = sum(len(line.split()) for line in title_lines)
    if words > MAX_TITLE_WORDS:
        print(f"  WARNING: thumbnail title is {words} words (cap {MAX_TITLE_WORDS}). "
              f"Tighten it: title = promise, thumbnail = proof, no duplicate of the video title.")

    brand.set_preset(preset_name)
    p = brand.P()
    # 1280x720 at 200 dpi -> 6.4 x 3.6 inches
    fig = plt.figure(figsize=(6.4, 3.6))
    fig.patch.set_facecolor(p["bg"])
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    if p["texture"] == "paper":
        brand._paper(fig, p)

    # FIXED FRAME 1: accent border
    ax.add_patch(Rectangle((0.012, 0.02), 0.976, 0.96, fill=False,
                 edgecolor=p["accent"], linewidth=3, zorder=5))

    # PER-VIDEO ART SKIN: panel where the AI character render drops in
    ax.add_patch(Rectangle((0.56, 0.04), 0.42, 0.92, facecolor=p["panel"],
                 edgecolor=p["grid"], linewidth=1, zorder=2))
    ax.text(0.77, 0.55, art_label, ha="center", va="center", color=p["muted"],
            fontsize=8, style="italic", zorder=3, wrap=True)
    ax.text(0.77, 0.46, "[ per-video art skin ]", ha="center", va="center",
            color=p["muted"], fontsize=7, zorder=3)

    # FIXED FRAME 2: hero stat zone, top-left (Inter Black for feed punch)
    ax.text(0.06, 0.82, hero_stat, ha="left", va="center", color=p["accent"],
            fontsize=66, fontweight="black", zorder=6)
    ax.text(0.065, 0.645, hero_label, ha="left", va="center", color=p["text"],
            fontsize=12, fontweight="bold", zorder=6)

    # FIXED FRAME 3: title band, upper/left, clear of the bottom progress bar
    for i, line in enumerate(title_lines):
        ax.text(0.06, 0.46 - i * 0.12, line, ha="left", va="center", color=p["text"],
                fontsize=24, fontweight="black", zorder=6)

    # FIXED FRAME 4: KiqIQ logo, constant corner, above the progress-bar zone.
    if brand.LOGO_PATH and os.path.exists(brand.LOGO_PATH):
        import matplotlib.image as mpimg
        from matplotlib.offsetbox import OffsetImage, AnnotationBbox
        from matplotlib.patches import FancyBboxPatch
        ax.add_patch(FancyBboxPatch((0.04, 0.06), 0.155, 0.11,
                     boxstyle="round,pad=0.004,rounding_size=0.018",
                     facecolor="#0B1F3A", edgecolor=p["accent"], linewidth=1.0,
                     mutation_aspect=0.56, zorder=6))
        logo = mpimg.imread(brand.LOGO_PATH)
        ab = AnnotationBbox(OffsetImage(logo, zoom=0.22), (0.1175, 0.115),
                            frameon=False, box_alignment=(0.5, 0.5), zorder=7)
        ax.add_artist(ab)
    else:
        ax.text(0.06, 0.115, brand.CHANNEL_MARK, ha="left", va="center",
                color=p["accent"], fontsize=15, fontweight="bold", zorder=7)

    base = filename or ("thumb_" + preset_name)
    path = f"{OUT}/{base}.png"
    plt.savefig(path, facecolor=p["bg"], dpi=200)          # 1280x720
    plt.savefig(f"{OUT}/{base}_preview120.png", facecolor=p["bg"], dpi=33)  # ~211x119 legibility test
    plt.close()
    return path


if __name__ == "__main__":
    print(thumbnail("data_native", "+31", "MORE TACKLES THAN ANYONE",
                    ["MEASURING THE", "UNMEASURABLE"],
                    "AI-generated stylized\nKante goes here"))
    print(thumbnail("engraving", "205", "GAMES. ONE LEGEND.",
                    ["THE RECORD,", "EXAMINED"],
                    "AI-generated engraving\nportrait goes here"))

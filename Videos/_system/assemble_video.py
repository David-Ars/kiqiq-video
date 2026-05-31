"""
KiqIQ video assembler (fallback). Pure ffmpeg, no extra dependencies.
The primary motion layer is Remotion (_system/remotion). This stays as a
no-dependency fallback that stitches stills + narration into a 1080p MP4.

Usage:
  python assemble_video.py <episode_dir>
      reads <episode_dir>/shotlist.json if present, else auto-builds from
      <episode_dir>/charts/*.png; uses the first mp3 in <episode_dir>/script/
      as narration if present; writes <episode_dir>/<foldername>.mp4

Env knobs: KIQIQ_MOTION=0 (static, fast), KIQIQ_PRESET, KIQIQ_FPS.
"""
import os, sys, json, subprocess, tempfile, glob

W, H = 1920, 1080
FPS = int(os.environ.get("KIQIQ_FPS", "30"))
PRESET = os.environ.get("KIQIQ_PRESET", "medium")
MOTION = os.environ.get("KIQIQ_MOTION", "1") != "0"
PAD_BG = "0x0B1F3A"
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "Inter-Bold.ttf")

def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

def ffprobe_dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nokey=1:noprint_wrappers=1", path], capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except Exception:
        return 0.0

def ff_path(p):
    return p.replace("\\", "/").replace(":", "\\:")

def make_shot(img, dur, text, idx, tmp):
    out = os.path.join(tmp, f"shot_{idx:03d}.mp4")
    frames = max(1, int(round(dur * FPS)))
    base = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:{PAD_BG}")
    if MOTION:
        vf = base + (f",zoompan=z='min(zoom+0.0006,1.12)':d={frames}"
                     f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
    else:
        vf = base + f",fps={FPS}"
    if text:
        t = text.replace("\\", "").replace(":", "\\:").replace("'", "’")
        vf += (f",drawtext=fontfile='{ff_path(FONT)}':text='{t}':x=80:y=h-200:"
               f"fontsize=56:fontcolor=white:alpha='if(lt(t,0.4),t/0.4,1)':"
               f"box=1:boxcolor=0x0B1F3A@0.6:boxborderw=24")
    run(["ffmpeg", "-y", "-loop", "1", "-t", f"{dur:.3f}", "-i", img, "-vf", vf,
         "-r", str(FPS), "-c:v", "libx264", "-preset", PRESET, "-pix_fmt", "yuv420p", out])
    return out

def build(ep):
    spec_path = os.path.join(ep, "shotlist.json")
    spec = json.load(open(spec_path)) if os.path.exists(spec_path) else {}
    shots = spec.get("shots")
    if not shots:
        charts = sorted(glob.glob(os.path.join(ep, "charts", "*.png")))
        shots = [{"image": os.path.relpath(c, ep)} for c in charts]
    if not shots:
        print("no shots: add charts/*.png or a shotlist.json"); sys.exit(1)

    audio = spec.get("audio")
    if not audio:
        mp3 = sorted(glob.glob(os.path.join(ep, "script", "*.mp3")))
        audio = os.path.relpath(mp3[0], ep) if mp3 else None
    audio_abs = os.path.join(ep, audio) if audio else None

    no_dur = [s for s in shots if not s.get("dur")]
    if no_dur and audio_abs and os.path.exists(audio_abs):
        used = sum(s.get("dur", 0) for s in shots)
        each = max(2.0, (ffprobe_dur(audio_abs) - used) / len(no_dur))
        for s in no_dur:
            s["dur"] = each
    for s in shots:
        s.setdefault("dur", 5.0)

    tmp = tempfile.mkdtemp(prefix="kiqiq_")
    parts = [make_shot(os.path.join(ep, s["image"]), float(s["dur"]), s.get("text"), i, tmp)
             for i, s in enumerate(shots)]
    listf = os.path.join(tmp, "list.txt")
    open(listf, "w").write("".join(f"file '{p}'\n" for p in parts))
    silent = os.path.join(tmp, "silent.mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listf, "-c", "copy", silent])

    out = os.path.join(ep, spec.get("output") or (os.path.basename(os.path.normpath(ep)) + ".mp4"))
    if audio_abs and os.path.exists(audio_abs):
        run(["ffmpeg", "-y", "-i", silent, "-i", audio_abs, "-c:v", "copy", "-c:a", "aac",
             "-b:a", "192k", "-shortest", out])
    else:
        run(["ffmpeg", "-y", "-i", silent, "-c", "copy", out])
    print("wrote", out, f"({ffprobe_dur(out):.1f}s, {len(shots)} shots)")
    return out

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python assemble_video.py <episode_dir>"); sys.exit(1)
    build(sys.argv[1])

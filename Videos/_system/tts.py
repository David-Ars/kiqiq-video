"""
KiqIQ narration renderer (ElevenLabs). Runs on your machine; the Cowork sandbox
cannot reach the ElevenLabs API.

Setup: put your ElevenLabs API key in _system/elevenlabs.key (or set ELEVENLABS_KEY).
Usage:
  python tts.py path\\to\\script.txt           -> writes script.mp3 beside it
                                                  (auto loudness-normalised to -14 LUFS via ffmpeg)
  python tts.py path\\to\\script.txt --raw      -> skip loudness normalization
  python tts.py --list                          -> list your available voices + IDs

Voice: defaults to "George" (British documentary). Confirm/override the ID below
or with a file _system/voice.id. Lock one voice as the channel narrator.
"""
import os, sys, json, shutil, subprocess, urllib.request, urllib.error

VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"   # ElevenLabs "George" (verify with --list)
MODEL = "eleven_multilingual_v2"
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.15, "use_speaker_boost": True}

HERE = os.path.dirname(__file__)

def load_key():
    k = os.environ.get("ELEVENLABS_KEY") or os.environ.get("ELEVEN_API_KEY")
    if k: return k.strip()
    for name in ("elevenlabs.key", "elevenlabs.key.txt", "elevenlabs.txt"):
        f = os.path.join(HERE, name)
        if os.path.exists(f): return open(f, encoding="utf-8-sig").read().strip()
    return None

def voice_id():
    for name in ("voice.id", "voice.id.txt"):
        f = os.path.join(HERE, name)
        if os.path.exists(f): return open(f, encoding="utf-8-sig").read().strip()
    return VOICE_ID

def api(path, key, data=None):
    url = "https://api.elevenlabs.io" + path
    req = urllib.request.Request(url, data=data, headers={
        "xi-api-key": key, "Content-Type": "application/json", "Accept": "application/json"})
    return urllib.request.urlopen(req, timeout=120)

def list_voices(key):
    with api("/v1/voices", key) as r:
        for v in json.load(r).get("voices", []):
            print(f'{v.get("voice_id")}  {v.get("name")}')

def render(script_path, key):
    text = open(script_path, encoding="utf-8").read().strip()
    body = json.dumps({"text": text, "model_id": MODEL, "voice_settings": SETTINGS}).encode()
    url = f"/v1/text-to-speech/{voice_id()}"
    out = os.path.splitext(script_path)[0] + ".mp3"
    req = urllib.request.Request("https://api.elevenlabs.io"+url, data=body,
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=300) as r, open(out, "wb") as f:
        f.write(r.read())
    print("wrote", out)
    return out

def normalize(mp3):
    # Loudness-normalise to -14 LUFS (YouTube's normalization target, so episodes
    # play at the same level as rivals; YT attenuates louder masters but does not
    # boost quieter ones). Free equivalent of Auphonic. No-op if ffmpeg is absent.
    if not shutil.which("ffmpeg"):
        print("(skipped loudnorm: ffmpeg not found)"); return
    tmp = os.path.splitext(mp3)[0] + ".norm.mp3"
    try:
        subprocess.run(["ffmpeg", "-y", "-i", mp3, "-af",
            "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "libmp3lame", "-b:a", "192k", tmp],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.replace(tmp, mp3)
        print("normalised", mp3, "(-16 LUFS)")
    except Exception as e:
        if os.path.exists(tmp): os.remove(tmp)
        print("(loudnorm failed, kept raw audio:", e, ")")

if __name__ == "__main__":
    key = load_key()
    if not key:
        print("ERROR: no ElevenLabs key. Put it in _system/elevenlabs.key"); sys.exit(1)
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        list_voices(key); sys.exit(0)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: python tts.py path/to/script.txt   (--raw to skip loudnorm, or --list)"); sys.exit(1)
    out = render(args[0], key)
    if "--raw" not in sys.argv:
        normalize(out)

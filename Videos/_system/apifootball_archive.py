"""
API-Football archive ingester (resumable, rate-limited).

Goal: pull as much useful API-Football data as possible into a local store
before access ends. Player-centric priority, so the most valuable data for
player essays lands first if the daily budget runs out.

AUTH. Two ways to subscribe to API-Football. Set PROVIDER to match yours:
  - "apisports": the API-Football dashboard plan (api-sports.io). Header
    x-apisports-key. This is the $19/mo Pro plan with 7,500 req/day.
  - "rapidapi":  subscribed through RapidAPI. Different host and headers.

Set the key in the environment, NOT the placeholder:
  PowerShell:  $env:APIFOOTBALL_KEY="paste-your-real-key"; python apifootball_archive.py

Safe to stop and re-run. A manifest records every completed request, so a
re-run skips what is already saved and continues.
"""
import os, sys, json, time, hashlib, urllib.parse, urllib.request, urllib.error

# ------------------------------------------------------------------ config
PROVIDER = "apisports"          # "apisports" or "rapidapi"
def _load_key():
    # 1) environment variable, 2) a local file apifootball.key next to this script.
    k = os.environ.get("APIFOOTBALL_KEY") or os.environ.get("API_FOOTBALL_KEY")
    if k:
        return k.strip()
    for name in ("apifootball.key", "apifootball.key.txt", "apifootball.txt"):
        keyfile = os.path.join(os.path.dirname(__file__), name)
        if os.path.exists(keyfile):
            return open(keyfile, encoding="utf-8-sig").read().strip()
    return None

KEY = _load_key()
OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "apifootball")

if PROVIDER == "apisports":
    BASE = "https://v3.football.api-sports.io"
    AUTH_HEADERS = {"x-apisports-key": KEY or ""}
elif PROVIDER == "rapidapi":
    BASE = "https://api-football-v1.p.rapidapi.com/v3"
    AUTH_HEADERS = {"x-rapidapi-key": KEY or "",
                    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"}
else:
    raise ValueError("PROVIDER must be 'apisports' or 'rapidapi'")

LEAGUES = {
    39: "Premier League", 140: "La Liga", 135: "Serie A",
    78: "Bundesliga", 61: "Ligue 1", 2: "UCL", 3: "UEL",
    88: "Eredivisie", 94: "Primeira Liga", 40: "Championship",
    1: "World Cup", 4: "Euros", 9: "Copa America", 5: "Nations League",
}
SEASONS = list(range(2010, 2026))

PULL_FIXTURES = True
PULL_PLAYER_CAREER = True
PULL_FIXTURE_EVENTS = False

DELAY = 0.4
DAILY_CAP = 7500
MINUTE_FLOOR = 3

# ------------------------------------------------------------------ plumbing
_PLACEHOLDER_WORDS = ("your", "here", "placeholder", "paste", "actual", "example", "real-key")
def _is_placeholder(k):
    if not k:
        return True
    kl = k.strip().lower()
    return any(w in kl for w in _PLACEHOLDER_WORDS)

if _is_placeholder(KEY):
    print("ERROR: no real API key found. You are still passing placeholder text, not your key.")
    print("Do ONE of these:")
    print('  A) put the key in a file:  create  _system\\apifootball.key  containing only your key, then:')
    print("        python apifootball_archive.py")
    print('  B) set the env var to the REAL key value (the long code from your dashboard):')
    print('        $env:APIFOOTBALL_KEY="paste_the_actual_code"; python apifootball_archive.py')
    print("Get the key: api-sports.io dashboard (Account) for PROVIDER='apisports', or the")
    print("X-RapidAPI-Key in your RapidAPI dashboard for PROVIDER='rapidapi'.")
    sys.exit(1)
if not (len(KEY) >= 20 and KEY.isalnum()):
    print(f"  note: the key does not look like a typical API-Football key (expected ~32 hex chars). Proceeding anyway.")

os.makedirs(OUT, exist_ok=True)
MANIFEST = os.path.join(OUT, "_manifest.json")
manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
made = 0

def _key(endpoint, params):
    raw = endpoint + "?" + urllib.parse.urlencode(sorted(params.items()))
    return hashlib.md5(raw.encode()).hexdigest(), raw

def get(endpoint, **params):
    global made
    h, raw = _key(endpoint, params)
    if h in manifest:
        return json.load(open(os.path.join(OUT, manifest[h])))
    if made >= DAILY_CAP:
        print(f"[stop] daily cap {DAILY_CAP} reached. Re-run tomorrow to continue.")
        save_manifest(); sys.exit(0)
    url = BASE + endpoint + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers=AUTH_HEADERS)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                body = json.load(r)
                rem_min = r.headers.get("X-RateLimit-Remaining")
                rem_day = r.headers.get("x-ratelimit-requests-remaining")
            # api-sports returns 200 with an 'errors' field for auth/quota problems
            errs = body.get("errors")
            if errs and (("token" in errs) or ("key" in errs) or ("plan" in errs)):
                print(f"[auth] API rejected the request: {errs}")
                print("Check the key is correct and PROVIDER matches your subscription.")
                save_manifest(); sys.exit(1)
            made += 1
            sub = endpoint.strip("/").replace("/", "_")
            os.makedirs(os.path.join(OUT, sub), exist_ok=True)
            fn = os.path.join(sub, h + ".json")
            json.dump(body, open(os.path.join(OUT, fn), "w"))
            manifest[h] = fn
            if made % 25 == 0:
                save_manifest()
                print(f"  {made} calls | day-remaining={rem_day} | {raw[:70]}")
            if rem_min is not None and rem_min.isdigit() and int(rem_min) <= MINUTE_FLOOR:
                print("  per-minute limit near, sleeping 60s"); time.sleep(60)
            else:
                time.sleep(DELAY)
            return body
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                pass
            if e.code in (401, 403):
                print(f"[auth] HTTP {e.code} from {BASE}. Server said: {detail or '(no body)'}")
                print("Fix one of these:")
                print(" 1) Use your REAL key, not the placeholder.")
                print(" 2) PROVIDER must match how you subscribed: 'apisports' (api-sports.io dashboard)")
                print("    or 'rapidapi' (subscribed via RapidAPI). They use different hosts and headers.")
                save_manifest(); sys.exit(1)
            wait = 5 * (attempt + 1)
            print(f"  retry {attempt+1} after HTTP {e.code}: {detail[:120]} (sleep {wait}s)")
            time.sleep(wait)
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"  retry {attempt+1} after error: {e} (sleep {wait}s)")
            time.sleep(wait)
    print(f"[skip] gave up on {raw}")
    return {"response": []}

def save_manifest():
    json.dump(manifest, open(MANIFEST, "w"))

def players_paged(**params):
    page, out = 1, []
    while True:
        body = get("/players", page=page, **params)
        out += body.get("response", [])
        paging = body.get("paging", {})
        if page >= paging.get("total", 1):
            break
        page += 1
    return out

# ------------------------------------------------------------------ pipeline
def run():
    print(f"provider={PROVIDER}  base={BASE}")
    print("status check..."); print(" ", get("/status").get("response", "?"))
    print("leagues catalogue..."); get("/leagues")

    for lid, name in LEAGUES.items():
        for yr in SEASONS:
            get("/standings", league=lid, season=yr)
            for tops in ("topscorers", "topassists", "topyellowcards", "topredcards"):
                get(f"/players/{tops}", league=lid, season=yr)
            get("/teams", league=lid, season=yr)

    seen_players = set()
    for lid, name in LEAGUES.items():
        for yr in SEASONS:
            for pl in players_paged(league=lid, season=yr):
                pid = (pl.get("player") or {}).get("id")
                if pid:
                    seen_players.add(pid)

    if PULL_FIXTURES:
        for lid in LEAGUES:
            for yr in SEASONS:
                get("/fixtures", league=lid, season=yr)

    if PULL_PLAYER_CAREER:
        for pid in sorted(seen_players):
            get("/transfers", player=pid)
            get("/trophies", player=pid)
            get("/sidelined", player=pid)

    save_manifest()
    print(f"DONE this run. total calls made: {made}. players seen: {len(seen_players)}.")

if __name__ == "__main__":
    run()

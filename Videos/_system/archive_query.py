"""
Query the local API-Football archive (the JSON dump in ../_data/apifootball).

Used by the researcher and chart-builder so they never hand-parse the raw
hash-named files. Importable functions plus a CLI.

CLI:
  python archive_query.py coverage
  python archive_query.py find "Kante"
  python archive_query.py player 1234
  python archive_query.py leaderboard 39 2015 tackles 10
  python archive_query.py scorers 39 2015
  python archive_query.py standings 39 2015

Stat keys: goals assists tackles interceptions blocks shots key_passes
           passes dribbles duels_won minutes apps rating yellows reds
Reminder: API-Football is Tier 3. Cross-check thesis-critical figures.
"""
import os, sys, json, glob

ROOT = os.path.join(os.path.dirname(__file__), "..", "_data", "apifootball")
PLAYERS = os.path.join(ROOT, "players")

STAT_PATH = {
    "goals":("goals","total"), "assists":("goals","assists"),
    "tackles":("tackles","total"), "interceptions":("tackles","interceptions"),
    "blocks":("tackles","blocks"), "shots":("shots","total"),
    "key_passes":("passes","key"), "passes":("passes","total"),
    "dribbles":("dribbles","success"), "duels_won":("duels","won"),
    "minutes":("games","minutes"), "apps":("games","appearences"),
    "rating":("games","rating"), "yellows":("cards","yellow"), "reds":("cards","red"),
}

def _g(d, *path, default=None):
    for k in path:
        if not isinstance(d, dict): return default
        d = d.get(k)
    return d if d is not None else default

def _iter_player_files():
    for f in glob.glob(os.path.join(PLAYERS, "*.json")):
        try:
            yield json.load(open(f, encoding="utf-8"))
        except Exception:
            continue

def coverage():
    seen = {}
    for body in _iter_player_files():
        pr = body.get("parameters", {})
        key = (pr.get("league"), pr.get("season"))
        seen[key] = seen.get(key, 0) + len(body.get("response", []))
    return sorted((str(l), str(s), n) for (l, s), n in seen.items())

def find(name):
    name = name.lower(); out = {}
    for body in _iter_player_files():
        for it in body.get("response", []):
            pl = it.get("player", {})
            nm = (pl.get("name") or "")
            if name in nm.lower():
                pid = pl.get("id")
                rec = out.setdefault(pid, {"id": pid, "name": nm,
                        "nationality": pl.get("nationality"), "seasons": set()})
                for st in it.get("statistics", []):
                    rec["seasons"].add((_g(st,"league","id"), _g(st,"league","season")))
    for r in out.values():
        r["seasons"] = sorted(str(x) for x in r["seasons"])
    return list(out.values())

def player_seasons(pid):
    rows = {}
    for body in _iter_player_files():
        for it in body.get("response", []):
            if (it.get("player") or {}).get("id") != pid: continue
            for st in it.get("statistics", []):
                key = (_g(st,"league","season"), _g(st,"league","id"), _g(st,"team","id"))
                rows[key] = {
                    "season": _g(st,"league","season"), "league": _g(st,"league","name"),
                    "team": _g(st,"team","name"), "apps": _g(st,"games","appearences"),
                    "minutes": _g(st,"games","minutes"), "goals": _g(st,"goals","total"),
                    "assists": _g(st,"goals","assists"), "tackles": _g(st,"tackles","total"),
                    "interceptions": _g(st,"tackles","interceptions"),
                    "yellows": _g(st,"cards","yellow"), "reds": _g(st,"cards","red"),
                    "rating": _g(st,"games","rating"),
                }
    return [rows[k] for k in sorted(rows, key=lambda k: (str(k[0]), str(k[1])))]

def leaderboard(league, season, stat, n=10):
    league, season = int(league), int(season)
    path = STAT_PATH.get(stat)
    if not path: raise SystemExit(f"unknown stat '{stat}'. options: {list(STAT_PATH)}")
    best = {}
    for body in _iter_player_files():
        pr = body.get("parameters", {})
        if str(pr.get("league")) != str(league) or str(pr.get("season")) != str(season):
            continue
        for it in body.get("response", []):
            pid = (it.get("player") or {}).get("id"); nm = _g(it,"player","name")
            for st in it.get("statistics", []):
                if _g(st,"league","id") != league: continue
                v = _g(st, *path)
                try: v = float(v)
                except (TypeError, ValueError): continue
                if pid not in best or v > best[pid][1]:
                    best[pid] = (nm, v)
    ranked = sorted(best.values(), key=lambda x: x[1], reverse=True)[:int(n)]
    return ranked

def _read_dir(sub, league, season):
    out = []
    for f in glob.glob(os.path.join(ROOT, sub, "*.json")):
        try: body = json.load(open(f, encoding="utf-8"))
        except Exception: continue
        pr = body.get("parameters", {})
        if str(pr.get("league")) == str(league) and str(pr.get("season")) == str(season):
            out.append(body)
    return out

def scorers(league, season, n=10):
    for body in _read_dir("players_topscorers", league, season):
        rows = [(_g(it,"player","name"), _g(it,"statistics",0,"goals","total"))
                for it in body.get("response", [])]
        return rows[:int(n)]
    return []

def standings(league, season):
    for body in _read_dir("standings", league, season):
        resp = body.get("response", [])
        if resp:
            table = _g(resp[0], "league", "standings", default=[[]])
            return [(r.get("rank"), _g(r,"team","name"), r.get("points")) for r in table[0]]
    return []

def _print(x): print(json.dumps(x, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    cmd = a[0]
    if cmd == "coverage":
        for l, s, n in coverage(): print(f"league {l}  season {s}  players {n}")
    elif cmd == "find": _print(find(" ".join(a[1:])))
    elif cmd == "player": _print(player_seasons(int(a[1])))
    elif cmd == "leaderboard":
        for nm, v in leaderboard(a[1], a[2], a[3], a[4] if len(a) > 4 else 10):
            print(f"{v:>8}  {nm}")
    elif cmd == "scorers":
        for nm, v in scorers(a[1], a[2]): print(f"{v:>4}  {nm}")
    elif cmd == "standings":
        for rk, nm, pts in standings(a[1], a[2]): print(f"{rk:>2}  {nm:<24} {pts}")
    else: print("unknown command"); print(__doc__)

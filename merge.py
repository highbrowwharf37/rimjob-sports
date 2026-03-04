import json, datetime, urllib.request

# Fetch team data
req = urllib.request.Request(
    'https://barttorvik.com/2026_team_results.json',
    headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'}
)
with urllib.request.urlopen(req) as r:
    teams = json.loads(r.read().decode())

print(f"Total teams: {len(teams)}")

# Try multiple player URLs
player_urls = [
    'https://barttorvik.com/playerstat.php?year=2026&json=1&minmin=50',
    'https://barttorvik.com/playerstat.php?year=2026&json=1&minmin=1',
    'https://barttorvik.com/playerstat.php?year=2026&json=1',
]

players = []
for url in player_urls:
    try:
        req2 = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req2, timeout=30) as r:
            content = r.read().decode().strip()
            print(f"Raw response from {url}: {content[:200]}")
            data = json.loads(content)
            if isinstance(data, dict):
                data = data.get('data', data.get('players', []))
            if len(data) > 0:
                players = data
                print(f"Got {len(players)} players!")
                break
    except Exception as e:
        print(f"Failed {url}: {e}")

out = {
    'teams': teams,
    'players': players,
    'updated': datetime.datetime.now(datetime.timezone.utc).isoformat()
}

with open('data.json', 'w') as f:
    json.dump(out, f)

print("Done!")

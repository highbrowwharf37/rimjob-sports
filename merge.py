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
    'https://barttorvik.com/playerstat.php?year=2026&json=1',
    'https://barttorvik.com/2026_player_results.json',
]

players = []
for url in player_urls:
    try:
        req2 = urllib.request.Request(url, headers=

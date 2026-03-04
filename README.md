# CBB Analytics + NBA Live

This repo contains two frontend experiences:

1. `cbb-data` — a React + TypeScript NCAA basketball analytics dashboard.
2. `nba-live` — a standalone NBA live game tracker (schedule, play-by-play, and player stats) powered by Sportradar.

## What Is Included

### CBB dashboard (`/cbb-data.html`)

- Power rankings
- Efficiency analysis
- Schedule strength
- Game predictor
- Bubble tracker
- Momentum
- Head-to-head comparison
- Upset alerts
- Conference strength
- Cinderella watch
- Draft board

### NBA live tracker (`/nba_live/nba-live.html`)

- Date-based NBA schedule browsing
- Live play-by-play feed
- Team logos (local assets with CDN fallback)
- Team context under scoreboard (record / standings when available)
- Player box-score style stat tables
- Side-by-side PBP + player stats layout (desktop)
- Show/hide left games menu toggle
- Final score hydration for completed games
- Adaptive request throttling with backoff for trial-rate-limited APIs

## Tech Stack

- React 18
- TypeScript
- Vite
- Plain HTML/CSS/JS page under `public/` for NBA live

## Local Development

### Prerequisites

- Node.js 18+
- npm
- Python 3 (only for manual CBB data refresh script)

### Install

```bash
npm install
```

### Start dev server

```bash
npm run dev
```

Then open:

- CBB dashboard: `http://localhost:5173/cbb-data.html`
- NBA live tracker: `http://localhost:5173/nba_live/nba-live.html`

Legacy redirect routes also exist:

- `http://localhost:5173/cbb_data.html`
- `http://localhost:5173/cbb_data/`
- `http://localhost:5173/nba-live.html`

## Data & Asset Scripts

### Refresh CBB source data

```bash
python3 scripts/fetch-data/fetch_cbb_data.py
```

Writes to `data/data.json`.

### Download NBA team logos locally

```bash
./scripts/fetch-data/fetch_nba_logos.sh
```

Downloads PNGs into `public/nba_live/logos/`.

## NBA Live API Notes

The NBA live page is currently configured for Sportradar trial access in:

- `public/nba_live/nba-live.html`

Key points:

- Trial access is rate-limited and may return `429`.
- The page uses an adaptive queue that increases pace when stable and backs off on throttling.
- Optional proxy support exists in `proxy/server.js` and `proxy/startup-script.sh`.

## Project Structure

```text
.
├── data/
│   └── data.json
├── proxy/
│   ├── server.js
│   └── startup-script.sh
├── public/
│   ├── cbb-data.html
│   ├── cbb_data.html                # redirect
│   ├── cbb_data/index.html          # redirect
│   ├── nba-live.html                # redirect
│   └── nba_live/
│       ├── nba-live.html
│       └── logos/
├── scripts/
│   └── fetch-data/
│       ├── fetch_cbb_data.py
│       └── fetch_nba_logos.sh
├── src/
│   ├── components/
│   │   ├── layout/
│   │   ├── tabs/
│   │   └── ui/
│   ├── data/
│   ├── hooks/
│   ├── styles/
│   ├── types/
│   ├── utils/
│   ├── App.tsx
│   └── main.tsx
├── package.json
└── README.md
```

## Commands

- `npm run dev` — start Vite dev server
- `npm run build` — type-check + Vite build
- `npm run preview` — preview production build

## Data Sources

- Barttorvik: https://barttorvik.com
- Sportradar NBA v8: https://developer.sportradar.com/docs/read/basketball/NBA_v8

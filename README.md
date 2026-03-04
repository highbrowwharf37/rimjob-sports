# CBB Analytics — College Basketball Rankings

A React and Vite-based web application providing comprehensive analytics, power rankings, game prediction, and advanced metrics for college basketball (NCAA MBB).

## Features

- **Power Rankings**: Up-to-date adjusted rankings for all teams, displaying stats like Offensive and Defensive Efficiency.
- **Efficiency Analysis**: Compare offensive vs defensive statistics dynamically.
- **Schedule Strength**: See whose schedule has tested them the most (SOS metrics).
- **Game Predictor**: Simulate head-to-head match-ups using adjusted efficiency margins.
- **Bubble Tracker**: Track "On the Bubble" teams vying for a spot in tournament play.
- **Momentum**: Analyze team performances specifically over recent games.
- **Head-to-Head**: Direct comparison of any two teams.
- **Upset Alerts**: Find potential trap games and potential upsets based on recent metrics.
- **Conference Strength**: Overview of conference-wide metrics.
- **Cinderella Watch**: Identify mid-majors and low-majors that have the analytical profile of a bracket buster.
- **Draft Board**: Track potential draft prospects.

## Tech Stack

- **Frontend**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite
- **Data Scripting**: Python (fetching from Barttorvik & NCAA stats APIs)

## Project Structure

- `src/`: Contains the React components (`components/`), app logic (`hooks/`), types, and styling.
- `scripts/fetch-data/fetch_cbb_data.py`: A Python script containing the data ingestion logic capable of fetching live stats from Barttorvik and NCAA.
- `data/`: Contains the cached/stored data (e.g., `data.json`) obtained by the python script.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+ recommended)
- [Python 3+](https://www.python.org/) (specifically for fetching/updating data)

### Installation

1. Install JavaScript dependencies using npm:
   ```bash
   npm install
   ```

2. Start the Vite development server:
   ```bash
   npm run dev
   ```

3. Open your browser and navigate to the local URL (usually `http://localhost:5173`).

### Updating Data

Currently, the basketball metrics and statistics can be updated by running the included python script:
```bash
# From the root directory:
python3 scripts/fetch-data/fetch_cbb_data.py
```
*Note: This contacts external APIs and endpoints; if the NCAA endpoint blocks the request, fallbacks may be required.*

## Build for Production

To create a production-ready build:
```bash
npm run build
```
This transpiles TypeScript and bundles your application into the `dist` directory. You can preview the production build with:
```bash
npm run preview
```

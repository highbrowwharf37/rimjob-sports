#!/usr/bin/env python3
"""
Convert NBA stats CSV files to JSON format for the HTML dashboard.
Run this script to generate JSON files that the nba_stats.html page will load.
"""

import csv
import json
import shutil
from pathlib import Path


def csv_to_json(csv_file):
    """Convert a CSV file to a list of dictionaries."""
    data = []
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
    return data


def write_json_to_targets(data, file_name, output_dirs):
    primary_output = output_dirs[0] / file_name
    with open(primary_output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    for mirror_dir in output_dirs[1:]:
        shutil.copy2(primary_output, mirror_dir / file_name)

    return primary_output


def main():
    root_dir = Path(__file__).resolve().parent.parent
    candidate_data_dirs = [
        root_dir / "Past FBB Data",
        root_dir / "Past Fantasy Data",
    ]
    data_dir = next((path for path in candidate_data_dirs if path.exists()), candidate_data_dirs[0])
    output_dirs = [
        root_dir / "nba_data",
        root_dir / "frontend" / "public" / "nba_data",
    ]

    for output_dir in output_dirs:
        output_dir.mkdir(parents=True, exist_ok=True)

    full_csv = data_dir / "nba_stats_full.csv"
    if full_csv.exists():
        full_data = csv_to_json(full_csv)
        output_file = write_json_to_targets(full_data, "nba_stats_full.json", output_dirs)
        print(f"Created {output_file} ({len(full_data)} records)")
    else:
        print(f"File not found: {full_csv}")

    seasons = []
    for csv_file in sorted(data_dir.glob("nba_stats_*.csv")):
        if "full" in csv_file.name:
            continue
        season = csv_file.stem.replace("nba_stats_", "")
        seasons.append(season)

        data = csv_to_json(csv_file)
        output_file = write_json_to_targets(data, f"nba_stats_{season}.json", output_dirs)
        print(f"Created {output_file} ({len(data)} records)")

    manifest = {
        "years": sorted(seasons, reverse=True),
        "last_updated": str(full_csv.stat().st_mtime) if full_csv.exists() else None,
    }
    manifest_file = write_json_to_targets(manifest, "manifest.json", output_dirs)
    print(f"\nCreated {manifest_file}")
    print(f"Available seasons: {', '.join(manifest['years'])}")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
set -euo pipefail

out_dir="${1:-public/nba_live/logos}"
base_url="https://a.espncdn.com/i/teamlogos/nba/500"
teams=(atl bkn bos cha chi cle dal den det gsw hou ind lac lal mem mia mil min nop nyk okc orl phi phx por sac sas tor uta was)

mkdir -p "$out_dir"

for abbr in "${teams[@]}"; do
  remote_abbr="$abbr"
  if [[ "$abbr" == "nop" ]]; then remote_abbr="no"; fi
  if [[ "$abbr" == "uta" ]]; then remote_abbr="utah"; fi

  src="${base_url}/${remote_abbr}.png"
  dest="${out_dir}/${abbr}.png"
  echo "downloading ${abbr}..."
  curl -fsSL "$src" -o "$dest"
done

echo "done: downloaded ${#teams[@]} logos to ${out_dir}"

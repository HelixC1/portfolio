#!/usr/bin/env python3
"""FLIGHT-LOGGER EDGE — Analyse CSV de vol."""

import argparse
import csv
import sys
from pathlib import Path


def analyze(path: Path) -> None:
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    if not rows:
        print("Fichier vide.")
        sys.exit(1)

    altitudes = [float(r["altitude_m"]) for r in rows]
    speeds = [float(r.get("ground_speed_kts", 0)) for r in rows]

    print(f"Fichier      : {path.name}")
    print(f"Points       : {len(rows)}")
    print(f"Alt. min/max : {min(altitudes):.0f} / {max(altitudes):.0f} m")
    print(f"Vitesse moy. : {sum(speeds)/len(speeds):.1f} kts")
    print(f"Durée        : {float(rows[-1]['timestamp_s']) - float(rows[0]['timestamp_s']):.0f} s")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyse log de vol CSV")
    parser.add_argument("csv_file", type=Path, help="Chemin vers le CSV")
    args = parser.parse_args()
    analyze(args.csv_file)


if __name__ == "__main__":
    main()

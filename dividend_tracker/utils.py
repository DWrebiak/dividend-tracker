# ------------
# CSV UTILITIES
# ------------

import csv
from typing import List, Dict

def save_dividends_to_csv(data: List[Dict], filename: str):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")

# ---------------------
# CONFIG FILE UTILITIES
# ---------------------

import argparse
import json
import os
import sys

def load_config():
    parser = argparse.ArgumentParser(description="Dividend Tracker")
    parser.add_argument(
        "--config",
        default="config/config.json",
        help="Path to configuration file (default: config/config.json)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.config):
        print(f"[ERROR] Config file not found: {args.config}")
        sys.exit(1)

    with open(args.config, "r") as f:
        config = json.load(f)

    return config

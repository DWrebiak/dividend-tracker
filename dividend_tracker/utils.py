# ------------
# CSV UTILITIES
# ------------

import csv
from typing import List, Dict
from pathlib import Path
from datetime import datetime

def save_dividends_to_csv(data: List[Dict], configname: str):
    if not data:
        print("No data to save.")
        return

    export_dir = Path("exports")
    export_dir.mkdir(exist_ok=True)

    config_name = Path(configname).stem

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    filename = f"{timestamp}_dividend_data_{config_name}.csv"
    file_path = export_dir / filename

    keys = data[0].keys()

    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
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
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Run script in a loop every 24 hours"
    )
    args = parser.parse_args()

    config_path = args.config
    loop_mode = args.loop

    if not os.path.isfile(config_path):
        print(f"[ERROR] Config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r") as f:
        config = json.load(f)

    return config, config_path, loop_mode

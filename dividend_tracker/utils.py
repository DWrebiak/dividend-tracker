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

"""Download World Bank WDI international migrant stock indicator."""
import argparse
from pathlib import Path
import requests
import pandas as pd

BASE = "https://api.worldbank.org/v2/country/all/indicator/SM.POP.TOTL"

def fetch(output):
    r = requests.get(BASE, params={"format": "json", "per_page": 20000}, timeout=60)
    r.raise_for_status()
    payload = r.json()[1]
    df = pd.DataFrame(payload)
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
    print(f"Saved {len(df)} World Bank records to {output}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--output", default="data/raw/world_bank.csv")
    a = p.parse_args(); fetch(a.output)

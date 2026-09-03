"""Download UNHCR Refugee Data Finder data via its public API.
See: https://www.unhcr.org/refugee-statistics/insights/explainers/forcibly-displaced-api.html
"""
import argparse
from pathlib import Path
import requests

API = "https://api.unhcr.org/population/v1/population/"

def fetch(year_from, year_to, output):
    params = {"yearFrom": year_from, "yearTo": year_to, "limit": 1000}
    r = requests.get(API, params=params, timeout=60)
    r.raise_for_status()
    data = r.json().get("items", [])
    import pandas as pd
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(data).to_csv(output, index=False)
    print(f"Saved {len(data)} UNHCR records to {output}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--from-year", type=int, default=2020)
    p.add_argument("--to-year", type=int, default=2025)
    p.add_argument("--output", default="data/raw/unhcr.csv")
    a = p.parse_args(); fetch(a.from_year, a.to_year, a.output)

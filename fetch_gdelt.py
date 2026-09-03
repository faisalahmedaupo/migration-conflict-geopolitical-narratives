"""Fetch a small GDELT DOC 2.0 news sample for exploratory research.
Use the official GDELT documentation and respect service limits/terms.
"""
import argparse
from pathlib import Path
import requests
import pandas as pd

URL = "https://api.gdeltproject.org/api/v2/doc/doc"

def fetch(query, output, timespan="7d", maxrecords=250):
    params = {"query": query, "mode": "artlist", "format": "json", "maxrecords": maxrecords, "timespan": timespan, "sort": "datedesc"}
    r = requests.get(URL, params=params, timeout=60)
    r.raise_for_status()
    articles = r.json().get("articles", [])
    df = pd.DataFrame(articles)
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, index=False)
    print(f"Saved {len(df)} GDELT article records to {output}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--query", default="refugee conflict migration"); p.add_argument("--output", default="data/raw/gdelt_live_sample.csv"); p.add_argument("--timespan", default="7d")
    a = p.parse_args(); fetch(a.query, a.output, a.timespan)

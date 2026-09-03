from pathlib import Path
import random
import pandas as pd

random.seed(42)
root = Path(__file__).resolve().parents[1]
out = root / "data" / "raw"
out.mkdir(parents=True, exist_ok=True)

cases = {
    "Ukraine": ["refugee", "security", "border", "humanitarian", "diplomacy"],
    "Rohingya": ["refugee", "humanitarian", "border", "responsibility", "security"],
    "MiddleEast": ["security", "humanitarian", "diplomacy", "border", "refugee"],
}
rows = []
for case, terms in cases.items():
    for i in range(180):
        date = pd.Timestamp("2022-01-01") + pd.Timedelta(days=random.randint(0, 1095))
        selected = random.sample(terms, k=random.choice([1, 2]))
        text = "Migration reporting discusses " + " and ".join(selected) + " in the context of conflict."
        rows.append({"date": date, "case": case, "text": text, "source": "SYNTHETIC_DEMO"})
pd.DataFrame(rows).to_csv(out / "gdelt_articles.csv", index=False)

unhcr = []
for case in cases:
    for year in range(2022, 2026):
        unhcr.append({"year": year, "case": case, "refugees": random.randint(50000, 900000), "displaced": random.randint(100000, 1500000), "source": "SYNTHETIC_DEMO"})
pd.DataFrame(unhcr).to_csv(out / "unhcr.csv", index=False)

acled = []
for case in cases:
    for month in pd.date_range("2022-01-01", "2025-12-01", freq="MS"):
        acled.append({"date": month, "case": case, "event_count": random.randint(5, 100), "fatalities": random.randint(0, 250), "source": "SYNTHETIC_DEMO"})
pd.DataFrame(acled).to_csv(out / "acled.csv", index=False)

print("Created synthetic demo datasets. They must not be presented as empirical findings.")

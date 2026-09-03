import re
import pandas as pd

def clean_text(text):
    text = "" if pd.isna(text) else str(text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text

def prepare_articles(df):
    out = df.copy()
    if "text" in out.columns:
        out["clean_text"] = out["text"].map(clean_text)
    if "date" in out.columns:
        out["date"] = pd.to_datetime(out["date"], errors="coerce")
    return out

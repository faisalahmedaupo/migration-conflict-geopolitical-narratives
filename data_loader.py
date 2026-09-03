from pathlib import Path
import pandas as pd

def load_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)

def load_optional(path):
    path = Path(path)
    return pd.read_csv(path) if path.exists() else pd.DataFrame()

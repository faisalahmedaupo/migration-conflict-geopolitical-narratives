import pandas as pd

def zscore(series):
    s = pd.Series(series, dtype=float)
    std = s.std(ddof=0)
    return (s - s.mean()) / std if std else s * 0

def exploratory_geopolitical_index(df, columns, weights=None):
    """Exploratory standardized composite; report components alongside it."""
    weights = weights or {c: 1 / len(columns) for c in columns}
    parts = {c: zscore(df[c]) * weights.get(c, 0) for c in columns}
    return pd.DataFrame(parts).sum(axis=1)

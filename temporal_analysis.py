import pandas as pd

def monthly_frame_rates(df, date_col="date", frame_cols=None):
    if frame_cols is None:
        frame_cols = [c for c in df.columns if c.startswith("frame_")]
    out = df.copy()
    out[date_col] = pd.to_datetime(out[date_col], errors="coerce")
    out = out.dropna(subset=[date_col]).set_index(date_col)
    return out[frame_cols].resample("MS").mean().reset_index()

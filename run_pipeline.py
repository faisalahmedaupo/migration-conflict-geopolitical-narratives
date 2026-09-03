from pathlib import Path
import sys
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.config import load_config
from src.preprocess import prepare_articles
from src.narrative_analysis import frame_scores
from src.validation import validation_report
from src.visualization import save_frame_bar

cfg = load_config()
root = Path(__file__).resolve().parents[1]
raw = root / cfg["paths"]["raw"]
processed = root / cfg["paths"]["processed"]
figures = root / cfg["paths"]["figures"]
processed.mkdir(parents=True, exist_ok=True); figures.mkdir(parents=True, exist_ok=True)

articles = pd.read_csv(raw / "gdelt_articles.csv")
print("Validation:", validation_report(articles))
articles = prepare_articles(articles)

scores = articles["clean_text"].apply(lambda x: frame_scores(x, cfg["frames"]))
score_df = pd.DataFrame(scores.tolist()).fillna(0)
for col in score_df:
    articles[f"frame_{col}"] = score_df[col]

articles.to_csv(processed / "articles_scored.csv", index=False)
frame_counts = score_df.sum().sort_values(ascending=False)
save_frame_bar(frame_counts, figures / "frame_prevalence_demo.png")
frame_counts.to_csv(processed / "frame_counts_demo.csv")
print("Pipeline complete. Outputs are illustrative if source is SYNTHETIC_DEMO.")

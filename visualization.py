from pathlib import Path
import matplotlib.pyplot as plt

def save_frame_bar(frame_counts, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    frame_counts.plot(kind="bar", ax=ax)
    ax.set_title("Illustrative geopolitical frame prevalence")
    ax.set_ylabel("Count")
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)

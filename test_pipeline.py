from pathlib import Path
import subprocess, sys

def test_demo_pipeline():
    root = Path(__file__).resolve().parents[1]
    subprocess.run([sys.executable, str(root / "scripts" / "generate_demo_data.py")], check=True)
    subprocess.run([sys.executable, str(root / "scripts" / "run_pipeline.py")], check=True)
    assert (root / "data/processed/articles_scored.csv").exists()

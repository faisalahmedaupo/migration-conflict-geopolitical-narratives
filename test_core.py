import pandas as pd
from src.narrative_analysis import frame_scores, assign_frames
from src.validation import validate_required_columns

def test_frame_scores():
    lex = {"security": ["security", "border"], "humanitarian": ["refugee", "aid"]}
    s = frame_scores("refugee security border", lex)
    assert s["security"] == 2
    assert s["humanitarian"] == 1

def test_assign_frames():
    lex = {"security": ["security"], "humanitarian": ["refugee"]}
    assert assign_frames("security security", lex) == ["security"]

def test_validation():
    assert validate_required_columns(pd.DataFrame({"a": [1]}), ["a"])

import re


def frame_scores(text, frame_lexicons):
    text = str(text).lower()
    tokens = set(re.findall(r"[a-zA-Z][a-zA-Z-]+", text))
    scores = {}
    for frame, terms in frame_lexicons.items():
        hits = sorted(tokens.intersection(set(t.lower() for t in terms)))
        scores[frame] = len(hits)
    return scores


def assign_frames(text, frame_lexicons):
    scores = frame_scores(text, frame_lexicons)
    max_score = max(scores.values(), default=0)
    return [k for k, v in scores.items() if v == max_score and v > 0]

from collections import Counter
import re


def normalize_actor(name):
    return re.sub(r"\s+", " ", str(name).strip().lower())


def actor_counts(values):
    return Counter(normalize_actor(v) for v in values if str(v).strip())


def cooccurrence_edges(actor_lists):
    edges = Counter()
    for actors in actor_lists:
        unique = sorted(set(normalize_actor(a) for a in actors if str(a).strip()))
        for i, a in enumerate(unique):
            for b in unique[i + 1:]:
                edges[(a, b)] += 1
    return edges

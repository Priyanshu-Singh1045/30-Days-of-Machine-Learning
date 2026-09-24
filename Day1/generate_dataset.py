"""
generate_dataset.py
--------------------
Creates a synthetic "StreamFlix" content-ratings dataset for Day 1 of the
30 Days of Machine Learning challenge (Descriptive Statistics).

The distribution is deliberately skewed: most titles cluster in the
6-8 range, but a long tail of poorly-produced / abandoned titles sits at
1-2 stars. This mirrors a common real-world pattern (streaming platforms,
app store reviews, e-commerce products) where the MEAN understates typical
quality because it gets dragged down by a minority of very low scores.

Run:  python generate_dataset.py
Output: data/streaming_ratings.csv
"""

import numpy as np
import pandas as pd

np.random.seed(42)

N_TITLES = 1200

GENRES = ["Drama", "Comedy", "Action", "Documentary", "Thriller",
          "Romance", "Sci-Fi", "Horror", "Kids", "Reality"]

CONTENT_TYPES = ["Movie", "Series"]


def make_title_names(n):
    adjectives = ["Silent", "Broken", "Last", "Hidden", "Golden", "Dark",
                  "Endless", "Forgotten", "Rising", "Lost", "Crimson", "Quiet"]
    nouns = ["Horizon", "Kingdom", "Echo", "Shadows", "Harbor", "Legacy",
             "Signal", "Garden", "Empire", "Witness", "Voyage", "Ember"]
    rng = np.random.default_rng(7)
    return [f"{rng.choice(adjectives)} {rng.choice(nouns)} {i}" for i in range(n)]


def generate_ratings(n):
    """
    Mixture distribution:
      - 82% of titles: 'normal' catalogue quality ~ Beta scaled to 5.5-9.5
      - 18% of titles: 'long tail' low-quality / abandoned content ~ 1-3
    This is what creates the mean/median gap highlighted in the Day 1 post.
    """
    n_normal = int(n * 0.82)
    n_tail = n - n_normal

    normal_ratings = 5.5 + np.random.beta(2, 2, n_normal) * 4.0      # ~5.5 - 9.5
    tail_ratings = 1.0 + np.random.beta(1.5, 3.0, n_tail) * 2.0      # ~1.0 - 3.0

    ratings = np.concatenate([normal_ratings, tail_ratings])
    np.random.shuffle(ratings)
    return np.round(ratings, 1)


def generate_num_ratings(n):
    # Number of user ratings per title - also skewed (most titles have few
    # ratings, a handful of hits have tens of thousands).
    return np.round(np.random.lognormal(mean=5.5, sigma=1.4, size=n)).astype(int).clip(10, 50000)


def main():
    ratings = generate_ratings(N_TITLES)
    num_ratings = generate_num_ratings(N_TITLES)
    genres = np.random.choice(GENRES, size=N_TITLES, p=[
        0.16, 0.13, 0.14, 0.08, 0.12, 0.10, 0.09, 0.07, 0.06, 0.05
    ])
    content_type = np.random.choice(CONTENT_TYPES, size=N_TITLES, p=[0.6, 0.4])
    release_year = np.random.randint(2015, 2026, size=N_TITLES)

    df = pd.DataFrame({
        "title_id": [f"T{100000 + i}" for i in range(N_TITLES)],
        "title_name": make_title_names(N_TITLES),
        "genre": genres,
        "content_type": content_type,
        "release_year": release_year,
        "num_ratings": num_ratings,
        "avg_rating": ratings,
    })

    df = df.sort_values("title_id").reset_index(drop=True)
    df.to_csv("data/streaming_ratings.csv", index=False)
    print(f"Wrote data/streaming_ratings.csv with {len(df)} rows")
    print(df["avg_rating"].describe())


if __name__ == "__main__":
    main()

"""
CLI: analyse reviews for any Play-Store app(s).

Example
-------
python -m app_review_sentiment.pipeline "Spotify" "com.whatsapp"
"""
import argparse, pathlib, sys
from . import fetch, preprocess, sentiment, topics


def run(packages, outdir="outputs", n=1000, engine="vader", n_topics=10):
    out = pathlib.Path(outdir)
    out.mkdir(exist_ok=True)

    # -------- fetch & basic info --------
    try:
        df = fetch.fetch(packages, n=n)
    except Exception as e:
        sys.exit(f"[✗] {e}")

    # -------- sentiment (keep stop-words) --------
    df["Clean_sent"] = df["Review"].map(
        lambda t: preprocess.clean_text(t, remove_stop=False)
    )
    df[f"Sent_{engine}"] = getattr(sentiment, engine)(df["Clean_sent"])

    # -------- topics (remove stop-words) --------
    df["Clean_topic"] = df["Review"].map(
        lambda t: preprocess.clean_text(t, remove_stop=True)
    )
    top_df = topics.lda(df["Clean_topic"], n_topics=n_topics)

    # -------- save --------
    df.to_csv(out / "reviews.csv", index=False)
    top_df.to_csv(out / "topics.csv", index=False)
    print(f"[✓] Saved → {out/'reviews.csv'}  &  {out/'topics.csv'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Sentiment & topics for Play-Store apps."
    )
    ap.add_argument(
        "packages",
        nargs="+",
        help='Package ID **or** plain-English name, e.g. "com.spotify.music" or "Spotify".',
    )
    ap.add_argument("--outdir", default="outputs")
    ap.add_argument("--n", type=int, default=1000, help="max reviews per app")
    ap.add_argument(
        "--engine", choices=["vader", "textblob", "gpt"], default="vader"
    )
    ap.add_argument("--n_topics", type=int, default=10)
    run(**vars(ap.parse_args()))

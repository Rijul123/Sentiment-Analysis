"""
Fetch Play-Store reviews.

Functions
---------
resolve_package(query, lang='en', country='us') -> str
    Turns an app name or package ID into a canonical package ID.
fetch(packages, lang='en', country='us', n=None) -> DataFrame
    Downloads reviews for one or more packages.
"""
import pandas as pd
from google_play_scraper import reviews, Sort, reviews_all, search


def resolve_package(query: str, *, lang="en", country="us") -> str:
    """
    Accept either a full package ID or an app name.
    • If `query` contains a dot, assume it's already an ID.
    • Otherwise look up the first Play-Store result.
    """
    if "." in query and " " not in query:
        return query  # looks like a package ID

    hits = search(query, lang=lang, country=country, n_hits=1)
    if not hits:
        raise ValueError(f"No Play-Store result for '{query}'")
    return hits[0]["appId"]  # canonical package ID


def _get_reviews(package, lang, country, n):
    """
    Use google-play-scraper. Falls back to paginated 'reviews()'
    if reviews_all() hits a transient error.
    """
    try:
        data = reviews_all(package, lang=lang, country=country)
    except Exception:
        data, _ = reviews(
            package,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=min(200, n or 200),
        )

    if n:  # truncate if user limited number
        data = data[:n]
    return data


def fetch(packages, *, lang="en", country="us", n=None):
    """
    Parameters
    ----------
    packages : list[str] – names or package IDs.
    n        : int|None  – max reviews (per app); None = all.

    Returns
    -------
    pandas.DataFrame with columns:
        Package, AppName, Reviewer, Review, Rating, At
    """
    frames = []
    for q in packages:
        pkg_id = resolve_package(q, lang=lang, country=country)
        revs = _get_reviews(pkg_id, lang, country, n or 0)
        if not revs:
            continue

        df = (
            pd.DataFrame(revs)[["userName", "content", "score", "at"]]
            .rename(
                columns={
                    "userName": "Reviewer",
                    "content": "Review",
                    "score": "Rating",
                    "at": "At",
                }
            )
            .assign(Package=pkg_id, AppName=q)
        )
        frames.append(df)

    if not frames:
        raise RuntimeError("No reviews fetched – check package names or network.")
    return pd.concat(frames, ignore_index=True)

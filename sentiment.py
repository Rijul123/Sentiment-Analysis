import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


analyzer = SentimentIntensityAnalyzer()

def vader(series: pd.Series) -> pd.Series:
    """Fast, rule-based compound score (VADER)."""
    return series.fillna("").map(lambda t: analyzer.polarity_scores(t)["compound"])


def textblob(series: pd.Series) -> pd.Series:
    """TextBlob polarity; slower but smoother on long text."""
    return series.fillna("").map(lambda t: TextBlob(t).sentiment.polarity)
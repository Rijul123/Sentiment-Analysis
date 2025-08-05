import re, string, inflect, pandas as pd
import nltk
from nltk.corpus import stopwords

# NLTK data downloads are now handled by the Dockerfile,
# so we no longer need the download call.

STOP_WORDS = set(stopwords.words("english"))

_inflector = inflect.engine()
_punct_re = re.compile(f"[{re.escape(string.punctuation)}]")
_space_re = re.compile(r"\s+")

def _num2word(match):
    """Convert digit tokens to words for more robust vocab."""
    return _inflector.number_to_words(match.group())

def clean_text(txt: str, *, remove_stop: bool = False) -> str:
    """
    Basic normalization:
    • strip punctuation
    • digits → words
    • lowercase & squish spaces
    • optional stop-word removal
    """
    if pd.isnull(txt):
        return txt

    txt = _punct_re.sub(" ", txt)
    txt = re.sub(r"\b\d+\b", _num2word, txt)
    txt = _space_re.sub(" ", txt).lower().strip()

    if remove_stop:
        tokens = [w for w in txt.split() if w not in STOP_WORDS]
        txt = " ".join(tokens)

    return txt
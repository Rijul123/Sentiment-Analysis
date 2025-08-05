from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

def lda(series, n_topics=10, top_n=7, max_feat=400):
    vect = CountVectorizer(max_features=max_feat)
    X = vect.fit_transform(series)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=2).fit(X)

    words = vect.get_feature_names_out()
    records = []
    for i, comp in enumerate(lda.components_):
        top_words = [words[j] for j in comp.argsort()[:top_n]]
        records.append({'Topic': i+1, 'Words': ', '.join(top_words)})
    return pd.DataFrame(records)

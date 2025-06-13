import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation



data_file = "pre_processed.csv"  
df = pd.read_csv(data_file)
reviews = df['Review'].dropna().tolist()


vectorizer = CountVectorizer(max_features=400) 
X = vectorizer.fit_transform(reviews)

lda = LatentDirichletAllocation(n_components=15, random_state=2)  
lda.fit(X)

topic_words = []
for topic_idx, topic in enumerate(lda.components_):
    words = []  
    sorted_indices = topic.argsort()  
    for i in sorted_indices[:7]:  
        word = vectorizer.get_feature_names_out()[i]  
        words.append(word)  
    topic_words.append({"Topic": f"Topic {topic_idx + 1}", "Words": ", ".join(words)})

output_df = pd.DataFrame(topic_words)
output_df.to_csv("lda_topics.csv", index=False)


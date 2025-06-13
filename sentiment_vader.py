import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')






data_file = "pre_processed.csv"  
df = pd.read_csv(data_file)

reviews = df.groupby('Package Name').head(50).reset_index(drop=True) # get first 50 reviews

analyzer = SentimentIntensityAnalyzer()

def calculate_polarity(review):
    return analyzer.polarity_scores(review)['compound']

reviews['VADER Polarity'] = reviews['Review'].apply(calculate_polarity)

reviews[['Package Name', 'Review', 'VADER Polarity']].to_csv("50_reviews_with_vader.csv", index=False)


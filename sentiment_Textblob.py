import pandas as pd
from textblob import TextBlob
#

data_file = "pre_processed.csv"   
df = pd.read_csv(data_file)

reviews = df.groupby('Package Name').head(50).reset_index(drop=True) # gets first 50 reviews

def calculate_polarity(review):
    return TextBlob(review).sentiment.polarity

reviews['TextBlob Polarity'] = reviews['Review'].apply(calculate_polarity)



reviews[['Package Name', 'Review', 'TextBlob Polarity']].to_csv("50_reviews_with_textblob.csv", index=False)




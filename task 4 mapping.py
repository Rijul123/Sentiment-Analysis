import pandas as pd

data_file = "pre_processed.csv"  
topics_file = "lda_topics.csv"

topics = []

topics_df = pd.read_csv(topics_file)
app_df = pd.read_csv(data_file)
package_name = "combabylontelushealth"

package_reviews = app_df[app_df['Package Name'] == package_name] # only getting reviews for package app
reviews = package_reviews.head(50)  # getting first 50 reviews
print(topics_df.columns)
topics_df['Top Words'] = topics_df['Top Words'].apply(lambda x: x.split(", "))

for review in reviews['Review']:
        scores = [] # based on number of words in topic and review
      
        for topic_row in topics_df.itertuples(index=False):
            topic_words = set(topic_row[1])  
            review_words = set(review.lower().split()) 
            same_words = len(topic_words.intersection(review_words))  
            scores.append(same_words)
        
        topics.append(scores.index(max(scores)) + 1) #assign topic for review

reviews['Topic'] = topics
reviews.to_csv("review_topics.csv", index=False)
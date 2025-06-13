import pandas as pd
import openai
from openai import OpenAI
import os                          

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY") 
)

data_file = "pre_processed.csv"
df = pd.read_csv(data_file)

reviews = df.groupby('Package Name').head(50).reset_index(drop=True)  # gets first 50 reviews

def calculate_polarity(review):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are to analyze reviews, and calculate their sentiment "
                    "and polarity."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Classify the sentiment (positive, neutral, negative) on the "
                    "first line, then give a polarity score on the second line. "
                    f"Here is the review:\n\nReview: \"{review}\""
                ),
            },
        ],
    )

    content = response.choices[0].message.content
    print(f"API Response: {content}")
    sentiment_line = content.split("\n")[0]
    polarity_line = content.split("\n")[1]
    sentiment = sentiment_line.split("as")[-1].strip().strip(".")
    polarity_score = polarity_line.split(":")[-1].strip()
    return sentiment, polarity_score


reviews[['Sentiment', 'Polarity']] = (
    reviews['Review'].apply(calculate_polarity).apply(pd.Series)
)

reviews[['Package Name', 'Review', 'Sentiment', 'Polarity']].to_csv(
    "reviews_with_llama.csv",
    index=False,
)


print('aha')
reviews[['Sentiment', 'Polarity']] = reviews['Review'].apply(calculate_polarity).apply(pd.Series)

reviews[['Package Name', 'Review', 'Sentiment', 'Polarity']].to_csv("reviews_with_llama.csv", index=False)

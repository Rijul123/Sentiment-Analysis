import pandas as pd
import re
import inflect
import string

p = inflect.engine()

STOP_WORDS = {"the", "is", "in", "and", "to", "a", "of", "it", "for", "on", "with", "as", "at", "this", "that"}

def clean_text(text):
    if pd.isnull(text): 
        return text
    text = str(text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\b\d+\b', lambda x: p.number_to_words(x.group()), text)
    text = re.sub(r'\s+', ' ', text).strip().lower()
    no_stop_words = []
    for word in text.split():  
        if word not in STOP_WORDS:  
            no_stop_words.append(word)
    words = no_stop_words
    return ' '.join(words)


df = pd.read_csv('com_babylon_telushealth_reviews.csv')
df_cleaned = df.map(clean_text)
df_cleaned.to_csv('pre_processed.csv', index=False)

sample = df['Review'].sample(20, random_state=42) 
pd.set_option('display.max_colwidth', None)
print(sample.to_string(index=False))
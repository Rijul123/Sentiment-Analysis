
# Google Play Review Analyzer

This project scrapes reviews from any Android app on the Google Play Store and does sentiment analysis and topic modelling on its reviews.

## 🔧 What It Does

- Scrapes app reviews from Google Play  
- Cleans and preprocesses the text  
- Analyzes review sentiment (positive, neutral, negative)  
- Identifies key topics using LDA  

## 📁 Files

- `fetch.py` – Scrapes app reviews  
- `pre_process.py` – Cleans the text  
- `sentiment.py` – Performs sentiment analysis  
- `topics.py` – Extracts topics using LDA  
- `main.py` – Main script that ties everything together  

## Usage

**Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
```

**Install the Python packages**

```bash
pip install pandas nltk textblob scikit-learn google_play_scraper inflect
```

**Download the two NLTK corpora once**

```bash
python - <<'PY'
import nltk; nltk.download('vader_lexicon'); nltk.download('stopwords')
PY
```

**Run**

```bash
python main.py com.whatsapp \
  --n 500 \         # max reviews to scrape
  --engine vader \ 
  --n_topics 5      # number of topics
```

## or

## 🌐 View Online

https://playreviewscope.netlify.app

<img width="1427" height="485" alt="image" src="https://github.com/user-attachments/assets/1e057f95-c95b-4ca2-95f1-97ed503f9c9c" />



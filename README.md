# Sentiment Analysis 📊

This project is an **end-to-end sentiment analysis pipeline** that processes app reviews, applies three different sentiment models (VADER, TextBlob, and Llama 3 via Groq API), and performs topic modelling using LDA.

## 🔧 Features

- Cleans and prepares app review data
- Runs sentiment analysis using:
  - VADER (rule-based)
  - TextBlob (lexicon-based)
  - Llama 3 via Groq API (LLM-based)
- Trains an LDA topic model to group reviews by themes
- Assigns each review to a topic
- Saves all outputs to reusable CSVs

---

## 💂 Project Structure

```
sentiment-analysis/
├── 01_preprocess_reviews.py          # Clean and format reviews
├── 02_sentiment_vader.py             # VADER sentiment analysis
├── 02_sentiment_textblob.py          # TextBlob sentiment analysis
├── 02_sentiment_llama_api.py         # Groq API (Llama 3) sentiment analysis
├── 03_topic_model_lda.py             # Topic modelling using LDA
├── 04_topic_assignment.py            # Assign topics to reviews
├── config.py                         # Loads secrets from .env
├── data/
│   ├── raw/                          # Original review data
│   └── processed/                    # Cleaned review data
├── outputs/                          # Generated model results
├── .env.example                      # Example environment variable file
├── .gitignore                        # Excludes .env, outputs, etc.
├── requirements.txt                  # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Set up the environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your API key

Copy the example file and paste your real key:

```bash
cp .env.example .env
```

Edit `.env`:

```env
GROQ_API_KEY=your-key-here
GROQ_BASE_URL=https://api.groq.com/openai/v1
```

### 4. Run the full pipeline

```bash
python 01_preprocess_reviews.py
python 02_sentiment_vader.py
python 02_sentiment_textblob.py
python 02_sentiment_llama_api.py
python 03_topic_model_lda.py
python 04_topic_assignment.py
```

---

## 📁 Output Files

- `outputs/vader_sentiment.csv`
- `outputs/textblob_sentiment.csv`
- `outputs/llama_sentiment.csv`
- `outputs/topic_assignments.csv`
- `outputs/lda_model.pkl`

---

## 📦 Dependencies

Listed in `requirements.txt`. Key packages:

- `pandas`
- `nltk`
- `textblob`
- `scikit-learn`
- `openai` (for Groq API)
- `python-dotenv`

Tested on **Python 3.11+**.

---

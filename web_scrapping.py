import pandas as pd
from google_play_scraper import reviews_all

packages = ["com.babylon.telushealth", "com.loblaw.pchealth", "com.wam.android", "com.maplenativeuser", "com.ydo.smartapp" ]

reviews = pd.DataFrame()
dataframe_lst = []

for app in packages:

    app_reviews = reviews_all(app, lang = 'en', country ='ca', continuation_token =True)
    
    df = pd.DataFrame(app_reviews)

    df = df[['userName', 'content', 'score']]
    df.columns = ['Reviewer Name', 'Review', 'Rating']
    
    df['Package Name'] = app

    dataframe_lst.append(df)

reviews = pd.concat(dataframe_lst, ignore_index=True)
reviews = reviews[['Package Name', 'Reviewer Name', 'Review', 'Rating']]

csv_file = "com_babylon_telushealth_reviews.csv"
reviews.to_csv(csv_file, index=False)


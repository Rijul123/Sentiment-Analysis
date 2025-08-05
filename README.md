💬 Google Play Review Sentiment Analysis
This project is a web-based application designed to perform sentiment analysis and topic modeling on Google Play Store reviews. It allows users to gain insights into public opinion about specific Android applications by scraping reviews, determining their sentiment (positive, negative, neutral), and identifying common themes or topics discussed within them.

✨ Features
Google Play Review Scraping: Easily fetch reviews for any specified Android application available on the Google Play Store.

Customizable Review Count: Choose the number of reviews you want to scrape for analysis.

Sentiment Analysis: Utilizes Natural Language Processing (NLP) techniques to classify each review's sentiment as positive, negative, or neutral.

Topic Modeling: Identifies and extracts key topics or themes present across the collected reviews, providing a high-level understanding of user feedback.

Interactive Web Interface: A user-friendly interface to input app names, select parameters, and view analysis results.

⚙️ How It Works


Input: The user provides the name of a Google Play app selects the number of reviews to look at.

Scraping: The backend scrapes reviews from the Google Play Store for the specified application.

Processing: The collected reviews undergo an NLP pipeline:

Sentiment Analysis: Each review is processed to determine its emotional tone.

Topic Modeling: Algorithms are applied to group similar reviews and extract underlying topics.

Output: The results, including overall sentiment distribution and identified topics, are presented in an easy-to-understand format on the web interface.






To use the Review Sentiment Analysis tool:

Navigate to the deployed application: https://playreviewscope.netlify.app/

Enter App Name: Type the exact name of the Android application you wish to analyze in the designated input field.

Select Review Count: Choose the number of reviews you want to scrape (e.g., 100, 500, 1000).

Select Topic Count: Specify how many distinct topics you'd like the model to identify (e.g., 3, 5, 10).

Click "Analyze": Initiate the analysis process and view the results.

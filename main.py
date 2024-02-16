from textblob import TextBlob
from newspaper import Article

# Define the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Mathematics'

# Create an Article object and download/parsing the article
article = Article(url)
article.download()
article.parse()

# Get the text content of the article
text = article.text

# Perform sentiment analysis on the text using TextBlob
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity

# Determine the sentiment label based on the sentiment score
if sentiment_score > 0:
    sentiment_label = "Positive"
elif sentiment_score < 0:
    sentiment_label = "Negative"
else:
    sentiment_label = "Neutral"

# Print the sentiment analysis results
print("Sentiment Score:", sentiment_score)
print("Sentiment Label:", sentiment_label)


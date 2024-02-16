from textblob import TextBlob

# Define the text to analyze
text = "I love coding! It's so much fun."

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
print("Text:", text)
print("Sentiment Score:", sentiment_score)
print("Sentiment Label:", sentiment_label)

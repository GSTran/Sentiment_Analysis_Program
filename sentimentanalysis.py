from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input text from the user
input_text = input("Enter the text: ")

# Analyze sentiment
sentiment = analyze_sentiment(input_text)
print("Sentiment:", sentiment)

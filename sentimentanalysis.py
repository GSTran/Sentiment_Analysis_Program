from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    input_text = input("Enter a sentence: ")
    sentiment = analyze_sentiment(input_text)
    
    print("Sentiment:", sentiment)

if __name__ == "__main__":
    main()

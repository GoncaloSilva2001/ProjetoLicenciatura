from nltk.sentiment import SentimentIntensityAnalyzer

def calculate_word_sentiment(word):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(word)
    return scores['compound']

word = input("enter a word:")
sentiment_score = calculate_word_sentiment(word)

print(f"Sentiment score for the word '{word}': {sentiment_score}")
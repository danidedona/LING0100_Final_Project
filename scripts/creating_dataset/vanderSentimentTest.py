from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_compound_sentiment(phrase):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(phrase)
    return vs['compound'], vs  # Also return full scores if you want more than just compound

def main():
    analyzer = SentimentIntensityAnalyzer()
    print("Type a phrase to analyze sentiment (type 'exit' to quit):\n")

    while True:
        phrase = input("Enter phrase: ")
        if phrase.lower() == 'exit':
            break

        compound_score, full_scores = get_compound_sentiment(phrase)
        print(f"Compound Sentiment Score: {compound_score}")
        print(f"Detailed Scores: {full_scores}\n")

if __name__ == '__main__':
    main()

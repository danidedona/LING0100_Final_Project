import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load your cleaned swear words CSV
df = pd.read_csv("data/swear_words_cleaned.csv")

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Add sentiment score
df['Sentiment_Compound'] = df['English Translation'].apply(
    lambda x: analyzer.polarity_scores(str(x))['compound']
)

# Save result
df.to_csv("data/swear_words_with_sentiment.csv", index=False)
print("Saved with sentiment scores to data/swear_words_with_sentiment.csv")

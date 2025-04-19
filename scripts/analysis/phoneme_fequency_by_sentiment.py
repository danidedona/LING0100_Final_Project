import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import os
from load_utils import sentiment_bin

# Load data
df = pd.read_csv("data/filtered_swear_words_with_sentiment.csv")
df = df[df['IPA'].notna() & df['Sentiment_Compound'].notna()]
df['SentimentBin'] = df['Sentiment_Compound'].apply(sentiment_bin)

# === GENERAL ANALYSIS ===

# Count phonemes per sentiment bin
bin_counts = {}
for b in df['SentimentBin'].unique():
    phonemes = ''.join(df[df['SentimentBin'] == b]['IPA'].dropna())
    bin_counts[b] = Counter(phonemes)

phoneme_by_sentiment = pd.DataFrame(bin_counts).fillna(0).astype(int)
phoneme_by_sentiment['Total'] = phoneme_by_sentiment.sum(axis=1)
phoneme_by_sentiment = phoneme_by_sentiment.sort_values(by='Total', ascending=False).drop(columns='Total')

# Save and plot
os.makedirs("results", exist_ok=True)
phoneme_by_sentiment.to_csv("results/phoneme_by_sentiment.csv")
phoneme_by_sentiment.head(20).plot(kind='bar', figsize=(12,6))
plt.title("Top 20 Phonemes by Sentiment Bin")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/phoneme_by_sentiment_plot.png")
plt.close()

# === PER-LANGUAGE ANALYSIS ===

langs = df['Language'].unique()

for lang in langs:
    lang_df = df[df['Language'] == lang]
    lang_dir = f"results/{lang}"
    os.makedirs(lang_dir, exist_ok=True)

    bin_counts = {}
    for b in lang_df['SentimentBin'].unique():
        phonemes = ''.join(lang_df[lang_df['SentimentBin'] == b]['IPA'].dropna())
        bin_counts[b] = Counter(phonemes)

    if not bin_counts:
        continue

    phoneme_by_sentiment = pd.DataFrame(bin_counts).fillna(0).astype(int)
    phoneme_by_sentiment['Total'] = phoneme_by_sentiment.sum(axis=1)
    phoneme_by_sentiment = phoneme_by_sentiment.sort_values(by='Total', ascending=False).drop(columns='Total')

    phoneme_by_sentiment.to_csv(f"{lang_dir}/phoneme_by_sentiment.csv")

    phoneme_by_sentiment.head(20).plot(kind='bar', figsize=(12,6))
    plt.title(f"Top 20 Phonemes by Sentiment Bin – {lang}")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{lang_dir}/phoneme_by_sentiment_plot.png")
    plt.close()

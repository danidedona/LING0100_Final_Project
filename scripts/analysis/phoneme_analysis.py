import pandas as pd
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import panphon
import unicodedata

# === Load and clean dataset ===
df = pd.read_csv("data/swear_words_with_sentiment.csv")
for col in df.select_dtypes(include='object'):
    df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)


df = df[df['IPA'].notna() & (df['IPA'].str.strip() != '')]

# === General Phoneme Frequency ===
all_ipa = ''.join(df['IPA'].dropna().tolist())
phoneme_counts = Counter(all_ipa)

phoneme_df = pd.DataFrame(phoneme_counts.items(), columns=['Phoneme', 'Count'])
phoneme_df = phoneme_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
phoneme_df.to_csv("phoneme_frequency.csv", index=False)

fig, ax = plt.subplots(figsize=(10, 6))
phoneme_df.head(20).plot(kind='bar', x='Phoneme', y='Count', legend=False, color='skyblue', ax=ax)
ax.set_title("Top 20 Most Frequent Phonemes")
ax.set_xlabel("Phoneme")
ax.set_ylabel("Frequency")
ax.tick_params(axis='x', rotation=0)
plt.tight_layout()
plt.savefig("phoneme_plot.png")
plt.close()

# === Sound Class Setup ===
ft = panphon.FeatureTable()
manual_class_override = {
    't': 'plosive', 'k': 'plosive', 's': 'fricative', 'd': 'plosive', 'b': 'plosive',
    'p': 'plosive', 'v': 'fricative', 'ʃ': 'fricative', 'ɡ': 'plosive', 'z': 'fricative',
    'x': 'fricative', 'f': 'fricative', 'ʒ': 'fricative', 'ɕ': 'fricative', 'ʂ': 'fricative',
    'ɖ': 'plosive', 'ʈ': 'plosive', 'ɣ': 'fricative', 'ʝ': 'fricative', 'ʁ': 'fricative'
}

def get_sound_class(symbol):
    if symbol in manual_class_override:
        return manual_class_override[symbol]
    vectors = ft.word_to_vector_list(symbol, numeric=True)
    if not vectors:
        return 'unknown'
    features = vectors[0]
    names = ft.names
    def fval(name):
        return features[names.index(name)] if name in names else 0
    if fval('syl') == 1:
        return 'vowel'
    if fval('nas') == 1:
        return 'nasal'
    if fval('cont') == 1 and fval('syl') == 0:
        return 'fricative'
    if fval('delrel') == 0 and fval('syl') == 0:
        return 'plosive'
    if fval('approx') == 1 or (fval('son') == 1 and fval('syl') != 1 and fval('nas') != 1):
        return 'approximant'
    if fval('lat') == 1:
        return 'lateral'
    if fval('tap') == 1 or fval('flap') == 1:
        return 'tap_or_flap'
    if fval('trl') == 1:
        return 'trill'
    return 'other'

# === General Sound Class Frequency ===
class_counts = defaultdict(int)
for phoneme, count in phoneme_counts.items():
    sound_class = get_sound_class(phoneme)
    class_counts[sound_class] += count

class_df = pd.DataFrame(class_counts.items(), columns=['Sound Class', 'Count'])
class_df = class_df.sort_values(by='Count', ascending=False).reset_index(drop=True)
class_df.to_csv("phoneme_class_frequency.csv", index=False)

fig, ax = plt.subplots(figsize=(8, 6))
class_df.plot(kind='bar', x='Sound Class', y='Count', legend=False, color='salmon', ax=ax)
ax.set_title("Overall Phoneme Counts by Sound Class")
ax.set_xlabel("Sound Class")
ax.set_ylabel("Frequency")
ax.tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.savefig("phoneme_class_plot.png")
plt.close()

# === Sentiment-Based Phoneme Analysis ===
def sentiment_bin(score):
    if score <= -0.5:
        return 'very_negative'
    elif score <= -0.1:
        return 'moderately_negative'
    elif score < 0.1:
        return 'neutral'
    else:
        return 'positive'

df['SentimentBin'] = df['Sentiment_Compound'].apply(sentiment_bin)

bin_counts = {}
for b in df['SentimentBin'].unique():
    ipa_concat = ''.join(df[df['SentimentBin'] == b]['IPA'].dropna())
    bin_counts[b] = Counter(ipa_concat)

phoneme_by_sentiment = pd.DataFrame(bin_counts).fillna(0).astype(int)
phoneme_by_sentiment['Total'] = phoneme_by_sentiment.sum(axis=1)
phoneme_by_sentiment = phoneme_by_sentiment.sort_values('Total', ascending=False).drop(columns='Total')
phoneme_by_sentiment.to_csv("phoneme_by_sentiment.csv")

fig, ax = plt.subplots(figsize=(12, 6))
phoneme_by_sentiment.head(20).plot(kind='bar', ax=ax)
ax.set_title("Top 20 Phonemes by Sentiment Bin")
ax.set_xlabel("Phoneme")
ax.set_ylabel("Frequency")
ax.tick_params(axis='x', rotation=0)
plt.tight_layout()
plt.savefig("phoneme_by_sentiment_plot.png")
plt.close()

# === Sentiment-Based Sound Class Breakdown ===
phoneme_classes = {p: get_sound_class(p) for p in phoneme_by_sentiment.index}
class_by_sentiment = defaultdict(lambda: defaultdict(int))
for phoneme, row in phoneme_by_sentiment.iterrows():
    cls = phoneme_classes.get(phoneme, 'unknown')
    for col in phoneme_by_sentiment.columns:
        class_by_sentiment[cls][col] += row[col]

class_sent_df = pd.DataFrame(class_by_sentiment).T.fillna(0).astype(int)

# Add percentages
class_sent_percent = class_sent_df.div(class_sent_df.sum(axis=0), axis=1) * 100
class_sent_percent = class_sent_percent.round(2)

# Combine
class_sent_combined = pd.concat([class_sent_df, class_sent_percent], axis=1, keys=["Count", "Percent"])
class_sent_combined.to_csv("sound_class_by_sentiment_combined.csv")

fig, ax = plt.subplots(figsize=(10, 6))
class_sent_df.plot(kind='bar', ax=ax)
ax.set_title("Sound Class Distribution by Sentiment")
ax.set_xlabel("Sound Class")
ax.set_ylabel("Frequency")
ax.tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.savefig("sound_class_by_sentiment_plot.png")
plt.close()

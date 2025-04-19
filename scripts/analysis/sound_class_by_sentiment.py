import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
import os
from load_utils import get_sound_class

# === Overall analysis ===

# Load general output
phoneme_by_sentiment = pd.read_csv("results/phoneme_by_sentiment.csv", index_col=0)

# Map phonemes to sound classes
phoneme_classes = {p: get_sound_class(p) for p in phoneme_by_sentiment.index}
class_by_sentiment = defaultdict(lambda: defaultdict(int))

# Aggregate
for phoneme, row in phoneme_by_sentiment.iterrows():
    sound_class = phoneme_classes.get(phoneme, 'unknown')
    for col in phoneme_by_sentiment.columns:
        class_by_sentiment[sound_class][col] += row[col]

# Save + plot
class_df = pd.DataFrame(class_by_sentiment).T.fillna(0).astype(int)
percent_df = class_df.div(class_df.sum(axis=0), axis=1) * 100
combined_df = pd.concat([class_df, percent_df.round(2)], axis=1, keys=["Count", "Percent"])
combined_df.to_csv("results/sound_class_by_sentiment_combined.csv")

class_df.plot(kind='bar', figsize=(10, 6))
plt.title("Sound Class Distribution by Sentiment")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/sound_class_by_sentiment_plot.png")
plt.close()

# === Per-language analysis ===

langs = [d for d in os.listdir("results") if os.path.isdir(f"results/{d}") and len(d) == 2]

for lang in langs:
    lang_path = f"results/{lang}/phoneme_by_sentiment.csv"
    if not os.path.exists(lang_path):
        continue

    phoneme_by_sentiment = pd.read_csv(lang_path, index_col=0)
    phoneme_classes = {p: get_sound_class(p) for p in phoneme_by_sentiment.index}
    class_by_sentiment = defaultdict(lambda: defaultdict(int))

    for phoneme, row in phoneme_by_sentiment.iterrows():
        sound_class = phoneme_classes.get(phoneme, 'unknown')
        for col in phoneme_by_sentiment.columns:
            class_by_sentiment[sound_class][col] += row[col]

    class_df = pd.DataFrame(class_by_sentiment).T.fillna(0).astype(int)
    percent_df = class_df.div(class_df.sum(axis=0), axis=1) * 100
    combined_df = pd.concat([class_df, percent_df.round(2)], axis=1, keys=["Count", "Percent"])
    combined_df.to_csv(f"results/{lang}/sound_class_by_sentiment_combined.csv")

    class_df.plot(kind='bar', figsize=(10, 6))
    plt.title(f"Sound Class Distribution by Sentiment – {lang}")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"results/{lang}/sound_class_by_sentiment_plot.png")
    plt.close()

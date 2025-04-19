import pandas as pd
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import os
from load_utils import get_sound_class

# === Setup ===
df = pd.read_csv("data/filtered_swear_words_with_sentiment.csv")
df = df[df['IPA'].notna() & (df['IPA'].str.strip() != '')]

os.makedirs("results", exist_ok=True)

# === GENERAL ANALYSIS ===

# General phoneme frequency
all_ipa = ''.join(df['IPA'].tolist())
phoneme_counts = Counter(all_ipa)
phoneme_df = pd.DataFrame(phoneme_counts.items(), columns=['Phoneme', 'Count']).sort_values(by='Count', ascending=False)
phoneme_df.to_csv("results/phoneme_frequency.csv", index=False)

# Plot
phoneme_df.head(20).plot(kind='bar', x='Phoneme', y='Count', color='skyblue', legend=False, figsize=(10,6))
plt.title("Top 20 Most Frequent Phonemes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/phoneme_plot.png")
plt.close()

# Sound class frequency
class_counts = defaultdict(int)
for phoneme, count in phoneme_counts.items():
    class_counts[get_sound_class(phoneme)] += count

class_df = pd.DataFrame(class_counts.items(), columns=["Sound Class", "Count"]).sort_values(by="Count", ascending=False)
class_df.to_csv("results/phoneme_class_frequency.csv", index=False)

class_df.plot(kind='bar', x='Sound Class', y='Count', color='salmon', legend=False, figsize=(8,6))
plt.title("Overall Phoneme Counts by Sound Class")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/phoneme_class_plot.png")
plt.close()

# === PER LANGUAGE ANALYSIS ===
langs = df['Language'].unique()

for lang in langs:
    lang_df = df[df['Language'] == lang]
    lang_dir = f"results/{lang}"
    os.makedirs(lang_dir, exist_ok=True)

    # Phoneme frequency
    all_ipa = ''.join(lang_df['IPA'].tolist())
    phoneme_counts = Counter(all_ipa)
    phoneme_df = pd.DataFrame(phoneme_counts.items(), columns=['Phoneme', 'Count']).sort_values(by='Count', ascending=False)
    phoneme_df.to_csv(f"{lang_dir}/phoneme_frequency.csv", index=False)

    phoneme_df.head(20).plot(kind='bar', x='Phoneme', y='Count', color='skyblue', legend=False, figsize=(10,6))
    plt.title(f"Top 20 Most Frequent Phonemes – {lang}")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{lang_dir}/phoneme_plot.png")
    plt.close()

    # Sound class frequency
    class_counts = defaultdict(int)
    for phoneme, count in phoneme_counts.items():
        class_counts[get_sound_class(phoneme)] += count

    class_df = pd.DataFrame(class_counts.items(), columns=["Sound Class", "Count"]).sort_values(by="Count", ascending=False)
    class_df.to_csv(f"{lang_dir}/phoneme_class_frequency.csv", index=False)

    class_df.plot(kind='bar', x='Sound Class', y='Count', color='salmon', legend=False, figsize=(8,6))
    plt.title(f"Phoneme Counts by Sound Class – {lang}")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{lang_dir}/phoneme_class_plot.png")
    plt.close()

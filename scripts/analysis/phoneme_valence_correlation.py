import pandas as pd
import numpy as np
import os
from load_utils import get_sound_class

# === Overall correlation ===

df = pd.read_csv("data/filtered_swear_words_with_sentiment.csv")
df = df[df['IPA'].notna() & df['Sentiment_Compound'].notna()]

# Get all phonemes
all_ipa = ''.join(df['IPA'])
unique_phonemes = sorted(set(all_ipa))

# Binary phoneme columns
for p in unique_phonemes:
    df[f'has_{p}'] = df['IPA'].str.contains(p).astype(int)

# Correlation results
results = []
for p in unique_phonemes:
    corr = np.corrcoef(df[f'has_{p}'], df['Sentiment_Compound'])[0, 1]
    cls = get_sound_class(p)
    results.append({'Phoneme': p, 'CorrelationWithValence': corr, 'SoundClass': cls})

out_df = pd.DataFrame(results).sort_values(by='CorrelationWithValence')
out_df.to_csv("results/phoneme_valence_correlation_with_class.csv", index=False)


# === Per-language correlation ===

langs = df['Language'].dropna().unique()

for lang in langs:
    lang_df = df[df['Language'] == lang].copy()
    all_ipa = ''.join(lang_df['IPA'])
    unique_phonemes = sorted(set(all_ipa))

    for p in unique_phonemes:
        lang_df[f'has_{p}'] = lang_df['IPA'].str.contains(p).astype(int)

    results = []
    for p in unique_phonemes:
        try:
            corr = np.corrcoef(lang_df[f'has_{p}'], lang_df['Sentiment_Compound'])[0, 1]
        except:
            corr = np.nan
        cls = get_sound_class(p)
        results.append({'Phoneme': p, 'CorrelationWithValence': corr, 'SoundClass': cls})

    lang_out = pd.DataFrame(results).sort_values(by='CorrelationWithValence')
    os.makedirs(f"results/{lang}", exist_ok=True)
    lang_out.to_csv(f"results/{lang}/phoneme_valence_correlation_with_class.csv", index=False)

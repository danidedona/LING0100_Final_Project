import pandas as pd
import unicodedata

# load raw file
df = pd.read_csv("data/unclean/swear_words_combined.csv")

# strip whitespace from all fields
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# define a function to clean IPA
def clean_ipa(ipa):
    if not isinstance(ipa, str):
        return ipa
    # normalize unicode and remove diacritics (Mn = nonspacing marks)
    ipa = unicodedata.normalize('NFD', ipa)
    ipa = ''.join(c for c in ipa if unicodedata.category(c) != 'Mn')
    # optional: remove any non-IPA junk characters
    denylist = set([' ', '’', "'", ',', ':', '3', '1', '!', '?', '-', '–', 'ː', 'ʰ', 'ʷ', 'ʲ', 'پ', '惡', '閪'])
    ipa = ''.join(c for c in ipa if c not in denylist)
    return ipa

# apply IPA cleaner
df['IPA'] = df['IPA'].apply(clean_ipa)

# drop rows where IPA is now missing or empty
df = df[df['IPA'].notna() & (df['IPA'].str.strip() != '')]

# save cleaned file
df.to_csv("data/swear_words_cleaned.csv", index=False)
print("Cleaned data saved to data/swear_words_cleaned.csv")

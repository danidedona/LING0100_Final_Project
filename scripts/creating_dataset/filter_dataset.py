import pandas as pd

# Define list of English curse words to search for
curse_words = [
    "fuck", "shit", "bitch", "asshole", "bastard", "dick", "piss", "cunt",
    "motherfucker", "cock", "slut", "whore", "crap", "douche", "prick", "twat"
]

# Load dataset
df = pd.read_csv("data/swear_words_with_sentiment.csv")

# Normalize text (lowercase, strip whitespace)
df['English Translation'] = df['English Translation'].fillna('').str.lower().str.strip()

# Filter rows that contain any curse word in the English Translation
filtered_df = df[df['English Translation'].apply(
    lambda x: any(curse in x for curse in curse_words)
)]

# Save filtered results
filtered_df.to_csv("data/filtered_swear_words_with_sentiment.csv", index=False)
print(f"Saved {len(filtered_df)} filtered rows to data/filtered_swear_words_with_sentiment.csv")

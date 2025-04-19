import pandas as pd

# Load the filtered dataset
df = pd.read_csv("data/filtered_swear_words_with_sentiment.csv")

# Count words by language
counts = df['Language'].value_counts().sort_index()

# Convert to DataFrame and save
count_df = counts.reset_index()
count_df.columns = ['Language', 'WordCount']
count_df.to_csv("results/word_count_per_language.csv", index=False)

print("Saved word count per language to data/word_count_per_language.csv")

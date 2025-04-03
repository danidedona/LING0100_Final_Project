import json
import csv
import os
import sys

# Default input and output paths
DEFAULT_INPUT_JSON = "data/swear.json"
OUTPUT_DIR = "data/raw_words"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def json_to_csv(input_json):
    # Load JSON data
    with open(input_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Create separate CSV files for each language
    for lang, words in data.items():
        output_file = os.path.join(OUTPUT_DIR, f"{lang}_swear_words.csv")

        with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Word", "Language"])  # Header row
            
            for word in words:
                writer.writerow([word, lang])  # Each row has word + language code

        print(f"Created: {output_file}")

# Run the script
if __name__ == "__main__":
    # Check for command-line argument
    if len(sys.argv) > 1:
        input_json = sys.argv[1]
    else:
        input_json = DEFAULT_INPUT_JSON  # Use default if no argument is provided

    if not os.path.exists(input_json):
        print(f"Error: File '{input_json}' not found.")
        sys.exit(1)

    json_to_csv(input_json)
    print("All CSV files have been generated in 'data/raw_words'!")

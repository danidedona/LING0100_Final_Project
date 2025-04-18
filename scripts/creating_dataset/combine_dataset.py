import os
import sys
import csv

# Define your input and output directories
INPUT_DIR_IPA = "data/raw_words_and_ipa"
INPUT_DIR_TRANSLATIONS = "data/translations"
OUTPUT_DIR = "data"
FILE_NAME = "swear_words_combined.csv"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_csv(input_file_ipa, input_file_translations, output_file):
    """Processes a single IPA and translations CSV file, combining them."""
    with open(input_file_ipa, 'r', encoding='utf-8') as infileipa, open(output_file, 'a', encoding='utf-8', newline='') as outfile:
        with open(input_file_translations, 'r', encoding='utf-8') as infiletranslations:
            reader_ipa = csv.reader(infileipa)
            reader_translations = csv.reader(infiletranslations)

            # Skip headers
            next(reader_ipa)
            next(reader_translations)
            writer = csv.writer(outfile)

            for row_ipa, row_translations in zip(reader_ipa, reader_translations):
                if len(row_ipa) < 3 or len(row_translations) < 2:
                    continue  # Skip invalid rows
                
                word, lang, ipa = row_ipa
                _, translation = row_translations
                writer.writerow([word, lang, ipa, translation])

def process_all_csv():
    """Processes all CSV files in the input directory."""
    files = [f for f in os.listdir(INPUT_DIR_IPA) if f.endswith(".csv")]
    
    if not files:
        print(f"No CSV files found in '{INPUT_DIR_IPA}'.")
        return
    
    output_path = os.path.join(OUTPUT_DIR, FILE_NAME)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write("Word,Language,IPA,English Translation\n")

    for file in files:
        input_path_ipa = os.path.join(INPUT_DIR_IPA, file)
        input_path_translations = os.path.join(INPUT_DIR_TRANSLATIONS, file)
        process_csv(input_path_ipa, input_path_translations, output_path)
        print(f"Processed {file} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Process a single file
        csv_filename = sys.argv[1]
        input_path_ipa = os.path.join(INPUT_DIR_IPA, csv_filename)
        input_path_translations = os.path.join(INPUT_DIR_TRANSLATIONS, csv_filename)
        output_path = os.path.join(OUTPUT_DIR, FILE_NAME)

        if not os.path.exists(input_path_ipa):
            print(f"Error: File '{csv_filename}' not found in '{INPUT_DIR_IPA}'.")
            sys.exit(1)
        
        process_csv(input_path_ipa, input_path_translations, output_path)
        print(f"Processed {csv_filename} → {output_path}")
    else:
        # No argument provided, process all CSV files
        process_all_csv()
        print(f"All files processed! Check '{OUTPUT_DIR}'.")

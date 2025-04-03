import os
import sys
import epitran
import csv

# Updated language codes based on available Epitran mappings
LANGUAGE_CODES = {
    'en': 'generic-Latn',  # No specific English, but generic Latin script might work
    'fr': 'fra-Latn',      # French with Latin script
    'it': 'ita-Latn',      # Italian with Latin script
    'es': 'spa-Latn',      # Spanish with Latin script
    'pt': 'por-Latn',      # Portuguese with Latin script
    'ru': 'rus-Cyrl',      # Russian with Cyrillic script
    'tr': 'tur-Latn',      # Turkish with Latin script
    'zh': 'cmn-Latn',      # Mandarin with Latin script (for pinyin)
    'hi': 'hin-Deva',      # Hindi with Devanagari script
    'fa': 'fas-Arab',      # Persian with Arabic script
}

# Define your input and output directories
INPUT_DIR = "data/raw_words"
OUTPUT_DIR = "data/raw_words_and_ipa"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def transcribe_word(word, lang_code):
    """Transcribes a word into IPA using Epitran."""
    if lang_code not in LANGUAGE_CODES:
        return "[Unsupported language]"
    
    try:
        epi = epitran.Epitran(LANGUAGE_CODES[lang_code])
        return epi.transliterate(word)
    except Exception as e:
        return f"[Error: {str(e)}]"

def process_csv(input_file, output_file):
    """Processes a single CSV file, transcribing words into IPA."""
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Check if the file has a header row and add one to output if needed
        first_row = next(reader, None)
        if first_row is None:
            # Empty file
            writer.writerow(["Word", "Language", "IPA"])
            return
        
        # Check if the first row looks like a header
        has_header = "word" in str(first_row).lower() or "language" in str(first_row).lower()
        
        if has_header:
            # Use the existing header
            writer.writerow(["Word", "Language", "IPA"])
        else:
            # First row is data, not header - process it and add a header to output
            writer.writerow(["Word", "Language", "IPA"])
            infile.seek(0)  # Reset to beginning of file
        
        # Process all rows
        for row in reader:
            if len(row) < 2:
                continue  # Skip invalid rows
            
            word, lang_code = row
            ipa_transcription = transcribe_word(word.strip(), lang_code.strip())
            writer.writerow([word, lang_code, ipa_transcription])

def process_all_csv():
    """Processes all CSV files in the input directory."""
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
    
    if not files:
        print(f"No CSV files found in '{INPUT_DIR}'.")
        return

    for file in files:
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, file)
        process_csv(input_path, output_path)
        print(f"Processed {file} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Process a single file
        csv_filename = sys.argv[1]
        input_path = os.path.join(INPUT_DIR, csv_filename)
        output_path = os.path.join(OUTPUT_DIR, csv_filename)

        if not os.path.exists(input_path):
            print(f"Error: File '{csv_filename}' not found in '{INPUT_DIR}'.")
            sys.exit(1)
        
        process_csv(input_path, output_path)
        print(f"Processed {csv_filename} → {output_path}")
    else:
        # No argument provided, process all CSV files
        process_all_csv()
        print(f"All files processed! Check '{OUTPUT_DIR}'.")

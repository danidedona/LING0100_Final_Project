import os
import sys
import csv
import deepl
import argostranslate.package
import argostranslate.translate

# Define your input and output directories
INPUT_DIR = "data/raw_words"
OUTPUT_DIR = "data/translations"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
deepl_langs = [lang.code for lang in translator.get_source_languages()]


def translate_word(word, lang_code):
    """Translates a word into English using DeepL."""
    try:
        if lang_code.upper() not in deepl_langs:
            package_to_install = next(
                filter(
                    lambda x: x.from_code == lang_code and x.to_code == "en",
                    available_packages,
                ),
                None,
            )
            if package_to_install is None:
                raise Exception(
                    "Unsupported language code "
                    + lang_code
                    + " for translation to English."
                )
            argostranslate.package.install_from_path(package_to_install.download())
            return argostranslate.translate.translate(word, lang_code, "en")

        return translator.translate_text(
            text=word,
            source_lang=lang_code,
            target_lang="en-us",
            formality="prefer_less",
        ).text
    except Exception as e:
        return f"[Error: {str(e)}]"


def process_csv(input_file, output_file):
    """Processes a single CSV file, translating words into English."""
    with open(input_file, "r", encoding="utf-8") as infile, open(
        output_file, "w", encoding="utf-8", newline=""
    ) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Check if the file has a header row and add one to output if needed
        first_row = next(reader, None)
        if first_row is None:
            # Empty file
            writer.writerow(["Word", "English Translation"])
            return

        # Check if the first row looks like a header
        has_header = (
            "word" in str(first_row).lower() or "language" in str(first_row).lower()
        )

        if has_header:
            # Use the existing header
            writer.writerow(["Word", "English Translation"])
        else:
            # First row is data, not header - process it and add a header to output
            writer.writerow(["Word", "English Translation"])
            infile.seek(0)  # Reset to beginning of file

        # Process all rows
        for row in reader:
            if len(row) < 2:
                continue  # Skip invalid rows

            word, lang_code = row
            translation = translate_word(word.strip(), lang_code.strip())
            writer.writerow([word, translation])


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
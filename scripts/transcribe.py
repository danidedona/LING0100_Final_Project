import os
import epitran

# Path to the map directory
map_dir = os.path.join(os.path.dirname(epitran.__file__), 'data', 'map')

# List available language map files
available_langs = [os.path.splitext(f)[0] for f in os.listdir(map_dir) if f.endswith('.csv')]
print("Available language maps in Epitran:", available_langs)

# Check your current language code mappings against available ones
LANGUAGE_CODES = {
    'en': 'eng',
    'fr': 'fra',
    'it': 'ita',
    'es': 'spa',
    'pt': 'por',
    'ru': 'rus',
    'tr': 'tur',
    'zh': 'cmn-Hans',  # Mandarin (Simplified)
    'hi': 'hin-Deva',  # Hindi
    'fa': 'pes-Arab',  # Persian
}

print("\nChecking if your language codes exist:")
for short_code, lang_code in LANGUAGE_CODES.items():
    file_exists = os.path.exists(os.path.join(map_dir, f"{lang_code}.csv"))
    print(f"{short_code} -> {lang_code}: {'✓ Available' if file_exists else '✗ Not found'}")

# Try loading each language to check for additional issues
print("\nAttempting to initialize Epitran for each language:")
for short_code, lang_code in LANGUAGE_CODES.items():
    try:
        epi = epitran.Epitran(lang_code)
        print(f"{short_code} -> {lang_code}: ✓ Successfully loaded")
    except Exception as e:
        print(f"{short_code} -> {lang_code}: ✗ Error: {str(e)}")
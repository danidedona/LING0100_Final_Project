# LING0100_Final_Project

## ENV setup

1. conda create --name my_python python=3.11
2. conda activate my_python
3. pip install -r requirements.txt

## Setup

1. Clone the repo: git clone <your_repo_url>
2. Install dependencies: pip install -r requirements.txt

# json_to_csv.py

## Running json_to_csv.py

This Python script converts a JSON file containing swear words in different languages into individual CSV files for each language. Each CSV file will contain a list of words corresponding to a specific language.

Use the following command:

python3 scripts/json_to_csv.py [input_json_file]

Replace [input_json_file] with the path to your JSON file.

If no input file is specified, the script will default to data/swear.json.

# transcribe.py

## Supported Languages

This script currently supports the following languages:

| Language             | Code | Script             |
| -------------------- | ---- | ------------------ |
| English              | `en` | Latin              |
| French               | `fr` | Latin              |
| Italian              | `it` | Latin              |
| Spanish              | `es` | Latin              |
| Portuguese           | `pt` | Latin              |
| Russian              | `ru` | Cyrillic           |
| Turkish              | `tr` | Latin              |
| **Mandarin Chinese** | `zh` | Hanzi (Simplified) |
| **Hindi**            | `hi` | Devanagari         |
| **Persian (Farsi)**  | `fa` | Arabic             |

Available language maps in Epitran:

['hmn-Latn', 'spa-Latn', 'som-Latn', 'tir-Ethi-red', 'Goth2Latn', 'gan-Latn', 'zul-Latn', 'ben-Beng-east', 'ron-Latn', 'pii-latn_Wiktionary', 'ood-Latn-sax', 'uzb-Latn', 'lsm-Latn', 'xho-Latn', 'aze-Latn', 'lao-Laoo', 'hun-Latn', 'urd-Arab', 'tuk-Cyrl', 'mri-Latn', 'kmr-Latn-red', 'hrv-Latn', 'khm-Khmr', 'lao-Laoo-prereform', 'ckb-Arab', 'tir-Ethi-pp', 'sna-Latn', 'hsn-Latn', 'amh-Ethi-red', 'jpn-Ktkn-red', 'got-Latn', 'vie-Latn-so', 'cjy-Latn', 'ita-Latn', 'ava-Cyrl', 'kaz-Cyrl', 'tgk-Cyrl', 'ood-Latn-alv', 'jav-Latn', 'Latn2Goth', 'uig-Arab', 'jpn-Hrgn', 'swa-Latn-red', 'vie-Latn-ce', 'ceb-Latn', 'kin-Latn', 'fra-Latn', 'deu-Latn-np', 'ful-Latn', 'pan-Guru', 'nan-Latn-tl', 'nya-Latn', 'yor-Latn', 'sin-Sinh', 'fra-Latn-rev', 'yue-Latn', 'wuu-Latn', 'fin-Latn', 'aar-Latn', 'kmr-Latn', 'amh-Ethi', 'kaz-Cyrl-bab', 'kir-Arab', 'aii-Syrc', 'swa-Latn', 'uew', 'spa-Latn-eu', 'kir-Cyrl', 'srp-Latn', 'cat-Latn', 'mon-Cyrl-bab', 'ind-Latn', 'deu-Latn-nar', 'hak-Latn', 'run-Latn', 'jpn-Hrgn-red', 'fas-Arab', 'nan-Latn', 'tuk-Latn', 'tgl-Latn', 'nld-Latn', 'csb-Latn', 'kaz-Latn', 'mar-Deva', 'ara-Arab', 'zha-Latn', 'lav-Latn', 'mlt-Latn', 'rus-Cyrl', 'kat-Geor', 'jam-Latn', 'kor-Hang', 'deu-Latn', 'mya-Mymr', 'tam-Taml', 'ces-Latn', 'bxk-Latn', 'glg-Latn', 'vie-Latn-no', 'swe-Latn', 'hau-Latn', 'aze-Cyrl', 'fra-Latn-p', 'vie-Latn', 'orm-Latn', 'uzb-Cyrl', 'ben-Beng', 'kir-Latn', 'msa-Latn', 'generic-Latn', 'tam-Taml-red', 'ben-Beng-red', 'ori-Orya', 'est-Latn', 'cmn-Latn', 'kbd-Cyrl', 'pii-latn_Holopainen2019', 'sag-Latn', 'tur-Latn-red', 'por-Latn', 'tur-Latn', 'tgl-Latn-red', 'hin-Deva', 'mal-Mlym', 'lit-Latn', 'tha-Thai', 'srp-Cyrl', 'amh-Ethi-pp', 'tpi-Latn', 'jpn-Ktkn', 'hat-Latn-bab', 'fra-Latn-np', 'lez-Cyrl', 'tel-Telu', 'ilo-Latn', 'lij-Latn', 'sqi-Latn', 'pol-Latn', 'ukr-Cyrl', 'tir-Ethi', 'ltc-Latn-bax', 'epo-Latn', 'quy-Latn', 'tur-Latn-bab']

## Running the Script

You can run the transcription script in two ways:

1. Process All CSV Files
   If you run the script without any arguments, it will process all CSV files in the data/raw_words/ directory and save the transcribed output in data/raw_words_and_ipa/.

E.g. python3 scripts/transcribe.py

2. Process a Specific CSV File
   If you provide a filename as an argument, the script will only process that specific file from data/raw_words/ and save the transcribed output in data/raw_words_and_ipa/.

python3 scripts/transcribe.py myfile.csv

3. Handling Missing Files
   If the specified file does not exist in data/raw_words/, the script will print an error message and exit.

## Example Input (`data/swear_words.csv`)

```
merde,fr
fuck,en
perra,es
狗屎,zh
चूतिया,hi
کسکش,fa
```

## Example Output (`data/swear_words_ipa.csv`)

```
Word,Language,IPA
merde,fr,mɛʁd
fuck,en,fʌk
perra,es,ˈpera
狗屎,zh,kòʊʂʂɨ
चूतिया,hi,tʃuːtiːjaː
کسکش,fa,koskæʃ
```

Credits:

- Epitran: https://github.com/dmort27/epitran

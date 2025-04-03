# LING0100_Final_Project

# IPA Transcriber for Swear Words

## Description

This project transcribes swear words from various languages into IPA (International Phonetic Alphabet) using `epitran`.

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

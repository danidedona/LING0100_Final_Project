# LING0100_Final_Project

This project investigates the phonological structure and emotional valence of swear words across multiple languages. Using IPA transcription, sentiment analysis (via VADER), and phoneme-level statistical analysis, we explore whether there are universal trends in how profanity is constructed across cultures.

## ENV setup

1. conda create --name my_python python=3.11
2. conda activate my_python
3. pip install -r requirements.txt

## Setup

1. Clone the repo: git clone <your_repo_url>
2. Install dependencies: pip install -r requirements.txt




## Key Outputs

- **Phoneme Frequency:** Counts IPA symbols across all swears
- **Sentiment Binning:** Groups words by VADER valence
- **Correlation Analysis:** Correlates phoneme presence with sentiment
- **Sound Class Trends:** Analyzes vowels, plosives, fricatives, approximants, etc.



## Filtering Criteria

Words were only included in the final dataset if their **English translations contained a recognized curse word** from a predefined list. This may omit culturally offensive phrases without direct English equivalents.



## References & Data Sources

- **Epitran (G2P transcription):**  
  https://github.com/dmort27/epitran

- **Datasets:**  
  - https://www.kaggle.com/datasets/miklgr500/jigsaw-multilingual-swear-profanity  
  - https://github.com/chingachleung/Chinese_Hate_Speech-Baseline-  
  - https://www.kaggle.com/code/mpwolke/hindi-swear-words  
  - https://www.kaggle.com/code/mpwolke/persian-swear-words


## Authors

- **Daniela DeDona** – Lead developer, data processing, analysis scripting  
- **Ilija Ivanov** – Translation, language-specific analysis scripts  
- **Maya Muravlev** – Proposal writing, literature review, slides, analysis confirmation

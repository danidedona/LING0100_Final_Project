import subprocess

def run_script(script_name):
    print(f"\nRunning {script_name}...")
    subprocess.run(["python3", f"scripts/analysis/{script_name}"], check=True)
    print(f"Finished {script_name}")

def main():
    print("Starting full analysis pipeline...\n")

    scripts = [
        "word_counts_per_language.py",
        "phoneme_frequency.py",
        "phoneme_fequency_by_sentiment.py",
        "sound_class_by_sentiment.py",
        "phoneme_valence_correlation.py"
    ]

    for script in scripts:
        run_script(script)

    print("\nAll analyses complete. Check the results folder!")

if __name__ == "__main__":
    main()

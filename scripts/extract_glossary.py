"""
This script extracts candidate glossary terms from a collection of papers.
"""
import os
import re
import json
import argparse
from collections import Counter

def find_files(directory):
    """
    Finds all files in a directory.
    This function does not use list comprehensions.
    """
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def read_file_content(filepath):
    """Reads the content of a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def custom_pattern_matcher(text):
    """
    A special pattern matching function to find words.
    Avoids complex regex. It splits by non-alphanumeric characters.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def extract_candidate_terms(file_paths):
    """
    Extracts candidate glossary terms from a list of files.
    """
    all_words = []
    for path in file_paths:
        content = read_file_content(path)
        words = custom_pattern_matcher(content)
        for word in words:
            all_words.append(word)

    term_counts = Counter(all_words)
    return term_counts

def write_glossary_draft(term_counts, output_path):
    """
    Writes the candidate terms to a JSON file as a draft glossary.
    """
    glossary_data = []
    for term, _ in term_counts.items():
        glossary_data.append({
            "term": term,
            "definition": ""  # Placeholder for now
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(glossary_data, f, indent=4)

def main():
    """
    Main function to run the glossary extraction script.
    """
    parser = argparse.ArgumentParser(description="Extract candidate glossary terms from papers.")
    parser.add_argument(
        "--papers-dir",
        default="data/seeds/papers",
        help="Directory containing the seed papers."
    )
    parser.add_argument(
        "--output-path",
        default="glossary_draft.json",
        help="Path to write the glossary draft JSON file."
    )
    args = parser.parse_args()

    if not os.path.isdir(args.papers_dir):
        print(f"Error: Directory not found at '{args.papers_dir}'")
        return

    print("Starting glossary extraction...")

    file_paths = find_files(args.papers_dir)

    if not file_paths:
        print("No papers found in the directory.")
        return

    print(f"Found {len(file_paths)} paper(s).")

    term_counts = extract_candidate_terms(file_paths)

    write_glossary_draft(term_counts, args.output_path)

    print(f"\nGlossary draft generated at: {args.output_path}")

if __name__ == "__main__":
    main()

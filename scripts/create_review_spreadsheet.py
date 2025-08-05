"""
This script creates a CSV spreadsheet for reviewing glossary terms.
"""
import json
import csv
import argparse

def create_review_spreadsheet(json_path, csv_path):
    """
    Creates a CSV spreadsheet for reviewing glossary terms.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            glossary_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at '{json_path}'")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{json_path}'")
        return

    headers = ["term", "definition", "approved", "comments"]

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for entry in glossary_data:
            row = {
                "term": entry.get("term", ""),
                "definition": entry.get("definition", ""),
                "approved": "",  # Placeholder for reviewer
                "comments": ""    # Placeholder for reviewer
            }
            writer.writerow(row)

def main():
    """
    Main function to run the script.
    """
    parser = argparse.ArgumentParser(
        description="Create a review spreadsheet from a glossary JSON file."
    )
    parser.add_argument(
        "--json-path",
        default="glossary_draft.json",
        help="Path to the glossary draft JSON file."
    )
    parser.add_argument(
        "--csv-path",
        default="glossary_review.csv",
        help="Path to write the review CSV file."
    )
    args = parser.parse_args()

    print(f"Creating review spreadsheet from '{args.json_path}'...")
    create_review_spreadsheet(args.json_path, args.csv_path)
    print(f"Review spreadsheet created at '{args.csv_path}'")

if __name__ == "__main__":
    main()

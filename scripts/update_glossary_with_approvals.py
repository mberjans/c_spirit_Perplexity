import json
import csv
import argparse

def update_glossary_with_approvals(csv_path, json_path):
    """
    Updates the glossary JSON file with approvals from a CSV file.
    """
    try:
        with open(csv_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            reviewed_terms = {row['term']: row for row in reader}
    except FileNotFoundError:
        print(f"Error: Reviewed CSV file not found at '{csv_path}'")
        return

    updated_glossary = []
    for term, review_data in reviewed_terms.items():
        if review_data.get('approved', '').lower() == 'yes':
            updated_glossary.append({
                "term": term,
                "definition": review_data.get('definition', ''),
                "approved": True
            })

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(updated_glossary, f, indent=4)

def main():
    """
    Main function to run the script.
    """
    parser = argparse.ArgumentParser(
        description="Update glossary JSON with approvals from a CSV file."
    )
    parser.add_argument(
        "--csv-path",
        default="glossary_reviewed.csv",
        help="Path to the reviewed glossary CSV file."
    )
    parser.add_argument(
        "--json-path",
        default="glossary_approved.json",
        help="Path to write the updated, approved glossary JSON file."
    )
    args = parser.parse_args()

    print(f"Updating glossary from '{args.csv_path}'...")
    update_glossary_with_approvals(args.csv_path, args.json_path)
    print(f"Approved glossary created at '{args.json_path}'")

if __name__ == "__main__":
    main()

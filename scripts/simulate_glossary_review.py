import csv
import argparse

def simulate_review(input_csv_path, output_csv_path):
    """
    Simulates a review of the glossary CSV file.
    Approves about half of the terms and adds dummy definitions.
    """
    try:
        with open(input_csv_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Error: Input CSV file not found at '{input_csv_path}'")
        return

    for i, row in enumerate(rows):
        if i % 2 == 0:
            row['approved'] = 'yes'
            row['definition'] = f"This is a definition for '{row['term']}'."
            row['comments'] = "Looks good."
        else:
            row['approved'] = 'no'
            row['comments'] = "Not relevant."

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    """
    Main function to run the script.
    """
    parser = argparse.ArgumentParser(description="Simulate the review of a glossary CSV file.")
    parser.add_argument(
        "--input-csv",
        default="glossary_review.csv",
        help="Path to the input glossary review CSV file."
    )
    parser.add_argument(
        "--output-csv",
        default="glossary_reviewed.csv",
        help="Path to write the output reviewed CSV file."
    )
    args = parser.parse_args()

    print(f"Simulating review for '{args.input_csv}'...")
    simulate_review(args.input_csv, args.output_csv)
    print(f"Reviewed glossary created at '{args.output_csv}'")

if __name__ == "__main__":
    main()

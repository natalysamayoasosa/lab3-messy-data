import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

regex_file = BASE_DIR / "output" / "regex_cleaned_sequences.csv"
ai_file = BASE_DIR / "output" / "ai_cleaned_sequences.csv"
comparison_file = BASE_DIR / "output" / "comparison_results.csv"


def read_csv(file_path):
    with open(file_path, "r", newline="") as file:
        return list(csv.DictReader(file))


regex_records = read_csv(regex_file)
ai_records = read_csv(ai_file)

fields = [
    "sample_id",
    "organism",
    "gene",
    "reported_length",
    "actual_sequence_length",
    "sequence"
]

comparison_rows = []

for regex_record, ai_record in zip(regex_records, ai_records):
    for field in fields:
        regex_value = regex_record[field]
        ai_value = ai_record[field]

        comparison_rows.append({
            "sample_id": regex_record["sample_id"],
            "field": field,
            "regex_value": regex_value,
            "ai_value": ai_value,
            "match": regex_value == ai_value
        })

with open(comparison_file, "w", newline="") as file:
    fieldnames = [
        "sample_id",
        "field",
        "regex_value",
        "ai_value",
        "match"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(comparison_rows)

matches = sum(row["match"] for row in comparison_rows)
total = len(comparison_rows)

print(f"Matching fields: {matches}/{total}")
print(f"Disagreements: {total - matches}")

for row in comparison_rows:
    if not row["match"]:
        print(
            row["sample_id"],
            row["field"],
            row["regex_value"],
            row["ai_value"]
        )

print(f"Comparison written to: {comparison_file}")
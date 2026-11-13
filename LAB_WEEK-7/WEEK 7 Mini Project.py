"""
RECORD CHECK  -  my version
===========================

Name  : Ahir Siddhi
Lane  :  AI     
Date  : 13/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def parse_line(raw_line):
    """Clean and parse one survey record."""
    parts = raw_line.strip().lower().split(",")

    record = {}
    record["survey"] = parts[0].strip()

    for part in parts[1:]:
        key, value = part.split("=")
        record[key.strip()] = float(value.strip())

    return record


def status_of(record):
    """Return the status of a survey record."""
    if record["rating"] < 1 or record["rating"] > 5:
        return "FLAGGED"
    elif record["age"] < 18:
        return "FLAGGED"
    else:
        return "OK"

raw_records = []

with open("survey_records.txt", "r") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)

flagged_count = 0
total_records = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record)
    print("Status:", status)

    total_records += 1

    if status == "FLAGGED":
        flagged_count += 1

print("\nSUMMARY")
print("Total records:", total_records)
print("Flagged records:", flagged_count)











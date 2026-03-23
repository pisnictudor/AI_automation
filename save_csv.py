import csv

def save_to_csv(filename, rows):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID",
                "Title",
                "Summary",
                "Tone",
                "Priority",
                "Recommended Action"
            ])
            writer.writerows(rows)
    except OSError as e:
        print(f"Error while saving CSV: {e}")
        
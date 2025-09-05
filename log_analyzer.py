import csv
from collections import Counter

def analyze_log(file_path):
    counts = Counter()
    with open(file_path, "r") as f:
        for line in f:
            if "ERROR" in line:
                counts["ERROR"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "INFO" in line:
                counts["INFO"] += 1
    return counts

def save_report(counts, filename="report.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Count"])
        for k, v in counts.items():
            writer.writerow([k, v])

if __name__ == "__main__":
    result = analyze_log("system.log")
    print("Log Summary:", result)
    save_report(result)
    print("Report saved as report.csv")


"""
Topic: File Handling
Read and write text and CSV files safely using the 'with' context manager,
which automatically closes the file even if an error occurs.
"""

import csv
from pathlib import Path

# Store generated example files next to this script, regardless of the current
# working directory the script happens to be run from.
DATA_DIR = Path(__file__).parent / "sample_data"
DATA_DIR.mkdir(exist_ok=True)

TEXT_FILE = DATA_DIR / "notes.txt"
CSV_FILE = DATA_DIR / "students.csv"

# --- 1. Writing a Text File ---
# 'w' mode creates the file if it's missing, or overwrites it if it exists.
print("--- Writing a Text File ---")
with open(TEXT_FILE, "w", encoding="utf-8") as file:
    file.write("Line 1: Learning Python file handling.\n")
    file.write("Line 2: The 'with' statement auto-closes the file.\n")
print(f"Wrote to {TEXT_FILE}")

# --- 2. Reading an Entire Text File ---
print("\n--- Reading a Text File (read()) ---")
with open(TEXT_FILE, "r", encoding="utf-8") as file:
    contents = file.read()
print(contents)

# --- 3. Reading a Text File Line by Line ---
print("--- Reading a Text File (line by line) ---")
with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"  Line {line_number}: {line.strip()}")

# --- 4. Appending to a Text File ---
# 'a' mode adds to the end of the file instead of overwriting existing content.
print("\n--- Appending to a Text File ---")
with open(TEXT_FILE, "a", encoding="utf-8") as file:
    file.write("Line 3: Appended without erasing previous content.\n")
with open(TEXT_FILE, "r", encoding="utf-8") as file:
    print(file.read())

# --- 5. Writing a CSV File ---
print("--- Writing a CSV File ---")
students = [
    ["Name", "Age", "Major"],
    ["Alice", 22, "Computer Science"],
    ["Bob", 24, "Mathematics"],
    ["Charlie", 21, "Physics"],
]
with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print(f"Wrote to {CSV_FILE}")

# --- 6. Reading a CSV File ---
print("\n--- Reading a CSV File (csv.reader) ---")
with open(CSV_FILE, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  Row: {row}")

# --- 7. Reading a CSV File as Dictionaries ---
# DictReader uses the header row as keys, making each row easier to work with.
print("\n--- Reading a CSV File (csv.DictReader) ---")
with open(CSV_FILE, "r", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(f"  {row['Name']} ({row['Age']}) studies {row['Major']}")

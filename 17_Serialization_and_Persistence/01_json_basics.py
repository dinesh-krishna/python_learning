"""
Topic: JSON Serialization
The json module converts Python objects to/from JSON text, the standard
format for APIs, config files, and data interchange between languages.
"""

import json
from pathlib import Path

# --- 1. Serializing Python Objects to a JSON String ---
print("--- json.dumps(): Python -> JSON string ---")
person = {
    "name": "Alice",
    "age": 30,
    "is_member": True,
    "hobbies": ["reading", "chess"],
    "address": None,
}
json_string = json.dumps(person)
print(f"Compact: {json_string}")

pretty_json = json.dumps(person, indent=2, sort_keys=True)
print(f"\nPretty-printed:\n{pretty_json}")

# --- 2. Deserializing a JSON String Back to Python ---
print("\n--- json.loads(): JSON string -> Python ---")
raw_json = '{"title": "Dune", "year": 1965, "authors": ["Frank Herbert"]}'
book = json.loads(raw_json)
print(f"Parsed dict: {book}")
print(f"type(book) = {type(book)}")
print(f"book['title'] = {book['title']}")

# --- 3. Python <-> JSON Type Mapping ---
print("\n--- Type Mapping ---")
print(f"Python True  -> JSON: {json.dumps(True)}")
print(f"Python None  -> JSON: {json.dumps(None)}")
print(f"Python tuple -> JSON (becomes an array): {json.dumps((1, 2, 3))}")

# --- 4. Reading and Writing JSON Files ---
DATA_FILE = Path(__file__).parent / "sample_data.json"

print("\n--- Writing and Reading a JSON File ---")
with open(DATA_FILE, "w", encoding="utf-8") as file:
    json.dump(person, file, indent=2)
print(f"Wrote JSON to {DATA_FILE}")

with open(DATA_FILE, "r", encoding="utf-8") as file:
    loaded_person = json.load(file)
print(f"Loaded back: {loaded_person}")


# --- 5. Handling Non-Serializable Objects ---
print("\n--- Handling Non-Serializable Objects ---")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_to_dict(obj):
    """Custom 'default' function: tells json how to serialize an unknown type."""
    if isinstance(obj, Point):
        return {"x": obj.x, "y": obj.y}
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


point = Point(3, 4)
try:
    json.dumps(point)
except TypeError as error:
    print(f"Without a custom encoder: {error}")

print(f"With a custom encoder: {json.dumps(point, default=point_to_dict)}")

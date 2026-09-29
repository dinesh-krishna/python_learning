"""
Topic: pickle and shelve
pickle serializes arbitrary Python objects (not just JSON-safe ones) to bytes,
Python-to-Python. shelve builds a persistent, dictionary-like store on top of
pickle. Never unpickle data from an untrusted source - it can execute code.
"""

import pickle
import shelve
from pathlib import Path


# --- 1. pickle: Serializing Arbitrary Python Objects ---
class Employee:
    """A plain object with no special JSON support - pickle handles it directly."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name!r}, salary={self.salary})"


print("--- pickle.dumps() / pickle.loads() (in-memory) ---")
employee = Employee("Bob", 65000)
pickled_bytes = pickle.dumps(employee)
print(f"Pickled bytes (truncated): {pickled_bytes[:30]}...")

restored_employee = pickle.loads(pickled_bytes)
print(f"Restored object: {restored_employee}")
print(f"Restored is a real Employee instance: {isinstance(restored_employee, Employee)}")

# --- 2. Pickling to and from a File ---
PICKLE_FILE = Path(__file__).parent / "employee.pkl"

print("\n--- Pickling to a File ---")
with open(PICKLE_FILE, "wb") as file:  # "wb" = write binary
    pickle.dump(employee, file)
print(f"Wrote pickle to {PICKLE_FILE}")

with open(PICKLE_FILE, "rb") as file:  # "rb" = read binary
    loaded_employee = pickle.load(file)
print(f"Loaded from file: {loaded_employee}")

# --- 3. Security Warning ---
print("\n--- Security Warning ---")
print("  Never call pickle.load() on data from an untrusted source:")
print("  unpickling can execute arbitrary code embedded in the byte stream.")

# --- 4. shelve: A Persistent, Dict-Like Store Built on pickle ---
SHELF_FILE = Path(__file__).parent / "employee_shelf"

print("\n--- shelve: Persistent Key-Value Storage ---")
with shelve.open(str(SHELF_FILE)) as shelf:
    shelf["bob"] = Employee("Bob", 65000)
    shelf["alice"] = Employee("Alice", 72000)
    print(f"Keys stored: {list(shelf.keys())}")

# Reopening later still sees the previously stored data - it persists to disk.
with shelve.open(str(SHELF_FILE)) as shelf:
    print(f"Re-opened shelf, 'alice' -> {shelf['alice']}")

"""
Topic: Dictionaries and Sets
Dictionaries store key-value pairs; sets store unique, unordered elements.
"""

# --- 1. Creating a Dictionary ---
student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science",
}
print("--- Dictionary Basics ---")
print(f"Student record: {student}")
print(f"Name: {student['name']}")
print(f"Age via get(): {student.get('age')}")
print(f"Missing key via get() with default: {student.get('gpa', 'N/A')}")

# --- 2. Modifying a Dictionary ---
print("\n--- Modifying a Dictionary ---")
student["gpa"] = 3.8               # add a new key
print(f"After adding 'gpa': {student}")
student["age"] = 22                # update an existing key
print(f"After updating 'age': {student}")
del student["major"]               # remove a key
print(f"After deleting 'major': {student}")

# --- 3. Dictionary Methods ---
print("\n--- Dictionary Methods ---")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

print("\nIterating with .items():")
for key, value in student.items():
    print(f"  {key}: {value}")

# --- 4. Creating Sets ---
print("\n--- Set Basics ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"set_a: {set_a}")
print(f"set_b: {set_b}")

# Sets automatically remove duplicates.
duplicates = [1, 2, 2, 3, 3, 3]
unique_values = set(duplicates)
print(f"Set built from duplicates {duplicates}: {unique_values}")

# --- 5. Set Operations ---
print("\n--- Set Operations ---")
print(f"Union (a | b): {set_a | set_b}")
print(f"Intersection (a & b): {set_a & set_b}")
print(f"Difference (a - b): {set_a - set_b}")
print(f"Symmetric difference (a ^ b): {set_a ^ set_b}")

set_a.add(10)         # add a single element
set_a.discard(1)      # remove an element if present (no error if it's missing)
print(f"\nAfter add(10) and discard(1): {set_a}")

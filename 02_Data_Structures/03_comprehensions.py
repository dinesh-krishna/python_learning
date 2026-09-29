"""
Topic: Comprehensions
Concise, readable syntax for building lists, dictionaries, and sets from iterables.
"""

# --- 1. List Comprehension ---
# Syntax: [expression for item in iterable if condition]
print("--- List Comprehensions ---")
squares = [number ** 2 for number in range(1, 6)]
print(f"Squares 1-5: {squares}")

even_squares = [number ** 2 for number in range(1, 11) if number % 2 == 0]
print(f"Squares of even numbers 1-10: {even_squares}")

# Equivalent traditional loop, shown for comparison:
traditional_squares = []
for number in range(1, 6):
    traditional_squares.append(number ** 2)
print(f"Same result using a traditional loop: {traditional_squares}")

# --- 2. Nested List Comprehension ---
print("\n--- Nested List Comprehension ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [value for row in matrix for value in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# --- 3. Dictionary Comprehension ---
# Syntax: {key_expression: value_expression for item in iterable if condition}
print("\n--- Dictionary Comprehensions ---")
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")

celsius_temps = {"morning": 15, "noon": 25, "evening": 18}
fahrenheit_temps = {time: (temp * 9 / 5) + 32 for time, temp in celsius_temps.items()}
print(f"Celsius: {celsius_temps}")
print(f"Converted to Fahrenheit: {fahrenheit_temps}")

# --- 4. Set Comprehension ---
# Syntax: {expression for item in iterable if condition}
print("\n--- Set Comprehensions ---")
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_lengths = {len(word) for word in words}
print(f"Words: {words}")
print(f"Unique word lengths: {unique_lengths}")

"""
Topic: itertools Essentials
The itertools module provides fast, memory-efficient tools for working with
iterators: infinite sequences, combinatorics, and grouping.
"""

import itertools

# --- 1. Infinite Iterators (use with caution - always bound with islice/break) ---
print("--- Infinite Iterators ---")
counted = list(itertools.islice(itertools.count(start=10, step=5), 4))
print(f"itertools.count(10, step=5) -> first 4: {counted}")

cycled = list(itertools.islice(itertools.cycle(["A", "B", "C"]), 7))
print(f"itertools.cycle(['A','B','C']) -> first 7: {cycled}")

repeated = list(itertools.repeat("x", 4))
print(f"itertools.repeat('x', 4): {repeated}")

# --- 2. Combining Iterables ---
print("\n--- Combining Iterables ---")
chained = list(itertools.chain([1, 2], [3, 4], [5]))
print(f"itertools.chain([1,2], [3,4], [5]): {chained}")

zipped_longest = list(itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))
print(f"itertools.zip_longest: {zipped_longest}")

# --- 3. Combinatorics ---
print("\n--- Combinatorics ---")
letters = ["A", "B", "C"]
permutations = list(itertools.permutations(letters, 2))
combinations = list(itertools.combinations(letters, 2))
products = list(itertools.product([0, 1], repeat=2))
print(f"permutations(letters, 2): {permutations}")
print(f"combinations(letters, 2): {combinations}")
print(f"product([0,1], repeat=2): {products}")

# --- 4. Grouping Consecutive Items ---
# groupby only groups CONSECUTIVE equal keys, so input is often sorted first.
print("\n--- itertools.groupby ---")
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
for first_letter, group in itertools.groupby(words, key=lambda word: word[0]):
    print(f"  Group '{first_letter}': {list(group)}")

# --- 5. Accumulate: Running Totals ---
print("\n--- itertools.accumulate ---")
numbers = [1, 2, 3, 4, 5]
running_totals = list(itertools.accumulate(numbers))
running_max = list(itertools.accumulate(numbers, func=max))
print(f"Running totals of {numbers}: {running_totals}")
print(f"Running max of {numbers}: {running_max}")

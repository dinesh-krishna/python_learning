"""
Topic: collections - Counter, defaultdict, namedtuple
The collections module provides specialized container datatypes that solve
common problems more cleanly than plain lists/dicts/tuples.
"""

from collections import Counter, defaultdict, namedtuple

# --- 1. Counter: Counting Hashable Items ---
print("--- Counter ---")
words = "the quick brown fox jumps over the lazy dog the fox runs".split()
word_counts = Counter(words)
print(f"Word counts: {word_counts}")
print(f"Most common 2: {word_counts.most_common(2)}")
print(f"Count of 'the': {word_counts['the']}")
print(f"Count of missing word (no KeyError): {word_counts['cat']}")

# Counters support arithmetic operations.
inventory_a = Counter(apples=10, bananas=5)
inventory_b = Counter(apples=3, bananas=2, cherries=7)
print(f"\ninventory_a + inventory_b: {inventory_a + inventory_b}")
print(f"inventory_a - inventory_b: {inventory_a - inventory_b}")  # drops non-positive counts

# --- 2. defaultdict: Dictionaries with Automatic Default Values ---
print("\n--- defaultdict ---")
# A plain dict raises KeyError on a missing key; defaultdict auto-creates one.
groups = defaultdict(list)
pairs = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "potato")]
for category, item in pairs:
    groups[category].append(item)  # no need to check "if category not in groups"
print(f"Grouped items: {dict(groups)}")

# defaultdict(int) is a common pattern for counting.
letter_counts = defaultdict(int)
for letter in "mississippi":
    letter_counts[letter] += 1
print(f"Letter counts via defaultdict(int): {dict(letter_counts)}")

# --- 3. namedtuple: Lightweight, Immutable, Self-Documenting Records ---
print("\n--- namedtuple ---")
Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)
print(f"p1 = {p1}")
print(f"p1.x = {p1.x}, p1.y = {p1.y}")        # access by name, not just index
print(f"p1[0] = {p1[0]}, p1[1] = {p1[1]}")    # still supports tuple indexing

# namedtuples are immutable, like regular tuples.
try:
    p1.x = 99
except AttributeError as error:
    print(f"Cannot modify a namedtuple: {error}")

# ._replace() returns a NEW namedtuple with specified fields changed.
p2 = p1._replace(x=10)
print(f"p1 (unchanged): {p1}")
print(f"p2 (from _replace): {p2}")
print(f"p1._asdict(): {p1._asdict()}")

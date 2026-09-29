"""
Topic: Iterators and Generators
Understand the iteration protocol and how generators simplify creating iterators.
"""

# --- 1. Iterables vs. Iterators ---
# An iterable can produce an iterator (via iter()); an iterator yields values
# one at a time (via next()) and remembers its position between calls.
print("--- Iterables vs. Iterators ---")
numbers_list = [10, 20, 30]     # a list is iterable
iterator = iter(numbers_list)   # get an iterator from it
print(f"type(numbers_list): {type(numbers_list)}")
print(f"type(iterator): {type(iterator)}")
print(f"next(iterator): {next(iterator)}")
print(f"next(iterator): {next(iterator)}")
print(f"next(iterator): {next(iterator)}")

try:
    next(iterator)
except StopIteration:
    print("StopIteration raised: the iterator is exhausted.")


# --- 2. Building a Custom Iterator Class ---
class CountUpTo:
    """A custom iterator that counts up to a maximum value."""

    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        """Required so the object can be used in a for loop / with iter()."""
        return self

    def __next__(self):
        """Required so the object supports next(); raises StopIteration when done."""
        if self.current >= self.maximum:
            raise StopIteration
        self.current += 1
        return self.current


print("\n--- Custom Iterator Class ---")
for number in CountUpTo(5):
    print(f"CountUpTo value: {number}")


# --- 3. Generator Functions with yield ---
# 'yield' pauses the function, remembering its state, and resumes on the next call.
# Generators produce values lazily, one at a time, instead of building a full list.
def count_up_to_generator(maximum):
    """Generator equivalent of the CountUpTo class above - far less code."""
    current = 1
    while current <= maximum:
        yield current
        current += 1


print("\n--- Generator Function ---")
for number in count_up_to_generator(5):
    print(f"Generator value: {number}")

# --- 4. Generators Are Lazy (Memory-Efficient) ---
# Values are computed on demand, not stored all at once - useful for huge sequences.
print("\n--- Generator Laziness ---")
generator = count_up_to_generator(1_000_000)
print(f"Generator object created instantly: {generator}")
print(f"First value pulled on demand: {next(generator)}")
print(f"Second value pulled on demand: {next(generator)}")

# --- 5. Generator Expressions ---
# Like a list comprehension, but with () instead of [] - lazy and memory-efficient.
print("\n--- Generator Expressions ---")
squares_generator = (n ** 2 for n in range(1, 6))
print(f"Generator expression object: {squares_generator}")
print(f"Consumed as a list: {list(squares_generator)}")

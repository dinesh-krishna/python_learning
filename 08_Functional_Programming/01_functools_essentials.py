"""
Topic: functools Essentials
The functools module provides higher-order functions that operate on or
return other functions: reduce, partial, lru_cache, and more.
"""

import functools

# --- 1. functools.reduce: Fold a Sequence into a Single Value ---
# reduce(function, iterable, initial) repeatedly applies function(accumulator, item).
print("--- functools.reduce ---")
numbers = [1, 2, 3, 4, 5]
total = functools.reduce(lambda acc, n: acc + n, numbers)
product = functools.reduce(lambda acc, n: acc * n, numbers, 1)
print(f"Sum via reduce: {total}")
print(f"Product via reduce: {product}")

# --- 2. functools.partial: Pre-fill Some Arguments ---
# Creates a new callable with certain arguments already fixed.
print("\n--- functools.partial ---")


def power(base, exponent):
    return base ** exponent


square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)
print(f"square(5) = {square(5)}")
print(f"cube(2) = {cube(2)}")

# --- 3. functools.lru_cache: Memoization ---
# Caches return values for given inputs, avoiding repeated expensive computation.
call_count = 0


@functools.lru_cache(maxsize=None)
def fibonacci(n):
    """Return the n-th Fibonacci number, using memoized recursion."""
    global call_count
    call_count += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n--- functools.lru_cache ---")
print(f"fibonacci(20) = {fibonacci(20)}")
print(f"Function calls made (cached): {call_count}")
print(f"Cache info: {fibonacci.cache_info()}")


# --- 4. functools.total_ordering: Fill in Comparison Methods ---
# Define __eq__ and one other comparison (__lt__); the rest are generated for you.
@functools.total_ordering
class Version:
    """A simple version number that supports full ordering from just 2 methods."""

    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self):
        return f"Version({self.major}.{self.minor})"


print("\n--- functools.total_ordering ---")
v1 = Version(1, 5)
v2 = Version(2, 0)
print(f"{v1} < {v2}: {v1 < v2}")
print(f"{v1} > {v2}: {v1 > v2}")    # generated automatically from __lt__/__eq__
print(f"{v1} <= {v2}: {v1 <= v2}")  # generated automatically

"""
Topic: Type Hints
Type hints document expected argument/return types and enable static checkers
(mypy, Pylance) to catch bugs before running the code. Python does NOT enforce
them at runtime - they are purely informational unless checked by a tool.
"""

from typing import Optional, Union


# --- 1. Basic Function Annotations ---
def add(a: int, b: int) -> int:
    """Add two integers; '-> int' documents the return type."""
    return a + b


print("--- Basic Function Annotations ---")
print(f"add(2, 3) = {add(2, 3)}")
print(f"Annotations: {add.__annotations__}")

# --- 2. Variable Annotations ---
name: str = "Alice"
scores: list[int] = [90, 85, 78]  # built-in generics (Python 3.9+)
print("\n--- Variable Annotations ---")
print(f"name: str = {name}")
print(f"scores: list[int] = {scores}")


# --- 3. Optional and Union ---
# Optional[X] means "X or None"; Union[X, Y] means "X or Y".
def find_user(user_id: int) -> Optional[str]:
    """Return a username, or None if no matching user exists."""
    users = {1: "alice", 2: "bob"}
    return users.get(user_id)


def parse_value(raw: Union[str, int]) -> int:
    """Accept either a string or an int and return an int."""
    return int(raw)


print("\n--- Optional and Union ---")
print(f"find_user(1) = {find_user(1)}")
print(f"find_user(99) = {find_user(99)}")
print(f"parse_value('42') = {parse_value('42')}")
print(f"parse_value(42) = {parse_value(42)}")


# Modern syntax (Python 3.10+): use '|' instead of Union/Optional.
def parse_value_modern(raw: str | int) -> int:
    """Same as parse_value(), using the newer '|' union syntax."""
    return int(raw)


print(f"parse_value_modern(42) = {parse_value_modern(42)}")


# --- 4. Type Hints for Collections ---
def average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length."""
    return {word: len(word) for word in words}


print("\n--- Collection Type Hints ---")
print(f"average([1.0, 2.0, 3.0]) = {average([1.0, 2.0, 3.0])}")
print(f"word_lengths(['hi', 'python']) = {word_lengths(['hi', 'python'])}")

# --- 5. Type Hints Are Not Enforced at Runtime ---
# Python will happily run this even though it violates the hint - hints are
# only checked by external tools like mypy or Pylance, not by the interpreter.
print("\n--- Type Hints Are Not Enforced at Runtime ---")
print(f"add('2', '3') still runs (string concatenation): {add('2', '3')}")

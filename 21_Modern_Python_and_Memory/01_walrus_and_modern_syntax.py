"""
Topic: Modern Python Syntax
A tour of newer language features that make code more concise and explicit:
the walrus operator, positional/keyword-only parameters, and f-string '='.
"""

# --- 1. The Walrus Operator (:=), Python 3.8+ ---
# Assigns a value AND returns it in the same expression - useful for avoiding
# repeated computation inside conditions/loops.
print("--- Walrus Operator (:=) ---")

data = [1, 2, 3, 4, 5, 6, 7, 8]

# Without walrus: compute len(data) once, store it, then use it.
n = len(data)
if n > 5:
    print(f"Without walrus: list has {n} items (> 5)")

# With walrus: compute AND check in a single expression.
if (count := len(data)) > 5:
    print(f"With walrus: list has {count} items (> 5)")

# Very common in while loops that read until some "empty" sentinel:
print("\nWalrus in a loop (simulated input queue):")
inputs = iter(["first", "second", "", "never reached"])
while (line := next(inputs)) != "":
    print(f"  Processing: {line}")

# --- 2. Positional-Only and Keyword-Only Parameters, Python 3.8+ ---
# '/' marks everything before it as positional-only; '*' marks everything
# after it as keyword-only. This makes function signatures self-documenting.
print("\n--- Positional-Only and Keyword-Only Parameters ---")


def create_user(username, password, /, *, is_admin=False):
    """'username'/'password' must be positional; 'is_admin' must be named."""
    return f"User(username={username}, is_admin={is_admin})"


print(create_user("alice", "hunter2", is_admin=True))
try:
    create_user(username="alice", password="hunter2")  # fails: not allowed as keywords
except TypeError as error:
    print(f"Positional-only violation caught: {error}")

try:
    create_user("alice", "hunter2", True)  # fails: is_admin must be passed by keyword
except TypeError as error:
    print(f"Keyword-only violation caught: {error}")

# --- 3. f-string '=' Debug Specifier, Python 3.8+ ---
# Automatically prints both the expression's source text and its value.
print("\n--- f-string '=' Debug Specifier ---")
width = 12
height = 5
print(f"{width=}")
print(f"{height=}")
print(f"{width * height=}")

# --- 4. Structural Pattern Matching on Data Shapes, Python 3.10+ ---
# match-case can also destructure lists/dicts/objects, not just literal values.
print("\n--- Structural Pattern Matching ---")


def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On the X-axis at {x}"
        case (0, y):
            return f"On the Y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"


for sample in [(0, 0), (5, 0), (0, -3), (2, 4), "not a tuple"]:
    print(f"  describe_point({sample!r}) -> {describe_point(sample)}")

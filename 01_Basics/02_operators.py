"""
Topic: Operators
Explore arithmetic, comparison, logical, and assignment operators in Python.
"""

# --- 1. Arithmetic Operators ---
a, b = 17, 5
print("--- Arithmetic Operators ---")
print(f"{a} + {b} = {a + b}")     # addition
print(f"{a} - {b} = {a - b}")     # subtraction
print(f"{a} * {b} = {a * b}")     # multiplication
print(f"{a} / {b} = {a / b}")     # true division (always returns a float)
print(f"{a} // {b} = {a // b}")   # floor division (drops the remainder)
print(f"{a} % {b} = {a % b}")     # modulus (remainder only)
print(f"{a} ** {b} = {a ** b}")   # exponentiation

# --- 2. Comparison Operators ---
# Always evaluate to a bool: True or False.
print("\n--- Comparison Operators ---")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# --- 3. Logical Operators ---
# Combine boolean expressions; Python short-circuits and/or evaluation.
is_adult = True
has_ticket = False
print("\n--- Logical Operators ---")
print(f"is_adult and has_ticket: {is_adult and has_ticket}")
print(f"is_adult or has_ticket: {is_adult or has_ticket}")
print(f"not is_adult: {not is_adult}")

# --- 4. Assignment Operators ---
# Shorthand for updating a variable based on its current value.
counter = 10
print("\n--- Assignment Operators ---")
print(f"Initial counter: {counter}")
counter += 5   # same as counter = counter + 5
print(f"After += 5: {counter}")
counter -= 3
print(f"After -= 3: {counter}")
counter *= 2
print(f"After *= 2: {counter}")
counter //= 4
print(f"After //= 4: {counter}")

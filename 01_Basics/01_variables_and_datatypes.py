"""
Topic: Variables and Data Types
Learn how Python stores data in variables and the core built-in data types.
"""

# --- 1. Variables ---
# Python variables are created the moment you assign a value; no declaration needed.
name = "Alice"
age = 30
print("--- Variables ---")
print(f"Variable 'name': {name}")
print(f"Variable 'age': {age}")

# --- 2. Core Data Types ---
integer_value = 42                 # int: whole numbers
float_value = 3.14159              # float: decimal numbers
string_value = "Hello, Python!"    # str: text
boolean_value = True               # bool: True/False

print("\n--- Core Data Types ---")
print(f"integer_value = {integer_value}, type = {type(integer_value)}")
print(f"float_value = {float_value}, type = {type(float_value)}")
print(f"string_value = '{string_value}', type = {type(string_value)}")
print(f"boolean_value = {boolean_value}, type = {type(boolean_value)}")

# --- 3. Dynamic Typing ---
# A variable's type can change because Python infers the type from the assigned value.
dynamic_var = 10
print(f"\ndynamic_var starts as int: {dynamic_var} ({type(dynamic_var)})")
dynamic_var = "now I'm a string"
print(f"dynamic_var is now str: {dynamic_var} ({type(dynamic_var)})")

# --- 4. Type Casting ---
# Explicitly converting a value from one data type to another.
str_number = "100"
casted_int = int(str_number)        # str -> int
casted_float = float(casted_int)    # int -> float
casted_str = str(casted_float)      # float -> str
casted_bool = bool(casted_int)      # non-zero numbers are truthy

print("\n--- Type Casting ---")
print(f"'{str_number}' (str) -> {casted_int} (int)")
print(f"{casted_int} (int) -> {casted_float} (float)")
print(f"{casted_float} (float) -> '{casted_str}' (str)")
print(f"{casted_int} (int) -> {casted_bool} (bool)")

# Casting pitfall: non-numeric strings cannot be converted to int/float.
print("\n--- Casting Errors ---")
try:
    int("not a number")
except ValueError as error:
    print(f"Casting error example: {error}")

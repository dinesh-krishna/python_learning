"""
Topic: Function Basics
Define reusable blocks of code with parameters, return values, and default arguments.
"""


# --- 1. Defining and Calling a Function ---
def greet():
    """Print a simple, fixed greeting."""
    print("Hello from a function!")


print("--- Basic Function Call ---")
greet()


# --- 2. Parameters and Return Values ---
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


print("\n--- Parameters and Return Values ---")
result = add_numbers(5, 7)
print(f"add_numbers(5, 7) = {result}")


# --- 3. Default Arguments ---
# A default value is used automatically when the caller omits that argument.
def greet_person(name, greeting="Hello"):
    """Greet a person with an optional custom greeting."""
    return f"{greeting}, {name}!"


print("\n--- Default Arguments ---")
print(greet_person("Alice"))
print(greet_person("Bob", "Welcome"))


# --- 4. Keyword Arguments ---
# Arguments can be passed by name, in any order, which improves call-site clarity.
def describe_pet(name, animal_type="dog", age=1):
    """Describe a pet using named parameters."""
    return f"{name} is a {age}-year-old {animal_type}."


print("\n--- Keyword Arguments ---")
print(describe_pet("Rex", animal_type="dog", age=3))
print(describe_pet(age=2, name="Whiskers", animal_type="cat"))


# --- 5. Multiple Return Values ---
# Python returns multiple values as a tuple, which the caller can unpack.
def get_min_max(numbers):
    """Return both the minimum and maximum of a list."""
    return min(numbers), max(numbers)


print("\n--- Multiple Return Values ---")
smallest, largest = get_min_max([4, 9, 1, 7, 3])
print(f"Smallest: {smallest}, Largest: {largest}")

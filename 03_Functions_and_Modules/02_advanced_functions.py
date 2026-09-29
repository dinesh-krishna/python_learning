"""
Topic: Advanced Functions
Variable-length arguments, lambda functions, and Python's variable scope rules.
"""


# --- 1. *args: Variable Number of Positional Arguments ---
# Collects any extra positional arguments into a tuple named 'args'.
def sum_all(*args):
    """Return the sum of any number of positional arguments."""
    print(f"  args received as tuple: {args}")
    return sum(args)


print("--- *args ---")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")


# --- 2. **kwargs: Variable Number of Keyword Arguments ---
# Collects any extra keyword arguments into a dictionary named 'kwargs'.
def print_profile(**kwargs):
    """Print any number of named attributes."""
    print(f"  kwargs received as dict: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print("\n--- **kwargs ---")
print_profile(name="Alice", age=30, city="Paris")


# --- 3. Combining Regular Params, *args, and **kwargs ---
def build_order(item, *extras, **details):
    """Demonstrate combining a standard parameter with *args and **kwargs."""
    print(f"  Main item: {item}")
    print(f"  Extras: {extras}")
    print(f"  Details: {details}")


print("\n--- Combined Parameters ---")
build_order("Pizza", "extra cheese", "olives", size="large", delivery=True)

# --- 4. Lambda Functions ---
# Small, anonymous, single-expression functions, useful for short throwaway logic.
square = lambda x: x ** 2
add = lambda x, y: x + y
print("\n--- Lambda Functions ---")
print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")

# Lambdas are commonly used with sort keys, map(), and filter().
words = ["banana", "kiwi", "apple", "fig"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(f"Words sorted by length: {sorted_by_length}")

numbers = [1, 2, 3, 4, 5, 6]
doubled = list(map(lambda n: n * 2, numbers))
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Doubled: {doubled}")
print(f"Evens only: {evens}")

# --- 5. Scope and the LEGB Rule ---
# LEGB = Local -> Enclosing -> Global -> Built-in: the order Python searches for names.
global_variable = "I am global"


def outer_function():
    """Demonstrate the Enclosing scope for a nested function."""
    enclosing_variable = "I am enclosing"

    def inner_function():
        local_variable = "I am local"
        print(f"  Local: {local_variable}")
        print(f"  Enclosing: {enclosing_variable}")  # found in the enclosing scope
        print(f"  Global: {global_variable}")        # found in the global scope

    inner_function()


print("\n--- LEGB Scope Rule ---")
outer_function()

# The 'global' keyword lets a function modify a global variable instead of
# creating a new local variable that shadows it.
counter = 0


def increment_counter():
    """Modify the module-level 'counter' using the 'global' keyword."""
    global counter
    counter += 1


print("\n--- 'global' Keyword ---")
print(f"counter before: {counter}")
increment_counter()
increment_counter()
print(f"counter after two increments: {counter}")

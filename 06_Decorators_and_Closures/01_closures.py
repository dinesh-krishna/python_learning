"""
Topic: Closures
A closure is an inner function that remembers and can access variables from its
enclosing (outer) function's scope, even after the outer function has finished running.
"""


# --- 1. A Basic Closure ---
def make_multiplier(factor):
    """Return a function that multiplies its input by 'factor'."""

    def multiplier(number):
        # 'factor' is remembered from the enclosing scope, even after
        # make_multiplier() has already returned.
        return number * factor

    return multiplier


print("--- Basic Closure ---")
double = make_multiplier(2)
triple = make_multiplier(3)
print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# --- 2. Inspecting a Closure ---
# The __closure__ attribute reveals the captured (free) variables.
print("\n--- Inspecting a Closure ---")
print(f"double.__closure__: {double.__closure__}")
print(f"Captured value: {double.__closure__[0].cell_contents}")


# --- 3. Closures Retain State Between Calls ---
def make_counter():
    """Return a function that remembers a running count between calls."""
    count = 0

    def increment():
        nonlocal count  # required to modify the enclosing variable, not shadow it
        count += 1
        return count

    return increment


print("\n--- Closures Retain State ---")
counter_a = make_counter()
counter_b = make_counter()
print(f"counter_a(): {counter_a()}")
print(f"counter_a(): {counter_a()}")
print(f"counter_a(): {counter_a()}")
print(f"counter_b(): {counter_b()}")  # independent state from counter_a

# --- 4. Why Closures Matter: They Power Decorators ---
# The next file (02_decorators.py) builds directly on this closure pattern.
print("\n--- Preview: Closures Enable Decorators ---")


def logging_wrapper(func):
    """A closure that wraps another function to add behavior around it."""

    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__} with args={args}")
        return func(*args, **kwargs)

    return wrapper


wrapped_add = logging_wrapper(lambda x, y: x + y)
print(f"wrapped_add(2, 3) = {wrapped_add(2, 3)}")

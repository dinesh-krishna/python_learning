"""
Topic: Decorators with Arguments
Adding parameters to a decorator requires an extra layer of function nesting:
a decorator factory that returns the actual decorator.
"""

import functools


# --- 1. A Decorator Factory ---
# repeat(times) returns a decorator, which itself returns the wrapper function.
def repeat(times):
    """Return a decorator that calls the wrapped function 'times' times."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return decorator


@repeat(times=3)
def say_hello(name):
    """Return a greeting for 'name'."""
    return f"Hello, {name}!"


print("--- Decorator Factory: @repeat(times=3) ---")
print(say_hello("Alice"))


# --- 2. A Decorator with Validation Logic ---
def validate_positive(func):
    """Raise ValueError if any positional argument is not positive."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(isinstance(arg, (int, float)) and arg <= 0 for arg in args):
            raise ValueError("All numeric arguments must be positive.")
        return func(*args, **kwargs)

    return wrapper


@validate_positive
def calculate_area(width, height):
    """Return the area of a rectangle."""
    return width * height


print("\n--- Validation Decorator ---")
print(f"calculate_area(4, 5) = {calculate_area(4, 5)}")
try:
    calculate_area(-4, 5)
except ValueError as error:
    print(f"Validation caught an error: {error}")


# --- 3. Class-Based Decorators ---
# Any object with __call__ can act as a decorator; classes can track state via
# instance attributes instead of closures.
class CallCounter:
    """A class-based decorator that counts how many times a function is called."""

    def __init__(self, func):
        functools.update_wrapper(self, func)  # copies __name__, __doc__, etc.
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"  Call #{self.call_count} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CallCounter
def process_order(order_id):
    """Simulate processing an order."""
    return f"Processed order {order_id}"


print("\n--- Class-Based Decorator ---")
print(process_order(101))
print(process_order(102))
print(f"Total calls tracked: {process_order.call_count}")

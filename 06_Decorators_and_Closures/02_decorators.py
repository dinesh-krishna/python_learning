"""
Topic: Decorators
A decorator wraps a function to extend or modify its behavior without changing
its source code. Decorators are just syntactic sugar over closures.
"""

import functools
import time


# --- 1. A Decorator, Written the Manual Way ---
def announce(func):
    """Print a message before and after calling the wrapped function."""

    def wrapper(*args, **kwargs):
        print(f"  >> Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"  >> Finished {func.__name__}")
        return result

    return wrapper


def add(a, b):
    return a + b


print("--- Applying a Decorator Manually ---")
decorated_add = announce(add)
print(f"decorated_add(2, 3) = {decorated_add(2, 3)}")


# --- 2. The @decorator Syntax ---
# '@announce' above a function is shorthand for 'greet = announce(greet)'.
@announce
def greet(name):
    return f"Hello, {name}!"


print("\n--- Using @decorator Syntax ---")
print(greet("Alice"))


# --- 3. functools.wraps: Preserving Metadata ---
# Without @functools.wraps, the wrapped function's __name__/__doc__ get hidden
# behind the wrapper's own metadata.
def timer(func):
    """Measure and print how long the wrapped function takes to run."""

    @functools.wraps(func)  # copies __name__, __doc__, etc. from 'func' to 'wrapper'
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.6f} seconds")
        return result

    return wrapper


@timer
def slow_square(n):
    """Compute the square of n (with artificial busywork to make timing visible)."""
    _ = sum(i for i in range(100_000))
    return n ** 2


print("\n--- functools.wraps Preserves Metadata ---")
print(f"slow_square(4) = {slow_square(4)}")
print(f"Function name preserved: {slow_square.__name__}")
print(f"Docstring preserved: {slow_square.__doc__}")


# --- 4. Stacking Multiple Decorators ---
# Decorators apply bottom-up: @timer runs first (innermost), then @announce.
@announce
@timer
def compute(n):
    """Return n squared."""
    return n ** 2


print("\n--- Stacking Decorators ---")
print(f"compute(5) = {compute(5)}")

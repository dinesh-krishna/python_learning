"""
Topic: Context Managers
Context managers set up and reliably tear down resources using the 'with'
statement. This file shows the familiar built-in file example, then two ways
to build your own: a class with __enter__/__exit__, and @contextlib.contextmanager.
"""

import time
from contextlib import contextmanager

# --- 1. The Familiar Built-in Example ---
# open() returns a context manager: __exit__ closes the file even on error.
print("--- Built-in Context Manager: open() ---")
with open(__file__, "r", encoding="utf-8") as file:
    first_line = file.readline().strip()
print(f"First line of this script: {first_line}")
print(f"File closed automatically after the 'with' block: {file.closed}")


# --- 2. A Custom Context Manager Class ---
class Timer:
    """Context manager that measures how long the 'with' block takes to run."""

    def __enter__(self):
        """Called when entering the 'with' block; the return value is bound by 'as'."""
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Called when leaving the 'with' block, even if an exception occurred."""
        self.elapsed = time.perf_counter() - self.start
        print(f"  Block took {self.elapsed:.6f} seconds")
        return False  # False means: do not suppress any exception that occurred


print("\n--- Custom Context Manager Class ---")
with Timer():
    total = sum(i * i for i in range(100_000))
print(f"Sum result: {total}")


# --- 3. Handling Exceptions Inside a Context Manager ---
class SuppressError:
    """Context manager that swallows a specific exception type."""

    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Returning True tells Python the exception was handled - suppress it.
        return exc_type is not None and issubclass(exc_type, self.exception_type)


print("\n--- Suppressing Exceptions ---")
with SuppressError(ZeroDivisionError):
    print("  About to divide by zero...")
    result = 1 / 0
    print("  This line never runs.")
print("Execution continues normally after the 'with' block.")


# --- 4. @contextlib.contextmanager: A Simpler Way ---
# Turns a generator function into a context manager: code before 'yield' is
# __enter__, code after 'yield' (in a finally block) is __exit__.
@contextmanager
def managed_resource(name):
    """Simulate acquiring and releasing a named resource."""
    print(f"  Acquiring resource: {name}")
    try:
        yield f"resource:{name}"
    finally:
        print(f"  Releasing resource: {name}")


print("\n--- @contextmanager Decorator ---")
with managed_resource("database-connection") as resource:
    print(f"  Using {resource}")

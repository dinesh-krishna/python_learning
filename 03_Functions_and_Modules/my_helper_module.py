"""
A small custom module demonstrating reusable functions and constants.
Import this file from another script in the same folder to reuse its functions.
"""

PROJECT_NAME = "Python Learning Curriculum"


def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Welcome to {PROJECT_NAME}."


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


# This block only runs when my_helper_module.py is executed directly,
# not when it is imported - demonstrating that modules can be self-tested.
if __name__ == "__main__":
    print("my_helper_module.py ran directly - self-test:")
    print(greet("Tester"))
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(2, 3) = {multiply(2, 3)}")

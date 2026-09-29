"""
Topic: Modules and Packages
Organize and reuse code by importing built-in modules and your own custom modules.

Note: run this script from within its own folder (or via an IDE "Run" button)
so the 'import my_helper_module' statement below can find its sibling file.
"""

# --- 1. Importing a Built-in Module (whole module) ---
import math

print("--- Built-in Module: math ---")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.factorial(5) = {math.factorial(5)}")

# --- 2. Importing Specific Names from a Module ---
from random import randint, choice

print("\n--- Built-in Module: random (specific imports) ---")
print(f"randint(1, 10) = {randint(1, 10)}")
print(f"choice(['a', 'b', 'c']) = {choice(['a', 'b', 'c'])}")

# --- 3. Importing a Module with an Alias ---
import datetime as dt

print("\n--- Built-in Module: datetime (aliased) ---")
today = dt.date.today()
print(f"Today's date: {today}")

# --- 4. Importing a Custom Local Module ---
# 'my_helper_module.py' lives in this same folder and defines helper functions.
import my_helper_module

print("\n--- Custom Module: my_helper_module ---")
print(my_helper_module.greet("Alice"))
print(f"add(4, 6) = {my_helper_module.add(4, 6)}")
print(f"PROJECT_NAME constant = {my_helper_module.PROJECT_NAME}")

# --- 5. Importing Specific Names from a Custom Module ---
from my_helper_module import multiply

print("\n--- Custom Module (specific import) ---")
print(f"multiply(3, 7) = {multiply(3, 7)}")

# --- 6. The __name__ == "__main__" Idiom ---
# Code inside this guard only runs when the file is executed directly,
# not when it is imported as a module elsewhere.
print(f"\nThis script's __name__ is: {__name__}")
if __name__ == "__main__":
    print("Running as the main program (not imported).")

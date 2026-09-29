"""
Topic: Loops
Repeat actions using for and while loops, and control them with break/continue.
"""

# --- 1. For Loop over a range() ---
print("--- For Loop with range() ---")
for number in range(1, 6):
    print(f"Count: {number}")

# --- 2. For Loop over a Collection ---
fruits = ["apple", "banana", "cherry"]
print("\n--- For Loop over a List ---")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# --- 3. While Loop ---
print("\n--- While Loop ---")
countdown = 3
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Liftoff!")

# --- 4. break: Exit the Loop Early ---
print("\n--- break ---")
for number in range(10):
    if number == 4:
        print("Breaking at 4")
        break
    print(f"Number: {number}")

# --- 5. continue: Skip to the Next Iteration ---
print("\n--- continue ---")
for number in range(6):
    if number % 2 == 0:
        continue  # skip even numbers, move to the next iteration
    print(f"Odd number: {number}")

# --- 6. else with Loops ---
# The 'else' block runs only if the loop finishes WITHOUT hitting 'break'.
print("\n--- for-else (target found) ---")
target = 10
for number in range(2, 5):
    if number == target:
        print(f"Found {target}!")
        break
else:
    print(f"Loop finished without finding {target} (else block executed).")

print("\n--- for-else (target not found) ---")
target = 3
for number in range(2, 5):
    if number == target:
        print(f"Found {target}!")
        break
else:
    print(f"Loop finished without finding {target} (else block executed).")

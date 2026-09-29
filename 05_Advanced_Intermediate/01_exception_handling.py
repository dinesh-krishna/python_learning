"""
Topic: Exception Handling
Gracefully handle errors using try/except/else/finally, and define custom exceptions.
"""

# --- 1. Basic try/except ---
print("--- Basic try/except ---")
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Caught an error: {error}")

# --- 2. Catching Multiple Exception Types ---
print("\n--- Multiple Exception Types ---")
for value in ["10", "abc", "0"]:
    try:
        print(f"100 / int('{value}') = {100 / int(value)}")
    except ValueError:
        print(f"'{value}' is not a valid number.")
    except ZeroDivisionError:
        print(f"Cannot divide by zero (value was '{value}').")

# --- 3. else: Runs ONLY if No Exception Occurred ---
print("\n--- try/except/else ---")
try:
    number = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion succeeded, no exception raised: {number}")

# --- 4. finally: Always Runs, Regardless of an Exception ---
print("\n--- try/except/finally ---")
try:
    file_contents = "simulated file data"
    print(f"Processing: {file_contents}")
    raise RuntimeError("Something went wrong during processing!")
except RuntimeError as error:
    print(f"Handled error: {error}")
finally:
    print("Cleanup step: this always runs (e.g., closing a file/connection).")


# --- 5. Custom Exceptions ---
# Define your own exception types by subclassing Exception for domain-specific errors.
class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the available account balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}: balance is only {balance}.")


def withdraw(balance, amount):
    """Withdraw money from an account, raising a custom exception if funds are low."""
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


print("\n--- Custom Exceptions ---")
try:
    new_balance = withdraw(balance=100, amount=250)
except InsufficientFundsError as error:
    print(f"Custom exception caught: {error}")
else:
    print(f"Withdrawal successful. New balance: {new_balance}")

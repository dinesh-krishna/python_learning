"""
Topic: Unit Testing with unittest
The unittest module (built into Python) lets you write automated tests that
verify your code behaves as expected, and quickly flag regressions.
"""

import unittest


# --- 1. The Code Under Test ---
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def divide(a, b):
    """Return a divided by b; raises ValueError instead of ZeroDivisionError."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


class BankAccount:
    """A minimal bank account used to demonstrate setUp/tearDown."""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


# --- 2. A Test Case Class ---
# Each method starting with 'test_' is discovered and run automatically.
class TestMathFunctions(unittest.TestCase):
    """Tests for the simple add() and divide() functions above."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_divide_normal_case(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        # assertRaises verifies that the expected exception type is raised.
        with self.assertRaises(ValueError):
            divide(10, 0)


# --- 3. setUp/tearDown: Shared Fixtures for Each Test ---
class TestBankAccount(unittest.TestCase):
    """Tests for BankAccount; setUp() runs before EVERY test method."""

    def setUp(self):
        """Create a fresh account before each test, so tests don't affect each other."""
        self.account = BankAccount(balance=100)

    def test_deposit_increases_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def test_deposit_negative_amount_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)


# --- 4. Running the Tests ---
# 'exit=False' lets this keep running as a plain script instead of calling sys.exit().
# Normally you'd run tests via: python -m unittest 01_unittest_basics.py
print("--- Running unittest Test Suite ---")
if __name__ == "__main__":
    unittest.main(argv=[""], exit=False, verbosity=2)

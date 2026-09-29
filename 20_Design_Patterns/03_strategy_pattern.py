"""
Topic: Strategy Pattern
Lets you swap out an algorithm's implementation at runtime by encapsulating
each variant behind a common interface, instead of using long if/elif chains.
"""

from abc import ABC, abstractmethod


# --- 1. The Strategy Interface ---
class DiscountStrategy(ABC):
    """Common interface for every pricing strategy."""

    @abstractmethod
    def apply(self, price):
        raise NotImplementedError


# --- 2. Concrete Strategies ---
class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)


# --- 3. The Context: Uses Whatever Strategy It's Given ---
class ShoppingCart:
    """Delegates the discount calculation to whichever strategy it's configured with."""

    def __init__(self, discount_strategy):
        self.discount_strategy = discount_strategy
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        subtotal = sum(price for _, price in self.items)
        return self.discount_strategy.apply(subtotal)


print("--- Strategy Pattern ---")
cart = ShoppingCart(discount_strategy=NoDiscount())
cart.add_item("Keyboard", 50)
cart.add_item("Mouse", 25)
print(f"No discount: total = ${cart.total():.2f}")

# --- 4. Swapping Strategies at Runtime ---
print("\n--- Swapping the Strategy at Runtime ---")
cart.discount_strategy = PercentageDiscount(percent=10)
print(f"10% off: total = ${cart.total():.2f}")

cart.discount_strategy = FlatDiscount(amount=15)
print(f"$15 flat off: total = ${cart.total():.2f}")


# --- 5. Strategies Can Also Be Plain Functions (a Lighter-Weight Approach) ---
print("\n--- Function-Based Strategies (Pythonic Shortcut) ---")


def no_discount(price):
    return price


def percentage_discount(percent):
    """Return a discount function with 'percent' pre-configured (a closure)."""
    return lambda price: price * (1 - percent / 100)


strategies = {"none": no_discount, "vip": percentage_discount(20)}
subtotal = 100
for name, strategy in strategies.items():
    print(f"  Strategy '{name}': ${strategy(subtotal):.2f}")

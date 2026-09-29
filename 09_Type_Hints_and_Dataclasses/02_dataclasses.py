"""
Topic: Dataclasses
@dataclass automatically generates __init__, __repr__, and __eq__ for classes
that primarily exist to hold data, eliminating boilerplate code.
"""

from dataclasses import dataclass, field, asdict


# --- 1. A Basic Dataclass ---
@dataclass
class Point:
    """A 2D point - notice there's no __init__ or __repr__ written by hand."""

    x: int
    y: int


print("--- Basic Dataclass ---")
p1 = Point(3, 4)
p2 = Point(3, 4)
print(f"p1 = {p1}")                    # __repr__ generated automatically
print(f"p1 == p2 (auto __eq__): {p1 == p2}")


# --- 2. Default Values ---
@dataclass
class Product:
    """A product with some fields defaulted."""

    name: str
    price: float
    in_stock: bool = True
    tags: list[str] = field(default_factory=list)  # mutable defaults need field()


print("\n--- Default Values ---")
product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 19.99, in_stock=False, tags=["accessory", "wireless"])
print(f"product1 = {product1}")
print(f"product2 = {product2}")


# --- 3. Immutable Dataclasses (frozen=True) ---
@dataclass(frozen=True)
class ImmutablePoint:
    """frozen=True makes instances read-only after creation, like a tuple."""

    x: int
    y: int


print("\n--- Frozen (Immutable) Dataclass ---")
frozen_point = ImmutablePoint(1, 2)
print(f"frozen_point = {frozen_point}")
try:
    frozen_point.x = 99
except AttributeError as error:
    print(f"Cannot modify a frozen dataclass: {error}")


# --- 4. Methods on Dataclasses ---
# Dataclasses can still define regular methods alongside their auto-generated ones.
@dataclass
class Rectangle:
    """A rectangle with a computed method in addition to its data fields."""

    width: float
    height: float

    def area(self) -> float:
        """Return the rectangle's area."""
        return self.width * self.height


print("\n--- Dataclass with Methods ---")
rect = Rectangle(4, 5)
print(f"rect = {rect}, area = {rect.area()}")

# --- 5. Converting a Dataclass to a Dictionary ---
print("\n--- asdict() ---")
print(f"asdict(product2) = {asdict(product2)}")

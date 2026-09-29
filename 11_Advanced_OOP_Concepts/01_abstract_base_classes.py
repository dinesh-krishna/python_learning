"""
Topic: Abstract Base Classes (ABCs)
ABCs define a required interface: subclasses MUST implement certain methods,
or Python refuses to let you instantiate them. This enforces a contract
across related classes.
"""

from abc import ABC, abstractmethod


# --- 1. Defining an Abstract Base Class ---
class Shape(ABC):
    """Abstract base class: cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Subclasses MUST implement this method."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Subclasses MUST implement this method."""
        raise NotImplementedError

    def describe(self):
        """A regular (non-abstract) method - shared by all subclasses as-is."""
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


# --- 2. Attempting to Instantiate the Abstract Class Directly Fails ---
print("--- Abstract Classes Cannot Be Instantiated ---")
try:
    shape = Shape()
except TypeError as error:
    print(f"Error: {error}")


# --- 3. Concrete Subclasses Must Implement All Abstract Methods ---
class Circle(Shape):
    """Concrete subclass implementing both abstract methods."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """Another concrete subclass implementing both abstract methods."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


print("\n--- Concrete Subclasses Work Normally ---")
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.describe())

# --- 4. A Subclass Missing a Required Method Also Fails ---
print("\n--- Incomplete Subclasses Also Fail ---")


class Triangle(Shape):
    """Intentionally incomplete: forgot to implement perimeter()."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


try:
    incomplete_triangle = Triangle(3, 4)
except TypeError as error:
    print(f"Error: {error}")

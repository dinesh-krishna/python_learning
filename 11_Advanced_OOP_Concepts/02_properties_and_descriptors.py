"""
Topic: Properties and Descriptors
@property lets you run code on attribute access/assignment while keeping a
simple attribute-like syntax. Descriptors generalize this pattern so the same
logic can be reused across multiple classes/attributes.
"""


# --- 1. @property: Computed, Read-Only Attributes ---
class Circle:
    """A circle where 'area' is computed on the fly, not stored directly."""

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """Accessed like an attribute (circle.area), not called like a method."""
        return 3.14159 * self.radius ** 2


print("--- @property: Computed Attribute ---")
circle = Circle(5)
print(f"circle.radius = {circle.radius}")
print(f"circle.area = {circle.area}")  # no parentheses needed


# --- 2. @property with a Setter: Validation on Assignment ---
class Temperature:
    """Stores temperature in Celsius but validates and exposes it via a property."""

    def __init__(self, celsius):
        self._celsius = celsius  # convention: leading underscore = "internal" value

    @property
    def celsius(self):
        """Getter: runs whenever code reads temperature.celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter: runs whenever code assigns temperature.celsius = value."""
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        """A second, fully computed read-only property derived from celsius."""
        return (self._celsius * 9 / 5) + 32


print("\n--- @property with Validation ---")
temp = Temperature(25)
print(f"temp.celsius = {temp.celsius}")
print(f"temp.fahrenheit = {temp.fahrenheit}")
temp.celsius = 30  # goes through the setter, which validates the new value
print(f"After setting celsius = 30: fahrenheit = {temp.fahrenheit}")
try:
    temp.celsius = -300
except ValueError as error:
    print(f"Validation caught an error: {error}")


# --- 3. Descriptors: Reusable Property-Like Behavior ---
# A descriptor is any class implementing __get__/__set__; assigning an instance
# of it as a class attribute lets it manage that attribute for every instance.
class PositiveNumber:
    """A descriptor that enforces a positive value for whichever attribute uses it."""

    def __set_name__(self, owner, name):
        # Automatically called with the attribute's name, e.g. "width" or "height".
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.private_name[1:]} must be positive, got {value}.")
        setattr(instance, self.private_name, value)


class Rectangle:
    """Both 'width' and 'height' reuse the SAME PositiveNumber descriptor logic."""

    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width    # goes through PositiveNumber.__set__
        self.height = height  # goes through PositiveNumber.__set__

    def area(self):
        return self.width * self.height


print("\n--- Descriptors: Reusable Validation Across Attributes ---")
rect = Rectangle(4, 5)
print(f"rect.area() = {rect.area()}")
try:
    rect.width = -10
except ValueError as error:
    print(f"Descriptor caught an error: {error}")

"""
Topic: __slots__ and Memory Optimization
By default, every instance carries a __dict__ for arbitrary attributes. For
classes with millions of instances or fixed, known attributes, __slots__
trades that flexibility for a real reduction in per-instance memory use.
"""

import sys


# --- 1. A Regular Class: Has a __dict__ per Instance ---
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# --- 2. A __slots__ Class: No Per-Instance __dict__ ---
class SlottedPoint:
    __slots__ = ("x", "y")  # only these attribute names are allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y


print("--- Memory Comparison ---")
regular_point = RegularPoint(1, 2)
slotted_point = SlottedPoint(1, 2)

# getsizeof() only measures the object itself, not objects it references - so
# for a fair comparison, the regular instance's __dict__ size must be added.
regular_size = sys.getsizeof(regular_point) + sys.getsizeof(regular_point.__dict__)
slotted_size = sys.getsizeof(slotted_point)
print(f"RegularPoint: instance + __dict__ = {regular_size} bytes")
print(f"SlottedPoint: instance only (no __dict__) = {slotted_size} bytes")
print(f"RegularPoint has __dict__: {hasattr(regular_point, '__dict__')}")
print(f"SlottedPoint has __dict__: {hasattr(slotted_point, '__dict__')}")

# --- 3. __slots__ Prevents Adding New Attributes ---
print("\n--- __slots__ Restricts Attributes ---")
regular_point.z = 99  # works fine - __dict__ accepts any new attribute
print(f"regular_point.z = {regular_point.z}")

try:
    slotted_point.z = 99
except AttributeError as error:
    print(f"Cannot add an undeclared attribute: {error}")

# --- 4. When to Use __slots__ ---
print("\n--- When __slots__ Makes Sense ---")
print("  - Classes instantiated MANY times (thousands to millions), e.g. graph nodes")
print("  - Classes with a small, fixed, well-known set of attributes")
print("  - NOT when you need dynamic attributes, multiple inheritance with slots,")
print("    or class-level default mutable attributes")

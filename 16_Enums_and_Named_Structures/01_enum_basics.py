"""
Topic: Enum
Enums give a fixed set of named constants a proper type, replacing "magic"
strings/numbers (like status == 1) with self-documenting, type-safe values.
"""

from enum import Enum, IntEnum, auto


# --- 1. A Basic Enum ---
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("--- Basic Enum ---")
print(f"Color.RED = {Color.RED}")
print(f"Color.RED.name = {Color.RED.name}")
print(f"Color.RED.value = {Color.RED.value}")
print(f"Color.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED == 1: {Color.RED == 1}")  # False - plain Enum isn't interchangeable with int

# --- 2. Iterating Over an Enum ---
print("\n--- Iterating an Enum ---")
for color in Color:
    print(f"  {color.name} = {color.value}")

# --- 3. auto(): Let Python Assign Values ---
print("\n--- auto() ---")


class Status(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()


for status in Status:
    print(f"  {status.name} = {status.value}")

# --- 4. IntEnum: Enum Members That ARE Integers ---
# Unlike plain Enum, IntEnum members compare equal to and behave like plain ints.
print("\n--- IntEnum ---")


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


print(f"Priority.HIGH == 3: {Priority.HIGH == 3}")
print(f"Priority.HIGH > Priority.LOW: {Priority.HIGH > Priority.LOW}")
print(f"sorted list of priorities: {sorted([Priority.HIGH, Priority.LOW, Priority.MEDIUM])}")

# --- 5. Enums Replace Error-Prone "Magic Values" ---
print("\n--- Why Enums Matter ---")


def handle_status(status):
    """Using an Enum parameter makes invalid values impossible to pass by mistake."""
    if status is Status.COMPLETED:
        return "Task finished!"
    if status is Status.FAILED:
        return "Task failed - check logs."
    return "Task still in progress."


print(handle_status(Status.COMPLETED))
print(handle_status(Status.PENDING))

# Looking up a member by value or by name:
print(f"\nStatus(1) -> {Status(1)}")              # lookup by value
print(f"Status['FAILED'] -> {Status['FAILED']}")  # lookup by name

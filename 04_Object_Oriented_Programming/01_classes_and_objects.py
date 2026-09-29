"""
Topic: Classes and Objects
Classes are blueprints for creating objects that bundle data (attributes)
and behavior (methods) together.
"""


class Dog:
    """A simple class representing a dog."""

    # Class attribute: shared by ALL instances of this class.
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        """Initialize a new Dog instance with its own data (instance attributes)."""
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Instance method: behavior that depends on this specific dog."""
        return f"{self.name} says Woof!"

    def describe(self):
        """Instance method: build a human-readable description."""
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    def have_birthday(self):
        """Instance method that modifies the object's own state."""
        self.age += 1
        return f"{self.name} is now {self.age} years old."


print("--- Creating Objects (Instances) ---")
dog1 = Dog("Rex", "German Shepherd", 3)
dog2 = Dog("Bella", "Labrador", 5)

print(dog1.describe())
print(dog2.describe())

print("\n--- Calling Instance Methods ---")
print(dog1.bark())
print(dog2.bark())

print("\n--- Accessing Attributes ---")
print(f"dog1.name = {dog1.name}")
print(f"dog2.breed = {dog2.breed}")
print(f"Class attribute (species) shared by both: {dog1.species}, {dog2.species}")

print("\n--- Modifying State via a Method ---")
print(dog1.have_birthday())

print("\n--- Every Dog Instance Is Independent ---")
dog1.name = "Max"
print(f"dog1.name changed to: {dog1.name}")
print(f"dog2.name is unaffected: {dog2.name}")

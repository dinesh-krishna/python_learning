"""
Topic: The Four Pillars of OOP
Inheritance, polymorphism, encapsulation, and method overriding.
"""


# --- 1. Base Class (Parent) ---
class Animal:
    """A generic animal used as a base class for inheritance."""

    def __init__(self, name):
        self.name = name
        self._sound = "..."           # protected attribute (convention: single underscore)
        self.__secret_id = id(self)   # private attribute (name-mangled: double underscore)

    def make_sound(self):
        """Default behavior; subclasses are expected to override this."""
        return f"{self.name} makes a sound: {self._sound}"

    def get_secret_id(self):
        """Encapsulation: expose private data only through a controlled method."""
        return self.__secret_id


# --- 2. Inheritance: Dog and Cat reuse Animal's __init__ and attributes ---
class Dog(Animal):
    """Dog inherits from Animal and overrides make_sound()."""

    def __init__(self, name):
        super().__init__(name)  # reuse the parent's initialization logic
        self._sound = "Woof"

    def make_sound(self):
        """Method overriding: replaces the parent's generic implementation."""
        return f"{self.name} barks: {self._sound}!"


class Cat(Animal):
    """Cat inherits from Animal and overrides make_sound()."""

    def __init__(self, name):
        super().__init__(name)
        self._sound = "Meow"

    def make_sound(self):
        """Method overriding: replaces the parent's generic implementation."""
        return f"{self.name} meows: {self._sound}!"


print("--- Inheritance ---")
generic_animal = Animal("Creature")
dog = Dog("Rex")
cat = Cat("Whiskers")
print(generic_animal.make_sound())
print(dog.make_sound())
print(cat.make_sound())

# --- 3. Polymorphism ---
# The same method call (make_sound) behaves differently depending on the object's type.
print("\n--- Polymorphism ---")
animals = [generic_animal, dog, cat]
for animal in animals:
    print(animal.make_sound())

# --- 4. Encapsulation ---
# Internal details are hidden; access is controlled through public methods.
print("\n--- Encapsulation ---")
print(f"Dog's secret id (via public method): {dog.get_secret_id()}")
try:
    print(dog.__secret_id)  # fails: the attribute is name-mangled, not directly accessible
except AttributeError as error:
    print(f"Direct access fails as expected: {error}")

# The real attribute name is mangled to _ClassName__attribute.
print(f"Accessible via mangled name (not recommended): {dog._Animal__secret_id}")

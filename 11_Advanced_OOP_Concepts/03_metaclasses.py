"""
Topic: Metaclasses
A metaclass is "the class of a class": it controls how classes themselves are
created, just as a class controls how instances are created. Metaclasses are
an advanced tool, most often seen in frameworks (e.g., ORMs) rather than
everyday application code.
"""


# --- 1. Everything Is an Object, Including Classes ---
# By default, every class's type is 'type' - the built-in metaclass.
class Dog:
    pass


print("--- Classes Are Objects Too ---")
print(f"type(Dog) = {type(Dog)}")
print(f"type(type) = {type(type)}")


# --- 2. Creating a Class Dynamically with type() ---
# type(name, bases, namespace) is the same mechanism the 'class' keyword uses.
def bark(self):
    return f"{self.name} says Woof!"


def init_dog(self, name):
    self.name = name


DynamicDog = type("DynamicDog", (), {"bark": bark, "__init__": init_dog})

print("\n--- Creating a Class with type() Directly ---")
dynamic_dog = DynamicDog("Rex")
print(dynamic_dog.bark())


# --- 3. A Custom Metaclass ---
# Subclassing 'type' lets you hook into class creation itself.
class UpperCaseAttributeMeta(type):
    """A metaclass that uppercases every plain string class attribute."""

    def __new__(mcs, name, bases, namespace):
        updated_namespace = {}
        for key, value in namespace.items():
            # Skip dunder attributes (like __module__) - only touch user-defined ones.
            if isinstance(value, str) and not key.startswith("__"):
                updated_namespace[key] = value.upper()
            else:
                updated_namespace[key] = value
        return super().__new__(mcs, name, bases, updated_namespace)


class Config(metaclass=UpperCaseAttributeMeta):
    """Every plain string attribute here gets uppercased automatically."""

    environment = "production"
    region = "us-east-1"


print("\n--- Custom Metaclass Transforms Class Attributes ---")
print(f"Config.environment = {Config.environment}")
print(f"Config.region = {Config.region}")


# --- 4. Why Metaclasses Matter: Enforcing Rules Across Many Classes ---
class SingletonMeta(type):
    """A metaclass that makes every class using it a singleton (one instance only)."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """No matter how many times this is 'created', it's really the same instance."""

    def __init__(self):
        print("  (Creating a new DatabaseConnection instance...)")


print("\n--- Singleton Pattern via Metaclass ---")
connection1 = DatabaseConnection()
connection2 = DatabaseConnection()
print(f"connection1 is connection2: {connection1 is connection2}")

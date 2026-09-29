"""
Topic: Magic (Dunder) Methods
Special methods let your custom objects work with built-in functions and operators
such as print(), len(), ==, and +.
"""


class Book:
    """A class demonstrating common magic methods."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Called by print()/str() - should be a readable, user-friendly string."""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """Called by repr()/the interactive console - should be unambiguous,
        ideally text that could recreate the object."""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __len__(self):
        """Called by len() - lets len(book) return something meaningful."""
        return self.pages

    def __eq__(self, other):
        """Called by == - defines what equality means for two Book objects."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __add__(self, other):
        """Called by + - here, combine two books' page counts as an example."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages


print("--- __str__ and __repr__ ---")
book1 = Book("Dune", "Frank Herbert", 412)
book2 = Book("Dune", "Frank Herbert", 412)
book3 = Book("1984", "George Orwell", 328)

print(f"print(book1) uses __str__: {book1}")
print(f"repr(book1) uses __repr__: {repr(book1)}")

print("\n--- __len__ ---")
print(f"len(book1) = {len(book1)}")

print("\n--- __eq__ ---")
print(f"book1 == book2 (same title/author): {book1 == book2}")
print(f"book1 == book3 (different book): {book1 == book3}")

print("\n--- __add__ ---")
total_pages = book1 + book3
print(f"book1 + book3 (combined pages): {total_pages}")

print("\n--- Objects in a List Use __repr__ ---")
library = [book1, book3]
print(f"library list: {library}")

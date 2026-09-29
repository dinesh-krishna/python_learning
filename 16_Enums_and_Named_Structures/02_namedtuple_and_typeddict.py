"""
Topic: typing.NamedTuple and TypedDict
Both add structure and type-checking on top of tuples and dicts - useful
middle ground between a plain dataclass and a raw tuple/dict.
"""

from typing import NamedTuple, TypedDict


# --- 1. typing.NamedTuple: A Typed, Class-Based Alternative to collections.namedtuple ---
class Point(NamedTuple):
    """Looks like a class, but instances behave exactly like immutable tuples."""

    x: int
    y: int

    def distance_from_origin(self):
        """NamedTuple classes can still define regular methods."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


print("--- typing.NamedTuple ---")
p1 = Point(3, 4)
print(f"p1 = {p1}")
print(f"p1.x = {p1.x}, p1.y = {p1.y}")
print(f"p1.distance_from_origin() = {p1.distance_from_origin()}")
print(f"Still a tuple: isinstance(p1, tuple) = {isinstance(p1, tuple)}")

try:
    p1.x = 10
except AttributeError as error:
    print(f"Immutable, like collections.namedtuple: {error}")

# --- 2. TypedDict: Type-Checked Dictionary Shapes ---
# A TypedDict is STILL a plain dict at runtime - the extra type safety is
# only enforced by static checkers like mypy/Pylance, not by Python itself.
print("\n--- TypedDict ---")


class Movie(TypedDict):
    title: str
    year: int
    rating: float


movie: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
print(f"movie = {movie}")
print(f"type(movie) = {type(movie)}")  # plain dict at runtime
print(f"movie['title'] = {movie['title']}")


# --- 3. TypedDict with Optional Fields ---
class MovieNotes(TypedDict, total=False):
    """total=False makes every field in THIS class optional (instead of required)."""

    notes: str


class FullMovie(Movie, MovieNotes):
    """Combine the required fields from Movie with the optional 'notes' field."""


print("\n--- TypedDict with Optional Fields ---")
movie_with_notes: FullMovie = {
    "title": "Interstellar",
    "year": 2014,
    "rating": 8.6,
    "notes": "Bring tissues.",
}
movie_without_notes: FullMovie = {"title": "Tenet", "year": 2020, "rating": 7.8}
print(f"movie_with_notes = {movie_with_notes}")
print(f"movie_without_notes = {movie_without_notes}")

# --- 4. When to Choose What ---
print("\n--- Choosing Between namedtuple, NamedTuple, dataclass, and TypedDict ---")
print("  collections.namedtuple -> lightweight, no type hints needed")
print("  typing.NamedTuple      -> like namedtuple, but with type-checked fields")
print("  @dataclass             -> mutable by default, supports methods/defaults")
print("  TypedDict              -> when the data is naturally a dict (e.g., JSON)")

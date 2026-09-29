"""
Topic: sqlite3 - Working with a Relational Database
sqlite3 is in Python's standard library and provides a full relational
database stored in a single file - no server or extra installation needed.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "employees.db"

# --- 1. Connecting and Creating a Table ---
print("--- Connecting and Creating a Table ---")
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# DROP first so re-running this script starts from a clean, predictable state.
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute(
    """
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """
)
print(f"Database ready at {DB_FILE}")

# --- 2. Inserting Data (Always Use Parameterized Queries!) ---
# Using "?" placeholders prevents SQL injection - never build a query with an
# f-string/% from untrusted input.
print("\n--- Inserting Rows ---")
employees = [
    ("Alice", "Engineering", 95000),
    ("Bob", "Sales", 68000),
    ("Charlie", "Engineering", 105000),
]
cursor.executemany(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", employees
)
connection.commit()  # writes changes to disk - required after INSERT/UPDATE/DELETE
print(f"Inserted {len(employees)} rows")

# --- 3. Querying Data ---
print("\n--- Querying All Rows ---")
cursor.execute("SELECT id, name, department, salary FROM employees")
for row in cursor.fetchall():
    print(f"  {row}")

print("\n--- Querying with a Parameterized WHERE Clause ---")
cursor.execute(
    "SELECT name, salary FROM employees WHERE department = ?", ("Engineering",)
)
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,.2f}")

# --- 4. Updating and Deleting Data ---
print("\n--- Updating a Row ---")
cursor.execute("UPDATE employees SET salary = salary * 1.1 WHERE name = ?", ("Bob",))
connection.commit()
cursor.execute("SELECT name, salary FROM employees WHERE name = ?", ("Bob",))
print(f"  After raise: {cursor.fetchone()}")

print("\n--- Deleting a Row ---")
cursor.execute("DELETE FROM employees WHERE name = ?", ("Charlie",))
connection.commit()
cursor.execute("SELECT COUNT(*) FROM employees")
print(f"  Remaining employee count: {cursor.fetchone()[0]}")

# --- 5. Closing the Connection ---
# Closing releases the file lock; unlike 'with open(...)', 'with sqlite3.connect()'
# auto-commits/rolls back but does NOT auto-close the connection.
connection.close()
print("\nConnection closed.")

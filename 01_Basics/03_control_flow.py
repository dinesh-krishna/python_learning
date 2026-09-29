"""
Topic: Control Flow
Direct program execution using if-elif-else and the match-case statement.
"""

# --- 1. if-elif-else ---
temperature = 28
print("--- if-elif-else ---")
if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's cold outside.")

# --- 2. Nested Conditions ---
age = 20
has_id = True
print("\n--- Nested Conditions ---")
if age >= 18:
    if has_id:
        print("Entry allowed: adult with valid ID.")
    else:
        print("Entry denied: no ID provided.")
else:
    print("Entry denied: underage.")

# --- 3. Conditional (Ternary) Expression ---
# A compact one-line if-else for simple value assignment.
status = "adult" if age >= 18 else "minor"
print(f"\nTernary expression result: {status}")

# --- 4. match-case (structural pattern matching, Python 3.10+) ---
# A cleaner alternative to long if-elif chains when matching discrete values/patterns.
def describe_status_code(code):
    """Map an HTTP status code to a short human-readable description."""
    match code:
        case 200:
            return "OK"
        case 301 | 302:  # the "|" matches multiple literal values
            return "Redirect"
        case 404:
            return "Not Found"
        case code if code >= 500:  # guard clause: extra condition on the match
            return "Server Error"
        case _:  # wildcard: matches anything not covered above
            return "Unknown status code"


print("\n--- match-case ---")
for status_code in [200, 301, 404, 503, 999]:
    print(f"Status {status_code}: {describe_status_code(status_code)}")

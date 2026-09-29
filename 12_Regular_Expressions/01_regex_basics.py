"""
Topic: Regular Expressions (re module)
Regular expressions describe text patterns for searching, matching, and
replacing substrings, far more powerfully than plain string methods.
"""

import re

# --- 1. Basic Matching: search() vs. match() ---
text = "The rain in Spain falls mainly on the plain."

print("--- search() vs. match() ---")
print(f"re.search('rain', text): {re.search('rain', text)}")  # finds anywhere in the string
print(f"re.match('rain', text): {re.match('rain', text)}")    # None: 'rain' isn't at the START
print(f"re.match('The', text): {re.match('The', text)}")      # matches: text starts with 'The'

# --- 2. Common Patterns ---
print("\n--- Common Patterns ---")
digits_pattern = r"\d+"
words_pattern = r"\w+"
whitespace_pattern = r"\s+"
print(f"Pattern {digits_pattern!r} in 'Order #12345': {re.findall(digits_pattern, 'Order #12345')}")
print(f"Pattern {words_pattern!r} in 'hello_world 123': {re.findall(words_pattern, 'hello_world 123')}")
print(f"Pattern {whitespace_pattern!r} splits 'a   b  c': {re.split(whitespace_pattern, 'a   b  c')}")

# --- 3. findall(): Every Non-Overlapping Match ---
print("\n--- findall() ---")
words_with_ain = re.findall(r"\b\w*ain\w*\b", text)
print(f"Words containing 'ain': {words_with_ain}")

# --- 4. Groups: Capturing Parts of a Match ---
print("\n--- Capture Groups ---")
log_line = "2026-09-29 14:32:10 ERROR Failed to connect"
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
match = re.match(pattern, log_line)
if match:
    log_date, log_time, level, message = match.groups()
    print(f"Date: {log_date}, Time: {log_time}, Level: {level}, Message: {message}")

# Named groups make the intent clearer than positional indexing.
named_pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)"
named_match = re.match(named_pattern, log_line)
if named_match:
    print(f"Named group 'level': {named_match.group('level')}")
    print(f"As a dict: {named_match.groupdict()}")

# --- 5. sub(): Search and Replace ---
print("\n--- re.sub() ---")
masked = re.sub(r"\d", "*", "Card number: 4111 2222 3333 4444")
print(f"Masked digits: {masked}")


# sub() also accepts a function for computed replacements.
def double_number(match_obj):
    """Return the matched number doubled, as a string."""
    return str(int(match_obj.group()) * 2)


doubled = re.sub(r"\d+", double_number, "Values: 3, 7, 10")
print(f"Doubled numbers: {doubled}")

# --- 6. Compiling Patterns for Reuse ---
# re.compile() is more efficient when the same pattern is used many times.
print("\n--- Compiled Patterns ---")
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
sample_text = "Contact us at support@example.com or sales@example.co.uk"
emails = email_pattern.findall(sample_text)
print(f"Emails found: {emails}")

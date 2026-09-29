"""
Topic: collections - deque and ChainMap
deque provides fast appends/pops from both ends; ChainMap groups multiple
dictionaries into a single, searchable view without merging them.
"""

from collections import ChainMap, deque

# --- 1. deque: A Double-Ended Queue ---
# Unlike a list, deque has O(1) appends/pops from BOTH ends (list.insert(0, x)
# and list.pop(0) are O(n) because every remaining element must shift).
print("--- deque Basics ---")
queue = deque([1, 2, 3])
queue.append(4)         # add to the right end
queue.appendleft(0)      # add to the left end
print(f"After append(4) and appendleft(0): {queue}")
queue.pop()              # remove from the right end
queue.popleft()          # remove from the left end
print(f"After pop() and popleft(): {queue}")

# --- 2. deque as a Fixed-Size Sliding Window ---
print("\n--- deque with maxlen (Sliding Window) ---")
last_three = deque(maxlen=3)
for number in range(1, 7):
    last_three.append(number)
    print(f"  After adding {number}: {list(last_three)}")

# --- 3. deque for Fast Rotation ---
print("\n--- deque.rotate() ---")
letters = deque(["A", "B", "C", "D", "E"])
letters.rotate(2)    # positive rotates right
print(f"Rotated right by 2: {letters}")
letters.rotate(-2)   # negative rotates left (undoes the previous rotation)
print(f"Rotated left by 2 (back to original): {letters}")

# --- 4. ChainMap: Search Multiple Dictionaries as One ---
# Useful for layered configuration: e.g., command-line overrides > user config > defaults.
print("\n--- ChainMap ---")
defaults = {"theme": "light", "font_size": 12, "language": "en"}
user_settings = {"theme": "dark"}
command_line_overrides = {"font_size": 16}

settings = ChainMap(command_line_overrides, user_settings, defaults)
print(f"Effective 'theme': {settings['theme']}")            # from user_settings
print(f"Effective 'font_size': {settings['font_size']}")     # from command_line_overrides
print(f"Effective 'language': {settings['language']}")       # falls through to defaults
print(f"All effective settings merged: {dict(settings)}")

# Writes only ever affect the FIRST mapping in the chain.
settings["theme"] = "high-contrast"
print("\nAfter settings['theme'] = 'high-contrast':")
print(f"command_line_overrides: {command_line_overrides}")
print(f"user_settings (unchanged): {user_settings}")

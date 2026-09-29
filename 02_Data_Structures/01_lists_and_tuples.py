"""
Topic: Lists and Tuples
Lists are mutable ordered sequences; tuples are immutable ordered sequences.
"""

# --- 1. Creating Lists and Tuples ---
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = ("apple", "banana", "cherry")
print("--- Creation ---")
print(f"List: {fruits_list}")
print(f"Tuple: {fruits_tuple}")

# --- 2. Indexing ---
# Both support zero-based indexing and negative indexing (-1 refers to the last item).
print("\n--- Indexing ---")
print(f"First fruit (list): {fruits_list[0]}")
print(f"Last fruit (tuple): {fruits_tuple[-1]}")

# --- 3. Slicing ---
# sequence[start:stop:step] - the stop index is exclusive.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n--- Slicing ---")
print(f"numbers[2:5]: {numbers[2:5]}")
print(f"numbers[:4]: {numbers[:4]}")
print(f"numbers[6:]: {numbers[6:]}")
print(f"numbers[::2]: {numbers[::2]}")     # every second element
print(f"numbers[::-1]: {numbers[::-1]}")   # reversed copy

# --- 4. Common List Methods (lists are mutable) ---
print("\n--- List Methods ---")
fruits_list.append("date")            # add to the end
print(f"After append('date'): {fruits_list}")
fruits_list.insert(1, "blueberry")    # insert at a specific index
print(f"After insert(1, 'blueberry'): {fruits_list}")
fruits_list.remove("banana")          # remove the first matching value
print(f"After remove('banana'): {fruits_list}")
popped_item = fruits_list.pop()       # remove and return the last item
print(f"Popped item: {popped_item}, remaining: {fruits_list}")
fruits_list.sort()                    # sort in place
print(f"After sort(): {fruits_list}")
fruits_list.reverse()                 # reverse in place
print(f"After reverse(): {fruits_list}")

# --- 5. Tuples Are Immutable ---
print("\n--- Tuple Immutability ---")
try:
    fruits_tuple[0] = "avocado"
except TypeError as error:
    print(f"Cannot modify a tuple: {error}")

# Tuples still support read-only methods.
print(f"Count of 'apple' in tuple: {fruits_tuple.count('apple')}")
print(f"Index of 'cherry' in tuple: {fruits_tuple.index('cherry')}")

# --- 6. Tuple Unpacking ---
print("\n--- Tuple Unpacking ---")
first, second, third = fruits_tuple
print(f"Unpacked values: {first}, {second}, {third}")

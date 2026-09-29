"""
Topic: os module and Environment Variables
The os module provides operating-system interfaces: environment variables,
process info, and lower-level filesystem operations that predate pathlib.
"""

import os

# --- 1. Reading Environment Variables ---
print("--- Reading Environment Variables ---")
# os.environ.get() is safer than os.environ[...] - it won't raise KeyError.
username = os.environ.get("USERNAME", "unknown")  # "USERNAME" on Windows, "USER" elsewhere
print(f"Current user (from environment): {username}")
print(f"PATH variable is set: {'PATH' in os.environ}")

# --- 2. Setting a Temporary Environment Variable ---
# This only affects THIS process (and any child processes it spawns) -
# it does not permanently change your system's environment.
print("\n--- Setting an Environment Variable for This Process ---")
os.environ["MY_APP_MODE"] = "development"
print(f"MY_APP_MODE = {os.environ.get('MY_APP_MODE')}")

# --- 3. Common os Functions ---
print("\n--- Common os Functions ---")
print(f"os.getcwd(): {os.getcwd()}")
print(f"os.name (os identifier): {os.name}")
print(f"len(os.listdir('.')): {len(os.listdir('.'))} entries in the current directory")

# --- 4. os.path vs. pathlib ---
# os.path works with plain strings; pathlib (see 01_pathlib_deep_dive.py) is
# the more modern, object-oriented alternative. Both are still widely used.
print("\n--- os.path (string-based, the older API) ---")
sample_path = os.path.join("folder", "subfolder", "file.txt")
print(f"os.path.join(...): {sample_path}")
print(f"os.path.basename(...): {os.path.basename(sample_path)}")
print(f"os.path.dirname(...): {os.path.dirname(sample_path)}")
print(f"os.path.splitext(...): {os.path.splitext(sample_path)}")


# --- 5. A Practical Pattern: Configuration via Environment Variables ---
print("\n--- Practical Pattern: Config via Environment Variables ---")


def get_debug_mode():
    """Read a boolean-like setting from the environment, with a safe default."""
    return os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")


print(f"Debug mode enabled: {get_debug_mode()}")
os.environ["DEBUG"] = "true"
print(f"After setting DEBUG=true: {get_debug_mode()}")

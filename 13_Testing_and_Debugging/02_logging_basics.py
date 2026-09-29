"""
Topic: Logging
The logging module is the professional alternative to print() debugging:
it supports severity levels, timestamps, and configurable output destinations.
"""

import logging

# --- 1. Basic Configuration ---
# level=INFO means DEBUG messages are suppressed; only INFO and above are shown.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# --- 2. The Five Standard Severity Levels ---
print("--- Logging Levels (DEBUG is suppressed at level=INFO) ---")
logger.debug("This is a DEBUG message (won't be shown).")
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")


# --- 3. Logging Exceptions with Context ---
def divide(a, b):
    """Divide two numbers, logging the exception if it fails."""
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Division failed - see traceback below:")
        return None


print("\n--- Logging an Exception with Traceback ---")
divide(10, 0)

# --- 4. Using a Named Logger per Module ---
# __name__ makes it easy to trace which module a log message came from.
print("\n--- Logger Named After the Module ---")
print(f"logger.name = {logger.name}")

# --- 5. Adjusting the Logging Level at Runtime ---
print("\n--- Raising the Logging Level to WARNING ---")
logger.setLevel(logging.WARNING)
logger.info("This INFO message is now suppressed.")
logger.warning("This WARNING message still appears.")

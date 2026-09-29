"""
Topic: Command-Line Arguments (sys.argv and argparse)
Scripts often need input from the command line rather than interactive
input(). sys.argv is the raw, manual approach; argparse is the standard,
much more robust way to define and parse arguments.
"""

import argparse
import sys

# --- 1. sys.argv: The Raw Argument List ---
# sys.argv[0] is always the script name; the rest are the arguments passed in.
print("--- sys.argv ---")
print(f"Raw arguments received: {sys.argv}")
print(f"Script name: {sys.argv[0]}")
print(f"Extra arguments (if any): {sys.argv[1:]}")

# --- 2. argparse: A Robust CLI Argument Parser ---
# argparse auto-generates --help text, validates types, and reports clear
# errors for missing/invalid arguments. The flags below are optional (with
# defaults) so this script also runs with zero arguments; argparse supports
# required positional arguments too (e.g., parser.add_argument("name")).
print("\n--- argparse ---")

parser = argparse.ArgumentParser(
    description="A demo script showing how argparse defines a command-line interface."
)
parser.add_argument("--name", default="World", help="Name of the person to greet")
parser.add_argument(
    "--times", type=int, default=1, help="How many times to repeat the greeting"
)
parser.add_argument(
    "--shout", action="store_true", help="Print the greeting in uppercase"
)

# parse_known_args() ignores unrecognized extra args, keeping this demo
# runnable even inside tools (like test runners) that inject their own flags.
args, _unknown = parser.parse_known_args()

print(f"Parsed arguments: name={args.name!r}, times={args.times}, shout={args.shout}")

for _ in range(args.times):
    greeting = f"Hello, {args.name}!"
    print(greeting.upper() if args.shout else greeting)

print("\nTry running this from a terminal with custom arguments, for example:")
print("  python 02_command_line_arguments.py --name Alice --times 3 --shout")

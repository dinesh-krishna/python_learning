"""
Topic: pathlib Deep Dive
pathlib.Path represents filesystem paths as objects (not raw strings),
making path manipulation more readable and less error-prone than os.path.
"""

from pathlib import Path

# --- 1. Creating Paths ---
print("--- Creating Paths ---")
script_path = Path(__file__)      # path to this very script
current_dir = script_path.parent  # the folder containing this script
print(f"script_path = {script_path}")
print(f"current_dir = {current_dir}")

# The '/' operator joins path segments - cleaner than manual string concatenation.
data_dir = current_dir / "sample_data"
config_file = data_dir / "config.json"
print(f"data_dir (built with '/'): {data_dir}")
print(f"config_file (built with '/'): {config_file}")

# --- 2. Inspecting Path Components ---
print("\n--- Inspecting Path Components ---")
print(f"script_path.name: {script_path.name}")
print(f"script_path.stem (no extension): {script_path.stem}")
print(f"script_path.suffix: {script_path.suffix}")
print(f"script_path.parent: {script_path.parent}")
print(f"script_path.parts: {script_path.parts}")

# --- 3. Checking Existence and Type ---
print("\n--- Checking Existence and Type ---")
print(f"script_path.exists(): {script_path.exists()}")
print(f"script_path.is_file(): {script_path.is_file()}")
print(f"current_dir.is_dir(): {current_dir.is_dir()}")

# --- 4. Creating Directories and Files ---
print("\n--- Creating Directories and Files ---")
data_dir.mkdir(exist_ok=True)  # exist_ok=True avoids an error if it already exists
sample_file = data_dir / "notes.txt"
sample_file.write_text("Created with pathlib!\n", encoding="utf-8")
print(f"Created {sample_file}")
print(f"Contents: {sample_file.read_text(encoding='utf-8').strip()}")

# --- 5. Listing and Filtering Directory Contents ---
print("\n--- Listing Directory Contents ---")
for entry in current_dir.iterdir():
    kind = "dir" if entry.is_dir() else "file"
    print(f"  [{kind}] {entry.name}")

print("\n--- Glob for .py Files ---")
python_files = list(current_dir.glob("*.py"))
print(f".py files in this folder: {[f.name for f in python_files]}")

# --- 6. Building Cross-Platform Paths ---
# pathlib automatically uses the correct separator ('\\' on Windows, '/' elsewhere).
print("\n--- Cross-Platform Path Building ---")
cross_platform_path = Path("folder") / "subfolder" / "file.txt"
print(f"cross_platform_path: {cross_platform_path}")
print(f"As a POSIX-style string: {cross_platform_path.as_posix()}")

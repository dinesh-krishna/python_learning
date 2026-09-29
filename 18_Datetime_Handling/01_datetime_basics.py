"""
Topic: datetime
The datetime module handles dates, times, and time differences - essential
for logging, scheduling, and any time-aware application logic.
"""

from datetime import date, datetime, time, timedelta

# --- 1. date, time, and datetime Objects ---
print("--- Creating date/time/datetime Objects ---")
today = date.today()
specific_date = date(2026, 12, 25)
specific_time = time(14, 30, 0)
specific_datetime = datetime(2026, 12, 25, 14, 30, 0)
now = datetime.now()

print(f"today = {today}")
print(f"specific_date = {specific_date}")
print(f"specific_time = {specific_time}")
print(f"specific_datetime = {specific_datetime}")
print(f"now = {now}")

# --- 2. Accessing Components ---
print("\n--- Accessing Components ---")
print(f"now.year = {now.year}, now.month = {now.month}, now.day = {now.day}")
print(f"now.hour = {now.hour}, now.minute = {now.minute}, now.second = {now.second}")
print(f"now.weekday() (Mon=0..Sun=6): {now.weekday()}")

# --- 3. Formatting: datetime -> str (strftime) ---
print("\n--- strftime(): datetime -> str ---")
print(f"now.strftime('%Y-%m-%d'): {now.strftime('%Y-%m-%d')}")
print(f"now.strftime('%B %d, %Y'): {now.strftime('%B %d, %Y')}")
print(f"now.strftime('%H:%M:%S'): {now.strftime('%H:%M:%S')}")
print(f"now.isoformat(): {now.isoformat()}")

# --- 4. Parsing: str -> datetime (strptime) ---
print("\n--- strptime(): str -> datetime ---")
date_string = "2026-09-29 09:00:00"
parsed = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed '{date_string}' -> {parsed} (type: {type(parsed).__name__})")

# --- 5. timedelta: Differences and Arithmetic ---
print("\n--- timedelta ---")
one_week = timedelta(weeks=1)
next_week = today + one_week
print(f"today + 1 week = {next_week}")

difference = specific_date - today
print(f"Days until {specific_date}: {difference.days}")

deadline = now + timedelta(days=3, hours=2)
print(f"Deadline (now + 3 days, 2 hours): {deadline}")

# --- 6. Comparing Dates and Times ---
print("\n--- Comparisons ---")
print(f"specific_date > today: {specific_date > today}")
print(f"today == date.today(): {today == date.today()}")

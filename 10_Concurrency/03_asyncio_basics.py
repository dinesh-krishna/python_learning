"""
Topic: asyncio Basics
asyncio provides cooperative concurrency using a single thread: instead of the
OS switching between threads, your code explicitly "awaits" at points where it
would otherwise block, letting other tasks run in the meantime. Best suited
for many simultaneous I/O-bound operations (network requests, etc.).
"""

import asyncio
import time


# --- 1. A Basic Coroutine ---
async def say_after(delay, message):
    """An async function ('coroutine') that pauses without blocking other tasks."""
    await asyncio.sleep(delay)  # non-blocking sleep - other tasks can run meanwhile
    print(f"  {message} (after {delay}s)")


async def sequential_demo():
    """Awaiting coroutines one after another still runs them in sequence."""
    start = time.perf_counter()
    await say_after(0.3, "First")
    await say_after(0.3, "Second")
    print(f"Sequential await total: {time.perf_counter() - start:.2f}s")


# --- 2. Running Coroutines Concurrently with asyncio.gather ---
async def concurrent_demo():
    """gather() schedules multiple coroutines to run concurrently."""
    start = time.perf_counter()
    await asyncio.gather(
        say_after(0.3, "Task A"),
        say_after(0.3, "Task B"),
    )
    print(f"Concurrent gather total: {time.perf_counter() - start:.2f}s (faster!)")


# --- 3. Creating and Awaiting Tasks Individually ---
async def task_demo():
    """asyncio.create_task() schedules a coroutine to start running immediately."""
    task1 = asyncio.create_task(say_after(0.2, "Task 1"))
    task2 = asyncio.create_task(say_after(0.2, "Task 2"))
    # Both tasks are already running concurrently by the time we await them.
    await task1
    await task2


# --- 4. The Main Entry Point ---
async def main():
    print("--- Sequential await (no concurrency) ---")
    await sequential_demo()

    print("\n--- Concurrent asyncio.gather() ---")
    await concurrent_demo()

    print("\n--- Individually Created Tasks ---")
    await task_demo()


if __name__ == "__main__":
    # asyncio.run() creates an event loop, runs main() to completion, then closes it.
    asyncio.run(main())

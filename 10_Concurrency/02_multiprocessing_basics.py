"""
Topic: Multiprocessing Basics
Multiprocessing runs code in separate processes (each with its own Python
interpreter and memory), bypassing the GIL entirely. This makes it ideal for
CPU-bound work (heavy computation), unlike threading which suits I/O-bound work.

Note: multiprocessing on Windows requires the "if __name__ == '__main__':"
guard shown below, because child processes re-import this module. Target
functions must also be defined at module level so they can be pickled.
"""

import multiprocessing
import time


def cpu_bound_task(n):
    """A deliberately expensive computation to demonstrate parallel speedup."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def increment_shared(counter, times):
    """Increment a shared, cross-process counter safely using its built-in lock."""
    for _ in range(times):
        with counter.get_lock():  # processes need explicit locking too
            counter.value += 1


def run_sequential(task_sizes):
    """Run each task one after another on a single core."""
    start = time.perf_counter()
    results = [cpu_bound_task(size) for size in task_sizes]
    elapsed = time.perf_counter() - start
    print(f"Sequential results: {results}")
    print(f"Sequential time: {elapsed:.2f}s")


def run_parallel(task_sizes):
    """Run each task in its own process, using multiple CPU cores."""
    start = time.perf_counter()
    with multiprocessing.Pool(processes=len(task_sizes)) as pool:
        results = pool.map(cpu_bound_task, task_sizes)
    elapsed = time.perf_counter() - start
    print(f"Parallel results: {results}")
    print(f"Parallel time: {elapsed:.2f}s")


if __name__ == "__main__":
    # Required on Windows: child processes import this file, so code that
    # starts new processes must be guarded to avoid infinite recursion.
    task_sizes = [3_000_000] * 4

    print("--- Sequential Execution ---")
    run_sequential(task_sizes)

    print("\n--- Parallel Execution with multiprocessing.Pool ---")
    run_parallel(task_sizes)

    # --- Sharing State Between Processes ---
    print("\n--- Sharing State with multiprocessing.Value ---")
    shared_counter = multiprocessing.Value("i", 0)  # 'i' = signed int
    processes = [
        multiprocessing.Process(target=increment_shared, args=(shared_counter, 1000))
        for _ in range(4)
    ]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print(f"Final shared_counter (expected 4000): {shared_counter.value}")

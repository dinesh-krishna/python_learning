"""
Topic: Threading Basics
Threads let multiple pieces of Python code run concurrently, which is ideal
for I/O-bound work (network calls, file I/O). Due to the GIL (Global
Interpreter Lock), threads do NOT achieve true CPU parallelism in CPython -
use multiprocessing for that instead (see 02_multiprocessing_basics.py).
"""

import queue
import threading
import time


# --- 1. Creating and Starting Threads ---
def download_file(file_id, delay):
    """Simulate a slow, I/O-bound task like downloading a file."""
    print(f"  Thread {file_id}: starting download...")
    time.sleep(delay)  # simulates waiting on network I/O
    print(f"  Thread {file_id}: download complete!")


print("--- Sequential Execution (for comparison) ---")
start = time.perf_counter()
download_file(1, 0.3)
download_file(2, 0.3)
print(f"Sequential total time: {time.perf_counter() - start:.2f}s")

print("\n--- Concurrent Execution with Threads ---")
start = time.perf_counter()
thread1 = threading.Thread(target=download_file, args=(1, 0.3))
thread2 = threading.Thread(target=download_file, args=(2, 0.3))
thread1.start()
thread2.start()
thread1.join()  # wait for thread1 to finish before continuing
thread2.join()  # wait for thread2 to finish before continuing
print(f"Concurrent total time: {time.perf_counter() - start:.2f}s (faster!)")

# --- 2. Race Conditions and Locks ---
# Without a lock, two threads updating shared state can interfere with each other.
counter = 0
counter_lock = threading.Lock()


def increment_counter(times):
    """Safely increment the shared 'counter' using a lock."""
    global counter
    for _ in range(times):
        with counter_lock:  # only one thread at a time can hold the lock
            counter += 1


print("\n--- Locks Prevent Race Conditions ---")
threads = [threading.Thread(target=increment_counter, args=(100_000,)) for _ in range(4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"Final counter (expected 400000): {counter}")

# --- 3. Thread-Safe Data Sharing with queue.Queue ---
work_queue = queue.Queue()
for item in range(5):
    work_queue.put(item)


def worker(worker_id):
    """Pull items off the shared queue until it's empty."""
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()
        except queue.Empty:
            break
        print(f"  Worker {worker_id} processed item {item}")


print("\n--- queue.Queue for Thread-Safe Sharing ---")
workers = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
for w in workers:
    w.start()
for w in workers:
    w.join()

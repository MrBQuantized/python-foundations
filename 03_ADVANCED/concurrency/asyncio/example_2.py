"""
This example is almost similar to example_1.py, except that 
in this case, we are making use of asynchronous functions (coroutines).
So, while one task is being suspended (hits await()), the event 
loop initiates the executes the next task in the queue.
There's no concurrency so, the performance is the same.

In the next example, we will see one of ways to implement
concurrency.

"""

import asyncio
import time


# Asynchronous
async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = fetch_data(1)       # Could be awaited directly (i.e.task1 = await fetch_data(1))   
    task2 = fetch_data(2)       # Could be awaited directly (i.e.task2 = await fetch_data(2))
    result1 = await task1
    print("Fetch 1 fully completed")
    result2 = await task2
    print("Fetch 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f}")
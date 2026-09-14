"""
This example demonstrates one of the correct ways to implement 
asynchronous code. The only difference between this example and the previous
one (example_2.py) is that we are actually creating tasks from the 
coroutines using `asyncio.create_task(async_func())`, instead of just 
calling those coroutines directly (i.e creating coroutine objects).
The coroutines are scheduled to run on the event loop 

"Do something with 1" and "Do something with 1" will run one after without 
the first task is fully complete. 
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
    task1 = asyncio.create_task(fetch_data(1))    
    task2 = asyncio.create_task(fetch_data(2))   
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
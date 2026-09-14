"""
In this example, we would be simulating the usual synchronous function.
We will observe idleness in the program when tasks are suspended using the time.sleep() 
function as no event loop would be used. 
`perf_counter()` will be used for instantiating executing time of each task and

This program can be improved with concurrent code execution using async functions.
"""

import time


# Synchronous
def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

def main():
    result1 = fetch_data(1)
    print("Fetch 1 fully completed")
    result2 = fetch_data(2)
    print("Fetch 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = main()
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f}")
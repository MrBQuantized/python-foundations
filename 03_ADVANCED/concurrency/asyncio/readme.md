# Asyncio

Asyncio is Python's built-in library for writing concurrent code.

## Synch vs Async

### 1. Synchronous

With synchronous code execution (which we normally use), one thing happens after another. They are best used in computing or CPU-bound operations e.g. heavy calculations, image processing, data-crunching. These tasks keep the PC busy doing actual work(No waiting). Multiple processes are used.

### 2. Asynchronous

In concurrent code, multiple tasks can be executed at the same period of time.For instance, instead of waiting for external tasks like database queries/response, network request, API calls, we can do other useful work during that time instead of idly sitting-by. These tasks are called I/O-bound tasks. They require asynchronous code execution for improved performance.

Asyncio is single-threaded and runs on a single process. They make use of what is known as "COOPERATIVE MULTITASKING" where tasks voluntarily give up control.

### 3. Concurrency:

This refers to multiple tasks being in progress during the same period.

### 4. Parallelism
Multiple tasks execute at the same instant, usually on multiplee CPU cores

> ### _!!! NOTE: Asynchronous doesn't automatically mean it's faster._

---



## BASIC ASYNC TERMINOLOGIES

## 1. Event loop (Scheduler)
This is the core manager that handles and shedules concurrent tasks within a single thread

```python
async def main():
    ...

if __name__ == "__main__":
    # Event loop
    asyncio.run(main())
```

### How it works

- **The Ready queue**: The loop maintains a queue of tasks that are to run right now
- **Execution**: It picks the top task and execute its code.
- **The Yield** `(await)` : The tasks runs until it hits an await expression (e.g., `await network_request()`). This pauses the task, packages it up, and hands control back to the loop.
- **I/O Polling**: While the task waits for **I/O**, the loop executes other ready tasks so the CPU never sits idle.
- **Resuming**: Once the underlying system alerts the loop that the network request or timer is done, 
- the loop moves the original task into the "ready" queue to pick up exactly where it left off.


## 2. Awaitables: 

Objects that implement a special await() method under the hood `await()` tells the event loop to pause the execution of the current function and yield control back to the event loop which can then run another function. It will remain suspended until awaitable completes.

The three main tyes of awaitable objects are:
- **Coroutines** : Functions declared with `async def`. Calling them doesn't run code; it just returns a coroutine object.
They are objects created when async functions are called.
- **Tasks**      : Wrappers around coroutines that are scheduled on the event loop. They are the schedulers to coroutines.
- **Futures**    : Low-level objects representing a result. Like Promises in JavaScript

Below is an example demostrating the awaitable objects in async code:
```python

# Synchronous function
def sync_function(test_param: str) -> str:
    print("This is a synchronous function.")

    time.sleep(0.1)

    return f"Sync Result: {test_param}"


# ALSO KNOWN AS COROUTINE FUNCTION
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")

    await asyncio.sleep(0.1)

    return f"Async Result: {test_param}"


async def main():
    # Couroutine
    coroutine_obj = async_function("Test")
    print(coroutine_obj)

    coroutine_result = await coroutine_obj
    print(coroutine_result)

    # Tasks
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)
```

"""
We are diving deeper into multithreading

Topic: Synchronizatlion of Threads

Imagine a situation you are running mutilple threads at once that access the same resource, you would want to  be able to manage it and ensure that there are no issues or errors. This is what the synchronization of threads tries to achieve.

Two common methods we will be treated are: 
    1. Lock         —  Allows one thread to execute before the next
    2. Semaphore    —  Limits the number of threads to a maximum value.
"""
import threading

# ===================================
# Locking 
# =================================== 
# A trivial example is a shared resource — a number, n
# One thread doubles it while the other divides it by 2 (counteracting threads)
# We lock the thread so that one gets to the max number and the other, the mininum
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)  # delay the program for 1 seconds for tracking purposes
    print("Reached the maximum!")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()


# We need to run two threads that executes both functions on parallel.
t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

# t1.start()
# t2.start()


# ===================================
# Semaphore 
# =================================== 

semaphore = threading.BoundedSemaphore(value=5) 


def access(thread_number):
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)
    print(f"{thread_number} is now releasing!")
    semaphore.release()

# Make a for-loop for 10 threads 
for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)


# The semaphore method with a value=ensures that only 5 threads run at a time.
# Thread 6 will only run when thread 1 releases, 7 after 2
"""
Threading helps us to speed up our program by executing 
mutliple tasks at the same time (with "so-called" threads)

This is seen in cases such as video games. You want all the actions, and movement and the rendering to happend simultaneously and not linearly (one after the other)
"""

import threading

# We define a function for the thread

def helloworld():
    print("Hello World!")

t1 = threading.Thread(target=helloworld)   # We are not calling helloworld
# t1.start()

# Threads allow us to execute two functions simultaneously

def function1():
    for x in range(10):
        print("ONE")
        # x +=1
        # print(f"{x:02.0f}   ONE")
        # if x == 1:
        #     print(f"TWO is printed {x} time")
        # else:
        #     print(f"TWO is printed {x} times")

def function2():
    for x in range(10):
        print("TWO")
        # x +=1
        # print(f"{x:02.0f}   TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

# Use the start function so that both can run at the same time.
# t1.start()
# t2.start()


# With a another print statement after your thread, the print statement
# executes alongside or even before the main thread. You can prevent this by
# using the .join() function.

def function3():
    for x in range(10):
        print("THREE")

t3 = threading.Thread(target=function3)
t3.start()
t3.join()
print("Something else")
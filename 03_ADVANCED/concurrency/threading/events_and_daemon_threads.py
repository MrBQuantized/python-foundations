"""
Topic: Events and Daemon Threading

Event and daemon are two important concepts in threading

Events are things in python that we can trigger.
When we trigger them, wwe can react to them in the code.

Daemon threads run in the background and the script terminates even though they are still running.
They are not to the program
"""
import threading
import time

# =====================================
# Events
# =====================================
# Creating events
event = threading.Event()

# This function is an event that waits until it's triggered
def myfunction():
    print("⏳ Waiting for event for trigger...\n")
    event.wait()

    print("🎬 Performing action XYZ now...")

# We define the the event
t1 = threading.Thread(target=myfunction)

# trigger the event
# t1.start()

# Choose to trigger the event or not
# x = input("Do you want to trigger the event? (y/n)\n")
# if x == "y":
    # set function triggers the event
    # event.set()

# =====================================
# Daemon Threads
# =====================================
from pathlib import Path

dir = Path(__file__).resolve().parents[0]
path = dir / "test.txt"
text = ""

print(path)
print(path.is_file())
# define a function that reads info from a file iteratively with
# with 3sec breaks in-between

def readFile():
    global text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()




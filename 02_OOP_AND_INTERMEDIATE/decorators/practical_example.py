"""
Practice script for Python.

Topic: Decorators in Practice

Real-world uses for decorators, building on the general pattern of
wrapping a function to add extra behavior.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Logging
# =================================================

# import os
# from pathlib import Path

# PATH = Path(__file__).resolve().parent
# os.chdir(PATH)
# print("Current working directory: ", os.getcwd())

# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)
#         # Logging
#         with open('logfile', 'a+') as f:
#             fname = function.__name__
#             print(f"{fname} returned value {value}")
#             f.write(f"{fname} returned value {value}\n")
#         return value
#
#     return wrapper

# @logged
# def add(x, y):
#     return x + y

# print(add(10, 20))

# =================================================
# Example 2: Timing
# =================================================

import time
import sys

# Increase the maximum limit for integer-to-string conversion, since
# the factorial-like result below produces a very large number.
sys.set_int_max_str_digits(maxdigits=100000)


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute.")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunction(90000)
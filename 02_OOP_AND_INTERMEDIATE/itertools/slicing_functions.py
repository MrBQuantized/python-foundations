"""
Python scripts on Itertools
Covers itertools functions that allows us to select certain items from iterables.
"""

# ===========================================
# Compress
# ===========================================
# This function used often in DS where there is some data and selectors 
# The selectors are used to filter down the data


import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)

for item in result:
    print(item)

print()
# it returns an iterable of values that are values of the iterable letters matching the True values in selectors.
# It is similar to the filter function in the sense that the filtered values are passed as iterables 
# while filter() needs a function


# ===========================================
# filter false
# ===========================================
# This function complements the built-in filter function
# returns the false values instead of True


def even(n):
    if n < 2:
        return True

    return False

result = itertools.filterfalse(even, numbers)

for item in result:
    print(item)

print()
# Two more itertools functions similar to the
# filter functions are:

# ===========================================
# Drop while
# ===========================================
# Drops values from an iterable till one value returns True.

values = [1, 3, 5, 6, 3, 2, 9]
result = itertools.dropwhile(even, values)

for item in result:
    print(item)

print()

# ===========================================
# Take while
# ===========================================
# Returns all values that are True until it reaches a False value
result = itertools.takewhile(even, values)

for item in result:
    print(item)

print()

# ===========================================
# Accumulate
# ===========================================
nums = [1, 2, 3, 4, 5, 6]
result = itertools.accumulate(nums)

for items in result:
    print(result)
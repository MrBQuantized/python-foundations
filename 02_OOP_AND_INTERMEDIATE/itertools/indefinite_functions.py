"""
Python script for infinite itertools functions

Itertools — a collection of tools that help us work with 
iterators in a fast and memory-efficient way.

An iterator is a sequential data that can be iterated or looped over.
The infinite itertools functions include:

    count, zip_longest, cycle, repeat, star map.
"""

import itertools

# ======================================
# Count
# ======================================
# By default, it starts at and counts by 1. This will be an ifinite operation
counter = itertools.count()

# for num in counter:
    # print(num)  

# Instead of using a for-loop, we can use the next() function and pass in the iterator.
# This would prints all the next values one-by-one each time it is printed
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# we can also have a list of values with index positions
# Supppose we want to pair each number with some index values on a daily basis

data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data))

# This runs until the shortest iterable, (data) is exhausted 

print(daily_data)
print()
# Passing  arguments into count function
# We can choose different starting and step values

counter = itertools.count(start=4, step=3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# The step can also accept decimals and negative values
counter = itertools.count(start=5, step=-2.5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# ======================================
# zip_longest
# ======================================
# Unlike the in-built zip function, the zip_longest runs and pairs 
# the iterables together. When the shortest one is exhausted, it continues 
# and pairs the rest of the longer iterable with None values from the shortest 

# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)


# ======================================
# Cycle
# ======================================
# Cycle also returns an iterable that goes on forever. It takes an iterable and cycles over the iterable infinitely.

counter = itertools.cycle([1,2,3,4])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# It can also cycle through a tuple of strings of On and Off
cycle = itertools.cycle(('On', 'Off'))

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()

# ======================================
# Repeat
# ======================================
# The repeat function takes some input and repeats it indefinitely
# we can also set the number of times for which the value should be repeated and throws an exception if the statement exceeds the repeat count.
repeat = itertools.repeat(2, times=4)

for time in repeat:
    print(time)

 
# A good use case would be in getting the powers 1, 2, 3... of a number, say 2.
squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))    


# ======================================
# Star Map
# ======================================
# This function is very similar to the map function.
# However, instead of taking arguments from iterables, it takes arguments that are already paired as tuples.

# First few powers

# squares = itertools.starmap(pow, [(0, 2), (1, 2)], (2, 2))
# or
data = itertools.repeat(2)
count = range(5)
squares = itertools.starmap(pow, list(zip(count, data)))

print(list(zip(count, data)))
print(list(squares))
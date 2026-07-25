"""
Practice script for Python.

Topic: Generator Comprehension

Generators are memory efficient. Rather than storing every value in
memory at once, a generator produces each value lazily, only when it's
requested.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Generator Functions vs. Generator Expressions
# =================================================
# A generator expression is similar to a list comprehension, but
# produces values lazily instead of building the full list upfront.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)

# The same result using a generator expression
my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)

# The same result using map() with a lambda
my_gen = map(lambda n: n * n, nums)
myList = [n for n in my_gen]
print(myList)

# =================================================
# Example 2: Generator Expressions and Generator Objects
# =================================================

from typing import Generator

data: range = range(10_000)
squared: Generator[int, None, None] = (pow(n, 2) for n in data)
print(squared)      # Prints the generator object itself, not its values
print(next(squared))
print(next(squared))
print(next(squared))
print(next(squared))
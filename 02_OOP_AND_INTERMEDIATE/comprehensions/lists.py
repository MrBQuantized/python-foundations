"""
Practice script for Python.

Topic: Set Comprehension

Set comprehension provides a concise way to build a set from an
iterable, using a single expression instead of a loop with explicit
add() calls. Since sets only store unique values, duplicates in the
source data are automatically dropped.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Set Comprehension
# =================================================

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 9]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# The same result using comprehension
my_set = {n for n in nums}
print(my_set)

# =================================================
# Example 2: Using Type Hints
# =================================================

values: list[int] = [5, 5, 5, 11, 11, 5, 10, 6, 45, 9, 6, 9, 9, 100]
filtered: set[int] = {v for v in values}
print(filtered)

# =================================================
# Example 3: Comprehension with Expressions and Conditions
# =================================================

values: list[int] = [5, 5, 5, 11, 11, 5, 10, 6, 45, 9, 6, 9, 9, 100]
filtered: set[int] = {v * 2 for v in values}
print(filtered)

values: list[int] = [5, 5, 5, 11, 11, 5, 10, 6, 45, 9, 6, 9, 9, 100]
filtered: set[int] = {v for v in values if v > 10 and v % 2 == 0}
print(filtered)

values: list[int] = [5, 5, 5, 11, 11, 5, 10, 6, 45, 9, 6, 9, 9, 100]
filtered: set[int] = {pow(v, 2) for v in values if v > 10}
print(filtered)
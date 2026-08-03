"""
Python Script on itertools

Definite functions: These are functions that will eventually terminate.
We will first deal with the most common ones — Combinations and Permutations.
These methods are ways to count groups/sequences/iterables, but with a little caveat:

    Combination  : The order does not matter
    Permutation  : The order matters

These arrangement methods do not repeat values (i.e. a,a or  b,b).

"""

import itertools

# =======================================
# Combinations & Permutations
# =======================================

letters = ['a', 'b', 'c', 'd']
names = ['Corey', 'Nicole']

# All possible combinations of two values/items from letters 
result = itertools.combinations(letters, 2)

for item in result:
    print(item)

print()
# And all the possible ordered combinations
result = itertools.permutations(letters, 2)

for item in result:
    print(item)

# =======================================
# Product
# =======================================
# Since combination and permutation methods do not allow repetition of values,
# we can use the cartesian product function to produce combination of values that allows for repetition of values.
# Let's see the possible ways to create a four digit code 
numbers = [0, 1, 2, 3]
# repeated = itertools.product(numbers, repeat=4)

# for item in repeated:
#     print(item)


# =======================================
# Combinations_with_replacement
# =======================================
# This is another itertool function that allows us to create combinations with repeated values
# We pass in the repitition value as positional argument instead
numbers = [0, 1, 2, 3]
repeated = itertools.combinations_with_replacement(numbers, 4)

# for item in repeated:
#     print(item)



# =======================================
# Chain
# =======================================
# The chain method is used in combination of iterables and then looping through each of the items in each iterable in a memory efficient way

combined = itertools.chain(letters, numbers, names)

for item in combined:
    print(item)

# =======================================
# Islice
# =======================================
# This allows us to perform slicing on an iterator
# The arguments it takes are: 
#       .islice(iterable, start, stop, step)
# This method is useful especially in a scenario where we have an iterator too large to put into memory.
# We would want to get just a slice of it instead.

sliced = itertools.islice(range(10), 2, 10, 2)

for item in sliced:
    print(item)

# A more practical example

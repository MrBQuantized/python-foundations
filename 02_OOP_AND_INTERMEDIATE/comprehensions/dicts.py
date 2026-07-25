"""
Practice script for Python.

Topic: Dictionary Comprehension

Dictionary comprehension provides a concise way to build a dictionary
from an iterable, using a single expression instead of a loop with
explicit key assignments.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

players = ['Lionel Messi', 'Kylian Mbappe', 'Cristiano Ronaldo', 'Maestro Kimpembe', 'Lamine Yamal']
number = [10, 9, 7, 3, 10]

# =================================================
# Example 1: Building a Dictionary with a Loop
# =================================================
# dict{'player': 'num'} from each player, num in zip(players, nums)

my_dict = {}
for player, num in zip(players, nums):
    my_dict[player] = num
print(my_dict)

# =================================================
# Example 2: Dictionary Comprehension
# =================================================

my_dict = {player: num for player, num in zip(players, nums)}
print(my_dict)

# =================================================
# Example 3: Comprehension with a Conditional
# =================================================
# We can also add restrictions.

my_dict = {player: num for player, num in zip(players, nums) if player != 'Lamine Yamal'}
print()
print(my_dict)

# =================================================
# Example 4: Using Type Hints
# =================================================

data: list[tuple[str, int]] = [('a', 1), ('b', 2), ('c', 3)]
my_dict: dict[str, int] = {k: v for k, v in data}
print(my_dict)
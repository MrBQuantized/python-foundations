# ======================================
# Multiplication Table
# ======================================

"""
Problem:
Generate the multiplication table for a given number.

Mathematical Principle:
The multiplication table of a number n is a list of 
products of n with integers from 1 to a specified limit.

Pseudocode:
1. Read the number.
2. Read the limit.
3. Repeat from 1 to the limit.
4. Multiply the number by the current integer.
5. Print the result.
"""

number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

for i in range(1, limit + 1):
    print(f"{number} × {i} = {number * i}")


# === Specific Multiplication Tables ===

# First 12 multiples of 3
number = 3

for x in range(1, 13):
    number *= 1
    print(
f"{number} times {x} =", 
number * x)
    
# First 20 multiples of 5
number = 5

for x in range(1, 21):
    number *= 1
    print(
f"{number} times {x} =",
number * x)
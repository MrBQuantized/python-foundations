# ======================================
# Factorial and Fibonacci Sequence
# ======================================

# === Factorial of a number (n) ===
"""
Problem:
Calculate the factorial of a given number.

Mathematical Principle:
n! = 1 × 2 × 3 × ... × n

Pseudocode:
1. Read the number.
2. Set factorial = 1.
3. Repeat from 1 to the number.
4. Multiply factorial by the current number.
5. Print the final factorial.
"""

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)

# === Fibonacci sequence ===
"""
Problem:
Generate the Fibonacci sequence up to a given number of terms.

Mathematical Principle:
F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1

Pseudocode:
1. Read the number of terms.
2. Initialize the first two terms of the sequence.
3. Print the first two terms.
4. Generate and print the remaining terms of the sequence.
"""

number = int(input("Enter the number of terms: "))
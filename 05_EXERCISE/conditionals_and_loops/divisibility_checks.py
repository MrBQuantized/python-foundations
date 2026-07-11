# ======================================
# Divisibility Checks
# ======================================

# === Divisible by Number (n) ====
"""
Problem:
Check the divisibility of a number, N by divisor, n.

Mathematical Principle:
A number, N is divisible by a divisor, n if 
the remainder of the division is zero (0).

    N mod n = 0

Pseudocode:
1. Read the number.
2. Read the divisor.
3. Check if the number is divisible by the divisor.
4. Print the result.
"""



number = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

if number % divisor == 0:
    print(f"{number} is divisible by {divisor}")
else:
    print(f"{number} is not divisible by {divisor}")


number = int(input("Enter a number: "))


if number % 3 == 0:
    print(f"{number} is divisible by 3")
else:
    print(f"{number} is not divisible by ")
        
# === Divisible by 3 and 5 ====

number = int(input('Enter a number: '))

if number % (5 and 3) == 0:
    print(f"{number} is a divisible of 3 and 5")
else:
    print(f"{number} is not divisible by 3 and 5")


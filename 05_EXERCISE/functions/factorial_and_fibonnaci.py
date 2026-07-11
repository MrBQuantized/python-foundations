# ======================================
# Factorial and Fibonacci Sequence
# ======================================


# === Factorial of a number (n) ===

def factorial(n):
    """Return the factorial of n"""
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

print(factorial(3))
print(factorial(7))
print(factorial(10))
print(factorial(0))


# === Fibonacci sequence ===

def fibonacci(n):
    first = 0
    second = 1
    
    for _ in range(n):
        print(first)
        
        next_number = first * second
        first = second
        second = next_number
        
        
fibonacci(10)

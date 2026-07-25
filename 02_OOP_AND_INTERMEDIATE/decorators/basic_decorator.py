"""
Practice script for Python.

Topic: Decorators

Decorators add extra functionality to a function without modifying its
underlying code. A decorator is itself a function that takes another
function as an argument and returns a new function that wraps it.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: A Decorator as a Plain Function Call
# =================================================

# def mydecorator(function):
#     """Decorate a function, giving it extra functionality."""
#
#     def wrapper():
#         """Call the actual function with the added functionality."""
#         print("I am decorating your function!")
#         function()  # The original function is called here.
#
#     return wrapper  # mydecorator returns the function that calls the original one.

# def hello_world():
#     print("Hello World!")

# mydecorator(hello_world)()  # Adds the extra functionality to hello_world.

# This works, but it's not the Pythonic way to apply a decorator.

# =================================================
# Example 2: Using the @ Decorator Syntax
# =================================================

# @mydecorator
# def hello_world():
#     print('Hello World!')

# hello_world()  # Produces the same result as calling mydecorator(hello_world)().

# =================================================
# Example 3: Decorating a Function with Arguments
# =================================================
# If the function being decorated takes one or more arguments, the
# wrapper needs to accept arguments too. Using *args and **kwargs makes
# the wrapper universal, regardless of the decorated function's signature.

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        function(*args, **kwargs)

    return wrapper


@mydecorator
def hello(person):
    print(f"Hello {person}!")


hello("Richard")

# =================================================
# Example 4: Decorating a Function That Returns a Value
# =================================================
# If the decorated function returns a value, the wrapper needs to
# capture and return that value as well.

def mydecorator(function):

    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function")
        return return_value

    return wrapper


@mydecorator
def hello(person):
    return f"Hello {person}!"


print(hello("Richard"))
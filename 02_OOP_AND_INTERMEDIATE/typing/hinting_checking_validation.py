"""
Practice script for Python.

Topic: Type Hinting, Checking, and Validation

Type hinting is the declaration of expected data types for variables,
function parameters, and return values.

Type checking is static analysis that verifies declared types are used
consistently, catching mismatches before runtime. Python's `mypy` tool
performs this kind of check, but it doesn't enforce anything at runtime
and won't catch issues introduced by dynamic data.

Type validation is runtime verification that data meets certain
requirements, raising an error when it doesn't. This is where tools
like Pydantic come in, complementing what static type checking can't
catch.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Type Hinting
# =================================================

def create_user(first_name: str, last_name: str, age: int) -> dict:
    # Two string parameters and one int parameter are expected;
    # a dict is returned.
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    }


user1: dict = create_user("Blessing", "Onoh", "23")
print(user1)

# Python ignores these type hints at runtime, since they're just
# metadata — passing "23" as a string instead of an int still runs
# without error.

# =================================================
# Example 2: Type Checking
# =================================================
# To perform type checking:
#   1. Install mypy: pip install mypy
#   2. Run: mypy script_name.py
#      (replace "script_name" with the actual name of your script)
#
# mypy reports either "Success" or the specific type errors it found.


# =================================================
# Example 3: Type Validation
# =================================================

# === Manual Validation ===
# Example with correct code
# def create_user(first_name: str, last_name: str, age: int) -> dict:
#     # Two string parameters and one int parameter are expected;
#     # a dict is returned.
#     email = f"{first_name.lower()}_{last_name.lower()}@example.com"
#
#     # Validation
#     if not isinstance(first_name, str):
#         raise TypeError("first_name must be a string")
#     if not isinstance(last_name, str):
#         raise TypeError("last_name must be a string")
#     if not isinstance(age, int):
#         raise TypeError("age must be an integer")
#
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email,
#         "age": age
#     }

# user1: dict = create_user("Blessing", "Onoh", 25)  # Correct data types
# print(user1)

# Example with bad code
# user1: dict = create_user("Blessing", "Onoh", "Twenty")  # Incorrect data type for age
# print(user1)

# The downside of manual validation is the amount of repetitive code,
# which becomes harder to maintain as a function grows more complex.
# Pydantic solves this problem.

# === Validation with Pydantic ===
# With Pydantic, you only need to import the module and apply the
# decorator above the function. Pydantic uses the existing type hints
# to perform validation automatically.

# from pydantic import validate_call

# @validate_call
# def create_user(first_name: str, last_name: str, age: int) -> dict:
#     # Two string parameters and one int parameter are expected;
#     # a dict is returned.
#     email = f"{first_name.lower()}_{last_name.lower()}@example.com"
#
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email,
#         "age": age
#     }

# user1: dict = create_user("Blessing", "Onoh", 25)  # Correct data types
# print(user1)

# Example with bad code
# user1: dict = create_user("Blessing", "Onoh", "Twenty")  # Incorrect data type for age
# print(user1)
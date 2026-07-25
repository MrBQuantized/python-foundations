"""
Practice script for Python.

Topic: Type Hinting

Python is a dynamically typed language, meaning a variable's data type
doesn't need to be specified until runtime. Type hinting lets you add
type information to your code anyway, which helps with writing
self-documenting code, catching bugs earlier, and getting better IDE
auto-completions.

"Type hinting" and "type annotation" differ slightly but are commonly
used interchangeably.

Type hints should be treated like comments and documentation: useful
when used well, but not something to overuse.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Type Hinting Variables
# =================================================

name: str = 'Blessing'
age: int = 25


# =================================================
# Example 2: Type Hinting Function Parameters and Return Values
# =================================================

# def create_user(first_name: str, last_name: str, age: int | None = None) -> dict:
#     # The union (|) lets age be either an int or None.
#     email = f"{first_name.lower()}_{last_name.lower()}@example.com"
#     # This is obviously a string, so it doesn't need its own type hint.
#
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email,
#         "age": age
#     }

# user1 = create_user("Blessing", "Onoh", age=25)
# user2 = create_user("Denzel", "Washington", "65")
# print(user1)
# print(user2)


# =================================================
# Example 3: A More Specific Return Type
# =================================================
# We can be more specific about the return value's shape.

def create_user(
        first_name: str,
        last_name: str,
        age: int | None = None
) -> dict[str, str | int | None]:  # Keys are strings; values can be strings, integers, or None.
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    }

# With a more complicated dictionary, a return hint like this can get
# long and crowd the function signature. A type alias solves this.

# =================================================
# Example 4: Using a Type Alias
# =================================================
# A type alias creates a new name for an existing type, which can then
# be reused wherever that type is needed.

type User = dict[str, str | int | None]  # The `type` keyword marks this as a type alias.


def create_user(
        first_name: str,
        last_name: str,
        age: int | None = None
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    }

# Type aliases can be created for any type, not just dictionaries.
"""
Python script on decorator types

Decorators come in different forms, normal decorators, oop deccorators and 
api.

- Normal Python decorators modify or extend the behavior of a function or method. 
They modify or wrap a function's behavior (e.g., logging, timimg, authentication)
-  OOP decorators are designed to modify methods inside classes (e.g., @staticmethod, 
@classmethod, @property)
-  API route decorators are usually decorator factories. They take configuration (like URL
path), create a decorator, and use it to register your function with framework so it knows which code to run for each incoming requets
"""

# =====================================
# Normal Python Decorators
# =====================================

def logger(func):
    def wrapper(*arg1, **arg2):
        print("Starting...\n")
        function = func(*arg1, **arg2)
        print(function)
        return "Finished!"
    return wrapper

@logger
def greet(name, person):
    return f"👋  Hello! {name}. I'm {person}\n"

# print(greet("Blessing", person="Sandra Gomez"))

# =====================================
# OOP Decorators
# =====================================
# With decorator
class Student:
    @staticmethod
    def greet(name):    # No self is needed
        print(f"Hello, {name}")


# student = Student()
# student.greet("Michael")
# Student.greet("Micheal")

# Without decorator
class Student:
    
    def greet(self, name):    # self parameter is needed
        print(f"Hello! {name}")

# student = Student()
# student.greet("Michael")

# =====================================
# API route Decorators
# =====================================
# Let's assume FASTAPI were written in the manner below:

class App:
    @staticmethod
    def get(path):

        def decorator(func):
            print(f"Registered {path} → {func.__name__}")
            return func

        return decorator
    
# Create an instance of the class
app = App()

# Call its method
decorator = app.get("/users")    # calls app.get("/users")

# @decorator
# def get_users():
#     return ["Alice", "Bob"]

# Which is usually written as:
@app.get("/users")
def get_users():
    return ["Alice", "Bob"]


print(get_users())


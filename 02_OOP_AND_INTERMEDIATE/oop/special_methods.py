"""
Practice script for OOP.

Topic: Special Methods

Special methods (also called magic methods or dunder methods, since
they're surrounded by double underscores) let a class emulate built-in
Python behaviors and operators.

The constructor (__init__) is the most commonly used special method,
responsible for initializing new objects. Two other commonly used ones
are __repr__ and __str__.

By defining our own special methods, we can customize how built-in
functions and operators behave for our objects.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Without __repr__ or __str__
# =================================================
# Without these special methods, printing an object falls back to the
# default representation, which is not very informative.

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = (first + '.' + last + '@email.com').lower()
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # def __repr__(self):
    #     # Explicit representation of an object
    #     return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)   # a string that can be used to recreate the object.

    # def __str__(self):
    #     return '{} {}'.format(self.fullname(), self.email)


emp_1 = Employee('Daniel', 'Okafor', 60000)
emp_2 = Employee('Beethoven', 'Ludwig', 40000)

print(emp_1)  # Returns a vague, default object representation.


# =================================================
# Example 2: Adding __repr__ and __str__
# =================================================
# __repr__ provides an unambiguous representation aimed at developers
# (ideally something that could recreate the object).
# __str__ provides a readable representation aimed at end users.

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = (first + '.' + last + '@email.com').lower()
        self.pay = pay

    def fullname(self):
        return '{} - {}, '.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        """Return a string that can be used to create the same object."""
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        """Return the fullname and email of an employee."""
        return '{} {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        """Add the salaries of two employees."""
        return self.pay + other.pay

    def __len__(self):
        """Return the length of an employee's fullname."""
        return len(self.fullname())


emp_1 = Employee('Daniel', 'Okafor', 60000)
emp_2 = Employee('Beethoven', 'Ludwig', 40000)

# print() now uses the __str__ method instead of the default representation
print(emp_1)

# We can still access both methods directly
print(repr(emp_1))
print(str(emp_1))

# Alternatively, call them as regular methods
print(emp_1.__repr__())
print(emp_1.__str__())


# =================================================
# Example 3: Arithmetic Dunder Methods
# =================================================
# Built-in types implement arithmetic operators through dunder methods.
# Defining __add__ lets us apply the same operator to our own objects.

print(int.__add__(1, 2))       # Addition for numeric types
print(str.__add__('a', 'b'))   # Concatenation for strings

# Applying this to our Employee objects
print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))


# =================================================
# Example 4: The __len__ Method
# =================================================
# __len__ lets our object work with the built-in len() function.

print(len('test'))        # The number of characters in a container
print('test'.__len__())

# We can use it on our own object after defining
# the method in our class
print(len(emp_1))
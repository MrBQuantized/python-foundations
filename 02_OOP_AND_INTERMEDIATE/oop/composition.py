"""
Python Script on OOP — Covers Composition and Aggregation

Composition in Object-Oriented Programmming (OOP) is a relationship where one class contains 
another class as one of its memebers/contents. It represents a "has-a" or more explicitly, 
"part-of" relationship, and the contained object's lifetime depends on the container object. 
In fact, the object becomes an attribute of the container class.dfs

In simpler terms, composition may be regraded as a container class delegating some responsiblility 
to another class which becomes an object/member.

Aggregation on the other hand, also represents a "has-a" relationship, but unlike coomposition,
the contained object can exist independently of the object that uses it.

"""

# ==================================
# Composition
# ==================================

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)   # Salary is instantiated

    def total_salary(self):
        return self.obj_salary.annual_salary()

# We do not need to instantiate the Salary class because,
# it is created by the Employee class
# emp = Employee('Max', 25, 10000, 1000)
# print(emp.total_salary())

# ==================================
# Aggregation
# ==================================
# In this case we would replace the attribute of Salary() with
# a salary object in the constructor of the Employee class
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary   

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(10000, 1000)
emp = Employee("Max", 25, salary)

print(emp.total_salary())
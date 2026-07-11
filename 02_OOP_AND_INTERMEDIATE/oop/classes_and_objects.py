"""Practice script for OOP. 
Covers classes, objects
"""

# =================================================
# Understanding Classes and Objects
# =================================================
# Class — a blueprint for creating objects 
# It defines the methods or functions or attributes for objects.
# Object — an instance of a class


name = 'Blessing'
age = 25

print(type(name))  
print(type(age))   

# name object is made from class str
# age object is made from class int 

# -- Objects have different behaviors (methods) --
print(name.upper())       

# The .upper() method belongs to the string object.
# it changes the string to UPPERCASE


# ===================================================
# Creating a class
# ===================================================
class Dog:
    """Represents a simple dog. 
    """
    def bark(self):  
        """Print the dog's bark"""               
        print("Whoof!! whoof!")


# ===================================================
# Creating Objects
# ===================================================
dog1 = Dog()
dog1.bark()

# Create another object
dog2 = Dog()
dog2.bark()

# dog1 and dog2 are both Dog objects

# ===================================================
# Adding attributes (or data fields)
# ===================================================
class Dog:
    def __init__(self, name, breed):
        """Initialize the dog with a name and breed"""
        self.name = name
        self.breed = breed
    
    def bark(self):               
        print("Whoof!! whoof!")

# Creating objects and adding parameters while calling the class
dog1 = Dog("Macho", "Neapolitan Mastiff")
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Blue", "Cane Corso")
print(dog2.name)
print(dog2.breed) 

# The __init__() method is constructor — used in creating objects
# It is run only once when an object is created/instantiated  
# data fields (name & breed) are inserted into the init method. 
# These data fields allows us to pass unique data for each object created.

# ===================================================
# Creating different types of objects
# ===================================================
# Each dog has an owner and 
# Each owner has an address and phone number 

class Dog:
    def __init__(self, name, breed, owner):
        """Add Owner as an attribute """
        self.name = name
        self.breed = breed
        self.owner = owner
        
class Owner:
    def __init__(self, name, address, contact_number):
        """Initializes Owner with name, address and contact number""" 
        self.name = name
        self.address = address
        self.phone_number = contact_number          # you can use different names
        
owner1 = Owner("Favor", "No. 12 Umule Rd.", "555-444")
dog1 = Dog("Macho", "Neapolitan Mastiff", owner1)
print(dog1.owner.name)

owner2 = Owner("Christian", "N0. 8 Pentagon Estate", "888-999")
dog2 = Dog("Blue", "Cane Corso", owner2)
print(dog2.owner.name)

# We can define different kinds of objects
# and create relationships between different objects
# Methods are the functions defined inside of a class. 
# The define what function or behaviors a object can perform. Example bark()

# -- Self Parameter/keyword --
# This refers to the specific instance/object of the class itself
# It is used to access the attributes and methods of a specific object from inside of the class.


# ===================================================
# More examples
# ===================================================
# Person class
class Person:
    def __init__(self, name, age):
        """Initialize Person with name and age"""
        self.name = name
        self.age = age
    
    def greet(self):
        """Print the person's greet message"""
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


person1 = Person("Bruno", 30)
person1.greet()

person2 = Person("Chidimma", 15)
person1.greet()

# Each Person object displays a unique greeting based on it's attributes

# User class
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self, user):
        """Method contains user parameter. 
        You can say hi to another user
        """
        print(f"sending message to user {user.username}: Hi {user.username}, it's {self.username}")


user1 = User("altman", "alt@gmail.com", "123")
user2 = User("superman", "super@outlook.com", "abc")

# user1 says hi to user 2
user1.say_hi_to_user(user2)

# -- You can access data on an object using dot (.) notation  
print(user1.email)

# -- You can also crete a new value to the attributes
user1.email = "altman@gmail.com "
print(user1.email)

# The username will accept any value, but this is not what we want.
# We need a way to control how data on objects are accessed and modified.


# =================================================
# Accessing and Modifying Data
# =================================================
# The traditional way:
# make the data private/protected and use getters and setters

class User:
    def __init__(self, username, email, password):
        """underscore (_) prefix the attribute/data to signify that it's 
        for internal use only
        """
        self.username = username
        self._email = email         # email is protected
        self.password = password
    
    def get_email(self):
        return self._email



print(user1._email) 


# Let's see a better example
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        """Keep the email in lowercase and strip/remove the trailing and 
        leading whitespaces.
        """
        return self._email.lower().strip()

user1 = User("altman", " Alt@gmail.com ", "123")
print(user1._email)
print(user1.clean_email())

# Methods (like clean_email) are provided within the class for modifying 
# the email in a controlled way rather than for external usage.

# == The "Consenting Adults" Philosophy ==
# Developers are trusted to respect the convention in python of not 
# accessing underscore-prefixed methods or attributes


# However, double underscore (__) can be used enforce this rule.

class User:
    def __init__(self, username, email, password):
        """Double underscore (__) completely restricts external access
        """
        self.username = username
        self.__email = email            # email is private  
        self.password = password

    def clean_email(self):
        """Keep the email in lowercase and strip/remove the trailing and 
        leading whitespaces.
        """
        return self.__email.lower().strip()
    
user1 = User("altman", " Alt@gmail.com ", "123")
print(user1.__email) 


# =================================================
# Creating getter and setter methods.
# =================================================
# The convention is to prefix the method with "get_" for getters 
# or "set_" for setters. These methods provide controlled logic for
# reading and manipulating any data.

class User:
    def __init__(self, username, email, password):
        """Use single underscore (_) prefix to enable reading and changes
        """
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self):
        """Get the email"""
        return self._email
    
    def set_email(self, new_email):
        """Set/modify the email to any value"""
        self._email = new_email  

user1 = User("altman", " Alt@gmail.com ", "123")
print(user1.get_email())

user1.set_email("altman@outlook.com")
print(user1.get_email())

# We now have a controlled way of reading and modifying the email.
# Let's see an example where we want to know the time and date 
# an email address is being accessed. We need the datetime module

from datetime import datetime as dt

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self):
        """Get the date and time of access"""
        print(f"Email accessed at {dt.now()}")
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email  
        
        
user1 = User("altman", " Alt@gmail.com ", "123")
user1.set_email("altman@outlook.com")
print(user1.get_email())

# All kind of actions involving validation and manipulation
# can be contained within these function blocks. 

# =================================================
# More examples of setter and getter methods
# =================================================
# 1. Simple Validation check:
# set the email to the new_email if it contains the "@" symbol.

from datetime import datetime as dt
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self):
        """Get the date and time of access"""
        print(f"Email accessed at {dt.now()}")
        return self._email
    
    def set_email(self, new_email):
        """Set email if it contains '@'. Otherwise, do nothing"""
        if "@" in new_email:
            self._email = new_email    

user1 = User("altman", " Alt@gmail.com ", "123")
user1.set_email("cg234f556")
print(user1.get_email())

user1.set_email("cg234f@556.com")
print(user1.get_email())

# =================================================
# Getter and Setter Properties 
# =================================================
# These properties are the more python ways of 
# reading and manipulating data

# == Steps to creating property==
# 1. Make the attribute private by prefixing with single underscore
# 2. State the getter property decorator (@property) 
# 3. Create a method with the same name as the attribute we are creating the property for.
# 4. State the the setter property decorator  (@attribute.setter) 
# 5. Same as step 3
from datetime import datetime as dt

class User:
    def __init__(self, username, email, password): 
        self.username = username
        self._email = email
        self.password = password
        
    @property
    def email(self):      
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    

user1 = User("altman", " Alt@gmail.com ", "123")
user1.email = "this is not an email"
print(user1.email)


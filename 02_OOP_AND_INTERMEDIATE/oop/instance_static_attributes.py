"""Practice script for OOP. 
Covers static and instance attributes, their differences
and when to use each attribute.
"""

# =================================================
# Static Vs Instance Attributes
# =================================================
"""
# Static Attributes
====================
- A Static attribute (sometimes called a class attribute)
is an attribute that belongs to the class itself, not to any 
specific instance of the class.
- They are shared by all instances or objects
of the class.
- There is only one copy of a static attribute in memory regardless
of the number of instances or object created.
- They can be accessed by both their classes and instances. 
- Can be accessed with class name and attribute name.
- Ideal for storing default/constant data shared among all instances
E.g default configuration settings.

# Instance Attributes
======================
- They are created in the init method
- Unique to each instance created (i.e. Belong to specific instances)
- Ideal for storing object-specific data.
"""

class User:
    user_count = 0
    """static attribute initialized to zero"""
    
    def __init__(self, username, email):
        """Instance attributes created in the init method"""
        self.username = username
        self.email = email
        # Increment the static attribute by 1 whenever an object is created
        User.user_count += 1
        
    def display_user(self):
        """Display user info"""
        print(f"Username: {self.username}, Email: {self.email}")
        
user1 =User("Nathaniel", "nathan@gmail.com")
user2 =User("Emily", "emmy@gmail.com")


# print(User.user_count)
# print(user1.user_count)
# print(user2.user_count)

# Each instance can have a separate value of the static attribute
user1.user_count = 1
print(user1.__dict__)
print(user2.__dict__)
# print(User.user_count)
# print(user1.user_count)   
# print(user2.user_count)

# Only user1 has a user_count of 1
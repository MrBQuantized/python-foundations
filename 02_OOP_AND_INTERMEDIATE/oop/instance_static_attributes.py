"""
Practice script for OOP.

Topic: Static vs Instance Attributes

Static (class) attributes belong to the class and are shared by all
instances. They are useful for storing data common to every object.

Instance attributes belong to individual objects. They are usually
created in the __init__() method and store data unique to each instance.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
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
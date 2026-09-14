"""
Practice script for OOP. 

Topic: Class methods

Class methods are methods that belong to the class itself. 
It has `cls` rather than `self` and can  access class attributes and often used as an alternative constructor.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

class BankAccount:
    bank_name = "GTBank"

    def __init__(self, owner):
        self.owner = owner

    # Working with class-level data
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    # Creating an alternative constructor 
    @classmethod
    def from_string(cls, text):
        owner = text
        return cls(owner)


# ======================================
#  Example 1: Accessing a class Attribute
# ======================================
acc1 = BankAccount("Blessing") 
acc2 = BankAccount("Onoh") 

print(acc1.bank_name)
print(acc1.bank_name)
print()

# Change the name of the bank using the class method
BankAccount.change_bank_name("Access Bank")      

# Internally Python does: 
#   BankAccount.change_bank_account(BankAccount, "Access Bank")
#   So, inside the method cls = BankAccount

print(acc1.bank_name)
print(acc2.bank_name)
print()

# ======================================
#  Example 2: Alternative Constructor
# ======================================

acc3 = BankAccount("GTBank")
acc4 = BankAccount.from_string("Access Bank")

#  Internally, Python translates it to:
#   BankAccount.from_string(BankAccount, "Access Bank")
# 
# where: 
#      cls = BankAccount, and owner = text

print(type(acc3.owner))
print(acc3.owner)
print(acc4.owner)


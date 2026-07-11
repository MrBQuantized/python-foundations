"""Practice script for OOP. 
Covers Encapsulation principle
"""

# =================================================
# Encapsulation
# =================================================
""" 
Encapsulation is a fundamental principles of OOP which
involves bundling attributes, methods/behaviors together 
into a single unit called "Class" and restricting direct 
access to the internal data.
"""
# Bad example (No encapsulation)

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1  # Not an ideal. Clients shouldn't be allowed to set balances
print(account.balance)


# Encapsulation with getter property and conditionals

class BankAccount:
    def __init__(self):
        self._balance = 0.0   # fixed attribute
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        
        
# Create account object
account = BankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)

account.withdraw(100)    # Error. Can't withdraw more than balance
print(account.balance)

# The data is encapsulated within the class and Balance is inaccessible


# Including setter property to control/set balance

class BankAccount:
    def __init__(self):
        self._balance = 0.0    
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
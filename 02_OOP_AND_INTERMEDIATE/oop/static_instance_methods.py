"""Practice script for OOP. 
Covers static and instance methods, and private and protected methods .
"""

# =================================================
# Static Vs Instance Methods
# =================================================
"""
# Static Method
================
- A Static method in Python is a method that belongs to the class itself
rather than any instance of the class (It doesn't have `self`).
- To define a static method, we use the `@staticmethod` decorator
- Ideal for tasks related to class domain but not related to any 
specific instance. 
- Can be used for utility functions e.g interest rate, and also to 
format methods or process outputs independent of instances 

# Instance Method
================
- An Instance method works with specific objects and can access or 
modify it's attributes
- It has `self`.

Both methods are inside a class
"""

class BankAccount:
    MIN_BALANCE = 100   # Capitalize constants in python
    
    
    def __init__(self, owner, balance = 0):
        """Each instance has an owner and balance 
        initialized to zero (0)
        """
        self.owner = owner
        self._balance = balance  # Protected 
            
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

account = BankAccount("Fred", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(8))


# =================================================
# Creating Private and Protected Method
# =================================================
"""Private and protected methods are created in the same manner as 
with attributes.
Single underscore for protected methods and double underscores for 
private methods:    

    1. Private: __method(), 
    2. Protected: _method()
    
Protected methods may still be accessible outside of the class, but 
private methods are completely for internal use only. 
"""
class BankAccount:
    MIN_BALANCE = 100  
    
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance  # Protected 
            
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive")
            
    def _is_valid_amount(self, amount):
        """Validate the amount deposited and keep protected"""
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        """log the transaction type and amount and
        make private
        """
        print(f"logging {transaction_type} of ${amount}, New balance: ${self._balance}")
        
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
    
account = BankAccount("Fred", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(8))

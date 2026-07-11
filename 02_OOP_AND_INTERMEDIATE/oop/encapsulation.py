"""
Practice script for OOP.

Topic: Encapsulation

Encapsulation is one of the fundamental principles of object-oriented
programming (OOP). It involves bundling data (attributes) and behavior
(methods) into a single unit called a class while restricting direct
access to an object's internal data.

Tip:
This is a practice script. Feel free to comment out, uncomment, modify,
or add lines of code and rerun the script to observe how the output
changes.
"""

# =================================================
# Example 1: Without Encapsulation
# =================================================
# The balance attribute is fully exposed, so clients can set it to any
# value, including an invalid one like a negative balance.

class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBankAccount(0.0)
account.balance = -1  # Not ideal. Clients shouldn't be allowed to set an invalid balance.
print(account.balance)

# There's no validation and no way to prevent direct, unchecked
# modification of the balance.

# Let's refactor the code using encapsulation.


# =================================================
# Example 2: Encapsulation with a Getter Property
# =================================================
# The balance is stored in a "private" attribute (_balance) and exposed
# only through a read-only property. Deposits and withdrawals are
# validated before the balance is updated.

class BankAccount:
    def __init__(self):
        self._balance = 0.0  # Protected attribute

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


# Create account object
account = BankAccount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)

# Attempt to withdraw more than the balance
try:
    account.withdraw(100)  # Raises an error. Can't withdraw more than the balance.
except ValueError as error:
    print(f"Withdrawal failed: {error}")

print(account.balance)

# The balance is encapsulated within the class and can't be modified
# directly from outside it.


# =================================================
# Example 3: Adding a Setter Property
# =================================================
# A setter allows controlled modification of the balance through the
# same property interface, with validation applied on assignment.

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


# Create account object
account = BankAccount()
print(account.balance)
account.balance = 50  # Valid assignment, goes through the setter
print(account.balance)

# Attempt to set an invalid balance
try:
    account.balance = -10  # Raises an error. Balance cannot be negative.
except ValueError as error:
    print(f"Assignment failed: {error}")

print(account.balance)

# The setter still enforces validation, so invalid values are rejected
# even when assigning directly to the property.
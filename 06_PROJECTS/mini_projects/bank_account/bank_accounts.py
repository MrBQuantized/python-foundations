class BalanceException(Exception):
    pass
    
class BankAccount:
    def __init__(self, initalAccount, acctName):
        self.balance = initalAccount
        self.name = acctName
        print(f"\nAccount '{self.name} created.\nBalance = ${self.balance:.2f} ")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error}')
                
                
class InterestRewardAcct(BankAccount):
    """Inherits properties from BanKAccount"""
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)  # 5% interest
        print("\nDeposit complete.")
        self.getBalance()
        
        
class SavingsAcct(InterestRewardAcct):
    """Inherits Interest account with a new property, 'fee'"""
    def __init__(self, initalAccount, acctName):
        super().__init__(initalAccount, acctName)
        # % 5 Fee on any withdrawal
        self.fee =  5
        
    def withdraw(self, amount):
        """Overwrites the superclass' withdraw method"""
        try: 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
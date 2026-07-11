class Employee:
    
    raise_amount = 1.04   # Class variable
    
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = (first + last +".@company.com").lower()
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applyRaise(self):
        self.salary = int(self.salary * Employee.raise_amount)


emp1 = Employee("Micheal", "Smith", 50000)
emp2 = Employee("David", "Donald", 50000)

emp1.applyRaise()
print(emp1.salary)

print(emp1.email)
print(emp1.fullname())
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
Employee.fullname(emp2)



class Employee:
    
    raise_amount = 1.04   # Class variable
    
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = (first + last +".@company.com").lower()
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amount)   # `self.` and `Employee.`` do the same thing

emp1 = Employee("Micheal", "Smith", 50000)
emp2 = Employee("David", "Donald", 50000)

emp1.applyRaise()
print(emp1.salary)
print(emp1.__dict__)

# Increment of class variable
class Employee:
    
    number_of_emps = 0    # Initialized to zero
    raise_amount = 1.04   # Class variable
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = (first + last +".@company.com").lower()
        Employee.number_of_emps += 1   # Increases by 1 with each instance created
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amount)   

emp1 = Employee("Micheal", "Smith", 50000)
emp2 = Employee("David", "Donald", 50000)
print(Employee.number_of_emps)
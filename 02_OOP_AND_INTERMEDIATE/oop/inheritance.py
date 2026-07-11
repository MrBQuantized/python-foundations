"""Practice script for OOP. 
Covers Inheritance principle
"""

# =================================================
# Inheritance
# =================================================
""" 
Inheritance is fundamental concept in OOP that involves creating 
new classes (subclasses or derived classes) based on existing classes
(superclasses or base classes).

Subclasses inherit properties and behavior from superclasses and 
can also add new features or overwrite existing ones.

They are described in terms of a `-is-a` relationships:

    — A Car is-a Vehicle
    — A Bike is-a Vehicle
"""
# Creating a Base/Super Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")


# Creating a Car subclass
class Car(Vehicle):
    """Subclass of Vehicle"""
    
    def __init__(self, brand, model, year, number_of_doors, 
    number_of_wheels):
        """Inherits attributes from Vehicle and also
        adds new features
        """
        # Call the init function of the superclass
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
        
# Create a Bike subclass
class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
    
# Creating objects
car = Car("Toyota", "Corolla", 2023, 4, 4)
bike = Bike("Honda", "CBR500R", 2023, 2)
print(car.__dict__)  # dictionary attribute available to all python objects
print(bike.__dict__)

car.start()
bike.start()
    
        
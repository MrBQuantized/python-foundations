"""Practice script for OOP. 
Covers Polymorphism principle
"""

# =================================================
# Polymorphism
# =================================================
"""
Polymorphism is derived from Greek and means 'having multiple forms"

    Poly = many
    
    Morph = form 

In programming, polymorphism means the anility of an object to 
take many forms.
"""

class Car:
    
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors
        
    def start(self):
        print("Car is starting.")
        
    def stop(self):
        print("Car is stopping.")
        
class Motorcycle:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_bike(self):
        print("Motorcycle is starting.")
        
    def stop_bike(self):
        print("Motorcycle is stopping.")


# Creating list of vehicles to inspect
vehicles = [Car("Ford", "Mustang", 2024, 2),Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    # Check if object is a Car object
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    # Check if object is a Motorcycle object
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle")
    
"""
There's nothing shared or consistent between these two objects and
the codes will get uglier as we continue to add objects and conditional checks.

We can solve this issue with Polymorphism making.
"""
    
# Creating shared properties
"""
Let's make Car and Motorcycle subclasses that share properties by inheritance
belonging to a superclass `Vehicle`
"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Vehicle is starting.")
    
    def stop(self):
        print("Vehicle is stopping.")
        
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors   # car has a specific attribute
    
    # def start(self):
    #     print("Car is starting.")
    
    # def stop(self):
    #     print("Car is stopping.")
        

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)     # No specific attributes for motorcycle
    
    # def start(self):
    #     print("Motorcycle is starting.")
    
    # def stop(self):
    #     print("Motorcycle is stopping.")
        

vehicles = [Car("Ford", "Mustang", 2024, 2),Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    # Check if the object is an instance of Vehicle
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")    
    
# We can overwrite the methods from the superclass in order to create more specific 
# methods/implementations within each subclass

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Vehicle is starting.")
    
    def stop(self):
        print("Vehicle is stopping.")
        
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors   # car has a specific attribute
    
    def start(self):
        print("Car is starting.")
    
    def stop(self):
        print("Car is stopping.")
        

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)     # No specific attributes for motorcycle
    
    def start(self):
        print("Motorcycle is starting.")
    
    def stop(self):
        print("Motorcycle is stopping.")
        

vehicles = [Car("Ford", "Mustang", 2024, 2),Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    # Check if the object is an instance of Vehicle
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")    
    
"""   
Polymorphism treats Car and Motorcycles as instances of the base Vehicle 
class and the specific implementations of the start and stop methods are 
invoked dynamically within the loop
"""

# We can use type hinting in Python as well 
# Python now knows that the list only contains Vehicles
vehicles: list[Vehicle] = [
    Car("Ford", "Mustang", 2024, 2),
    Motorcycle("Yamaha", "YZF-R3", 2024)
]


# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    # No need to check the instances
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__}")
    vehicle.start()
    vehicle.stop()
    
# Now we do not have to worry about creating more properties 
# even if we add more objects/subclasses say a Plane

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Vehicle is starting.")
    
    def stop(self):
        print("Vehicle is stopping.")
        
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors   # car has a specific attribute
    
    def start(self):
        print("Car is starting.")
    
    def stop(self):
        print("Car is stopping.")
        

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)     
    
    def start(self):
        print("Motorcycle is starting.")
    
    def stop(self):
        print("Motorcycle is stopping.")

class Plane(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)     
    
    def start(self):
        print("Plane is starting.")
    
    def stop(self):
        print("Plane is stopping.")
        

vehicles: list[Vehicle] = [
    Car("Ford", "Mustang", 2024, 2),
    Motorcycle("Yamaha", "YZF-R3", 2024),
    Plane("Boeing" "747", "2021", 16)
]


# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    # No need to check the instances
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__}")
    vehicle.start()
    vehicle.stop()
    
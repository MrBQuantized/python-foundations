"""
Practice script for OOP.

Topic: Polymorphism

Polymorphism comes from the Greek words "poly" (many) and "morph"
(form), meaning "many forms."

In object-oriented programming (OOP), polymorphism allows different
objects to respond to the same method or operation in their own way.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Without Polymorphism
# =================================================
# Car and Motorcycle are unrelated classes with no shared interface.
# Inspecting them requires a separate conditional branch and separate
# method calls for each type.

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


# List of vehicles to inspect
vehicles = [Car("Ford", "Mustang", 2024, 2), Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through the list and inspect each vehicle
for vehicle in vehicles:
    # Check if the object is a Car
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    # Check if the object is a Motorcycle
    elif isinstance(vehicle, Motorcycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle")

# There's nothing shared or consistent between these two classes.
# As more vehicle types are added, the code becomes harder to maintain
# because of the growing number of conditional checks.

# Let's refactor the code using inheritance and polymorphism.


# =================================================
# Example 2: Introducing Inheritance
# =================================================
# Car and Motorcycle now inherit from a common Vehicle superclass,
# sharing the brand and model attributes and the start/stop methods.

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
        self.number_of_doors = number_of_doors  # Car has a specific attribute

    # def start(self):
    #     print("Car is starting.")

    # def stop(self):
    #     print("Car is stopping.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)  # No specific attributes for motorcycle

    # def start(self):
    #     print("Motorcycle is starting.")

    # def stop(self):
    #     print("Motorcycle is stopping.")


vehicles = [Car("Ford", "Mustang", 2024, 2), Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through the list and inspect each vehicle
for vehicle in vehicles:
    # Check if the object is an instance of Vehicle
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")

# Both subclasses currently fall back to the generic Vehicle
# start/stop methods, since neither one overrides them yet.


# =================================================
# Example 3: Method Overriding (Runtime Polymorphism)
# =================================================
# Override the inherited methods to provide subclass-specific
# implementations.

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
        self.number_of_doors = number_of_doors  # Car has a specific attribute

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)  # No specific attributes for motorcycle

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")


vehicles = [Car("Ford", "Mustang", 2024, 2), Motorcycle("Yamaha", "YZF-R3", 2024)]

# Loop through the list and inspect each vehicle
for vehicle in vehicles:
    # Check if the object is an instance of Vehicle
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")

# Polymorphism treats Car and Motorcycle as instances of the base
# Vehicle class, while the subclass-specific start/stop methods are
# invoked dynamically within the loop.

# Type hints can also be used here.
# Python now knows that the list only contains Vehicle instances,
# so the isinstance check is no longer necessary.
vehicles: list[Vehicle] = [
    Car("Ford", "Mustang", 2024, 2),
    Motorcycle("Yamaha", "YZF-R3", 2024)
]

# Loop through the list and inspect each vehicle
for vehicle in vehicles:
    # No need to check the instance type
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()


# =================================================
# Example 4: Extending the Hierarchy with Another Subclass
# =================================================
# Adding new vehicle types requires no changes to the inspection loop.

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
        self.number_of_doors = number_of_doors  # Car has a specific attribute

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
    Plane("Boeing", "747", 2021)
]

# Loop through the list and inspect each vehicle
for vehicle in vehicles:
    # No need to check the instance type
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
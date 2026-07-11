"""
Practice script for OOP.

Topic: Inheritance

Inheritance is one of the fundamental principles of object-oriented
programming (OOP). It allows new classes (subclasses or derived classes)
to be created from existing classes (superclasses or base classes).

A subclass inherits the attributes and methods of its superclass and
can also add new features or override existing ones.

Inheritance describes an "is-a" relationship.

Examples:
- A Car is a Vehicle.
- A Bike is a Vehicle.

Tip:
Experiment with the code by commenting, uncommenting, modifying, or
adding lines and rerunning the script to observe the results.
"""

# =================================================
# Example 1: Creating a Base/Superclass
# =================================================
# Vehicle defines the shared attributes and behavior that all vehicle
# types will inherit.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


# =================================================
# Example 2: Creating a Car Subclass
# =================================================
# Car inherits from Vehicle and adds its own attributes on top of the
# ones defined in the superclass.

class Car(Vehicle):
    """Subclass of Vehicle."""

    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        """Inherit attributes from Vehicle and add Car-specific attributes."""
        # Call the superclass's __init__ to set the shared attributes
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


# =================================================
# Example 3: Creating a Bike Subclass
# =================================================
# Bike also inherits from Vehicle, demonstrating that multiple
# subclasses can extend the same superclass in different ways.

class Bike(Vehicle):
    """Subclass of Vehicle."""

    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


# =================================================
# Example 4: Creating Objects and Using Inherited Behavior
# =================================================
# Both Car and Bike objects have access to the attributes and methods
# defined in Vehicle, in addition to their own subclass-specific ones.

car = Car("Toyota", "Corolla", 2023, 4, 4)
bike = Bike("Honda", "CBR500R", 2023, 2)

# __dict__ is a built-in attribute holding an object's instance
# attributes as a dictionary
print(car.__dict__)
print(bike.__dict__)

car.start()
bike.start()
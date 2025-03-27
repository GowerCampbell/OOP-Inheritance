# Knotes for Inheritance from Classes II (PowerPoint)
# Written by Gower Campbell

# -----------------------------------------------------------------------------
# Introduction to Inheritance
# -----------------------------------------------------------------------------

"""
Inheritance is one of the core pillars of Object-Oriented Programming (OOP).
It allows us to reuse code from existing classes (base class, subclass, superclass).
"""

# Principles of Inheritance:
"""
- Inherit attributes and methods from parent classes.
- Creates an organized structure (e.g., Animal -> Dog).
- Allows extensibility by adding unique traits without changing the base class.
"""

# Key Terminology:
"""
- Superclass (Parent/Base Class): The class being inherited from.
- Subclass (Child/Derived Class): The class inheriting from the superclass.
- Inheritance Hierarchy: A structure that shows the relationship between classes.
"""

# -----------------------------------------------------------------------------
# The __init__ Method
# -----------------------------------------------------------------------------

"""
The __init__ method initializes an object's attributes when it is created.
"""

# Example:
class Animal:
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def speak(self):
        return "animal sound"

    def eat(self):
        return "animal eating"

# -----------------------------------------------------------------------------
# The @staticmethod Decorator
# -----------------------------------------------------------------------------

"""
The @staticmethod decorator allows a method to be called without creating an
instance of the class. It does not require access to the instance (self) or
class (cls) parameters.
"""

# Example:
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))  # Output: 8

# -----------------------------------------------------------------------------
# Method Overriding
# -----------------------------------------------------------------------------

"""
Method overriding allows a subclass to provide a specific implementation of a
method that is already defined in its superclass.
"""

# Example:
class Dog(Animal):
    def speak(self):
        # Override the speak method
        return "barks"

my_dog = Dog(4)
print(my_dog.speak())  # Output: barks
print(f"My dog has {my_dog.number_of_legs} legs.")  # Output: My dog has 4 legs.

generic_animal = Animal(4)  # Creates an instance of the base class
print(generic_animal.speak())  # Output: animal sound

# -----------------------------------------------------------------------------
# The super() Function
# -----------------------------------------------------------------------------

"""
The super() function allows a subclass to call methods from its superclass.
It is used to extend the functionality of the parent class and avoid redundancy.
"""

# Example:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "makes a sound"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Calls Animal's __init__ to initialize 'name' and 'age'
        self.breed = breed  # Initializes the new "breed" attribute

    def speak(self):
        # Extending the method from the base class
        return super().speak() + " and barks"

# Example Usage
my_dog = Dog("Buddy", 5, "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.speak())  # Output: makes a sound and barks

# -----------------------------------------------------------------------------
# Demonstrating Python Inheritance
# -----------------------------------------------------------------------------

# Parent Class: Car
class Car:
    # Class variable for whether the engine is running or not
    is_running = False

    # Constructor that allows us to set the make and model as instance variables
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Method to start the engine
    def start_car(self):
        self.is_running = True

    # Method to turn off the engine
    def turn_off_car(self):
        self.is_running = False

    # Method to print the make and model
    def show_make_and_model(self):
        print(f"This vehicle is a {self.make} {self.model}")

# Subclass: PickupTruck
class PickupTruck(Car):
    # Additional class variable specific to the PickupTruck class
    is_loaded = False

    # Method to load the truck
    def load(self):
        self.is_loaded = True

    # Method to remove the load from the truck
    def unload(self):
        self.is_loaded = False

# Example Usage
pickup_truck_1 = PickupTruck("Toyota", "Hilux")
pickup_truck_1.load()  # Changes is_loaded from False to True
pickup_truck_1.start_car()  # Changes is_running from False to True

print(pickup_truck_1.is_running)  # Output: True
print(pickup_truck_1.is_loaded)  # Output: True
pickup_truck_1.show_make_and_model()  # Output: This vehicle is a Toyota Hilux

# -----------------------------------------------------------------------------
# Example of super() Function
# -----------------------------------------------------------------------------

# Parent Class: Computer
class Computer:
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Subclass: Laptop
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)  # Calls Computer's __init__
        self.model = model

# Example Usage
vivobook = Laptop('Asus', 8, 512, 'Vivobook')
print('Computer make: ', vivobook.computer)  # Output: Asus
print('Computer model:', vivobook.model)  # Output: Vivobook
print(f"This computer has {vivobook.ram} GB of RAM.")  # Output: This computer has 8 GB of RAM.
print(f"This computer has {vivobook.ssd} GB of SSD storage.")  # Output: This computer has 512 GB of SSD storage.

# -----------------------------------------------------------------------------
# Example of Method Overriding
# -----------------------------------------------------------------------------

# Parent Class: Father
class Father:
    def transport(self):
        print("The transport used is a car")

    def action(self):
        print("Dad teaching son to ride a bicycle")

# Subclass: Son
class Son(Father):
    def transport(self):
        print("The transport used is a bicycle")

    def action(self):
        print("Son is riding a bicycle.")

# Example Usage
son_1 = Son()
son_1.transport()  # Output: The transport used is a bicycle
son_1.action()  # Output: Son is riding a bicycle.

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

"""
- Inheritance allows code reuse and extensibility by inheriting attributes and methods from a superclass.
- Method overriding enables a subclass to provide a specific implementation of a method.
- The super() function allows a subclass to access and extend the functionality of its superclass.
- Inheritance promotes organized and modular code design.
"""


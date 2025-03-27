# Learning Objectives & Outcomes
# Written by Gower Campbell

# -----------------------------------------------------------------------------
# Inheritance
# -----------------------------------------------------------------------------

"""
Inheritance allows us to create a new class with all the properties and attributes
of a base class, enabling code reuse and extensibility.
"""

# Key Concepts:
"""
- Parent/Base Class/Superclass: 
Contains all attributes and properties to inherit.
- Child/Subclass/Derived Class: 
Inherits all attributes and properties of the parent class.
"""

# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Call the parent class constructor
        self.grades = []

# -----------------------------------------------------------------------------
# Method Overriding
# -----------------------------------------------------------------------------

"""
Method overriding allows a subclass to provide a specific implementation of a method
that is already defined in its superclass. This can be used to extend or change the
behavior of the method.
"""

# Example:
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Usage
dog = Dog()
print(dog.speak())  # Output: Bark

# Extending functionality using `super()`
class Cat(Animal):
    def speak(self):
        return super().speak() + " and Meow"

# Usage
cat = Cat()
print(cat.speak())  # Output: Animal sound and Meow

# -----------------------------------------------------------------------------
# Multiple Inheritance
# -----------------------------------------------------------------------------

"""
Python allows multiple inheritance, where a subclass can inherit attributes and
properties from more than one base class. The method resolution order (MRO) determines
the order in which parent classes are searched for methods.
"""

# Example:
class Teacher:
    def teach(self):
        return "Teaching"

class Researcher:
    def research(self):
        return "Conducting research"

class Professor(Teacher, Researcher):
    pass

# Usage
prof = Professor()
print(prof.teach())  # Output: Teaching
print(prof.research())  # Output: Conducting research

# -----------------------------------------------------------------------------
# Special Methods (Magic Methods)
# -----------------------------------------------------------------------------

"""
Special methods (also called magic methods) allow us to define custom behavior for
Python's built-in operations, such as object instantiation, string representation,
and operator overloading.
"""

# Example: `__init__` for Instantiation
class Student:
    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average

# Example: `__str__` for String Representation
class Student:
    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average

    def __str__(self):
        return f"Student: {self.fullname}, ID: {self.student_number}, Average Grades: {self.average}"

# Usage
student_1 = Student("Jacob", "ADBB&*&", 87)
print(student_1)  # Output: Student: Jacob, ID: ADBB&*&, Average Grades: 87

# Example: Operator Overloading with `__add__`
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

# Usage
x = Number(10)
y = Number(30)
result = x + y
print(result)  # Output: 40

# Example: Comparator Methods with `__gt__`
class Student:
    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average

    def __gt__(self, other):
        return self.average > other.average

# Usage
student_1 = Student("Jacob", "ADBB&*&", 87)
student_2 = Student("Alex", "ACCCCCC", 86)
print(student_1 > student_2)  # Output: True

# -----------------------------------------------------------------------------
# Container-Like Objects
# -----------------------------------------------------------------------------

"""
Special methods can be used to make objects behave like containers, supporting
operations such as indexing, iteration, and length calculation.
"""

# Example: `__getitem__` for Indexing
class CustomContainer:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")
        return self.items[index]

# Usage
container = CustomContainer(['apple', 'banana', 'orange'])
print(container[0])  # Output: apple
print(container[1])  # Output: banana
print(container[2])  # Output: orange
# Uncommenting the following line raise an IndexError
# print(container[3]) # IndexError: Index out of range

'Special Methods Addressing Container-like objects'

# Length -> __len__(self)
# Get Item ->  __getitem__(self, key)
# Set Item -> __setitem__(self, key, item)
# Contains -> __Contains__(self, item)
# Iterator -> __Iter__(self)
# Next -> __Next__(self)

# Example: `__len__` for Length
class CustomContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Usage
container = CustomContainer(['apple', 'banana', 'orange'])
print(len(container))  # Output: 3

# Example: `__setitem__` for Setting Items
class CustomContainer:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")
        self.items[index] = value

# Usage
container = CustomContainer(['apple', 'banana', 'orange'])
container[1] = 'grape'  # Modify the item at index 1
print(container[1])  # Output: grape

# Example: `__contains__` for Membership Testing
class CustomContainer:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

# Usage
container = CustomContainer(['apple', 'banana', 'orange'])
print('banana' in container)  # Output: True
print('grape' in container)  # Output: False


# Example: `__iter__` and `__next__` for Iteration
class CustomContainer:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item

# Usage
container = CustomContainer(['apple', 'banana', 'orange'])
for item in container:
    print(item)  # Output: apple, banana, orange



# -----------------------------------------------------------------------------
# Lesson Conclusion
# -----------------------------------------------------------------------------

# Inheritance allows a subclass to inherit attributes and methods from a superclass, enabling
# code reuse and structured organisation.

# Superclass and Subclass: The superclass (parent) provides the inherited properties, while the
# subclass (child) extends or modifies them.

# Method Overriding: Subclasses can override inherited methods to provide specific
# implementations, allowing customization.

# super(): The super() function allows subclasses to call methods from the superclass, often
# used in constructors or overridden methods.

# Benefits: Inheritance simplifies code by reusing functionality, enhancing extensibility, and
# # maintaining a clear hierarchy.

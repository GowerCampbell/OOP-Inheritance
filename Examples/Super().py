# Demonstrating the Use of `super()` in Python with Detailed Explanations

# -----------------------------------------------------------------------------
# Basic Example of `super()` in Single Inheritance
# -----------------------------------------------------------------------------

class Parent:
    def __init__(self, name):
        """Constructor of Parent class."""
        self.name = name
        print(f"Parent initialized with name: {self.name}")

    def greet(self):
        """Method of Parent class."""
        print(f"Hello from {self.name}, the Parent!")

class Child(Parent):
    def __init__(self, name, age):
        """Constructor of Child class."""
        # Calling the constructor of the Parent class using `super()`
        super().__init__(name)  # This calls Parent.__init__(self, name)
        self.age = age
        print(f"Child initialized with age: {self.age}")

    def greet(self):
        """Method of Child class."""
        # Calling the `greet` method of the Parent class using `super()`
        super().greet()  # This calls Parent.greet(self)
        print(f"Hello from {self.name}, the Child, aged {self.age}!")

# Creating an instance of Child
child = Child("John", 12)
child.greet()  # Calls greet method of Child, which also calls Parent.greet()

# -----------------------------------------------------------------------------
# Multiple Inheritance Example
# -----------------------------------------------------------------------------

print("\n--- Multiple Inheritance Example ---")

class A:
    def greet(self):
        """Method of Class A."""
        print("Hello from Class A")

class B:
    def greet(self):
        """Method of Class B."""
        print("Hello from Class B")

# C inherits from both A and B
class C(A, B):
    def greet(self):
        """Method of Class C."""
        # `super()` follows the MRO (Method Resolution Order) to call the greet method
        super().greet()  # This calls A.greet() because of the MRO (C -> A -> B)
        print("Hello from Class C")

# Creating an instance of Class C
obj = C()
obj.greet()  # Calls greet from Class A, then from Class C

# -----------------------------------------------------------------------------
# Using `super()` to Call Parent Constructor in Multiple Inheritance
# -----------------------------------------------------------------------------

print("\n--- Using super() to Call Parent Constructor in Multiple Inheritance ---")

class D:
    def __init__(self, value):
        """Constructor of Class D."""
        self.value = value
        print(f"D initialized with value: {self.value}")

class E:
    def __init__(self, name):
        """Constructor of Class E."""
        self.name = name
        print(f"E initialized with name: {self.name}")

# F inherits from both D and E
class F(D, E):
    def __init__(self, value, name):
        """Constructor of Class F."""
        # Using `super()` to call constructors of both parent classes
        super().__init__(value)  # This calls D.__init__(self, value)
        E.__init__(self, name)  # Manually calling E's __init__ as part of initialization

# Creating an instance of Class F
obj_f = F(42, "Example")
print(f"Object F: value={obj_f.value}, name={obj_f.name}")

# -----------------------------------------------------------------------------
# Method Resolution Order (MRO) in Action
# -----------------------------------------------------------------------------

print("\n--- Method Resolution Order (MRO) ---")

class X:
    def hello(self):
        """Method of Class X."""
        print("Hello from X")

class Y(X):
    def hello(self):
        """Method of Class Y."""
        super().hello()  # Calls X's hello
        print("Hello from Y")

class Z(Y):
    def hello(self):
        """Method of Class Z."""
        super().hello()  # Calls Y's hello, which in turn calls X's hello
        print("Hello from Z")

# Creating an instance of Class Z
obj_z = Z()
obj_z.hello()  # This calls hello from Z, then Y, then X, in this order

# -----------------------------------------------------------------------------
# Demonstrating Method Resolution Order (MRO) in Multiple Inheritance
# -----------------------------------------------------------------------------

print("\n--- Demonstrating Method Resolution Order (MRO) in Multiple Inheritance ---")

class P:
    def greet(self):
        """Method of Class P."""
        print("Greetings from Class P")

class Q:
    def greet(self):
        """Method of Class Q."""
        print("Greetings from Class Q")

class R(P, Q):
    def greet(self):
        """Method of Class R."""
        super().greet()  # This calls P.greet because of MRO (R -> P -> Q)
        print("Greetings from Class R")

# Creating an instance of Class R
obj_r = R()
obj_r.greet()  # Calls greet from P, then R

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

"""
- `super()` is used to call methods from the parent class in inheritance.
- In single inheritance, `super()` directly calls the parent class's method.
- In multiple inheritance, `super()` follows the Method Resolution Order (MRO).
- MRO determines the order in which parent classes are searched for methods.
- `super()` is particularly useful for avoiding redundancy and maintaining clean code.
"""

# Demonstrating the Use of `*args` and `**kwargs` in Python

# -----------------------------------------------------------------------------
# Introduction to `*args` and `**kwargs`
# -----------------------------------------------------------------------------

"""
`*args` and `**kwargs` are special syntax in Python used to pass a variable number of arguments to a function.

- `*args`: Allows you to pass a variable number of positional arguments to a function.
  It collects all positional arguments into a tuple.

- `**kwargs`: Allows you to pass a variable number of keyword arguments to a function.
  It collects all keyword arguments into a dictionary.
"""

# -----------------------------------------------------------------------------
# Example of `*args`
# -----------------------------------------------------------------------------

# Without `*args`, you need to define a fixed number of parameters.
def add(num_1, num_2, num_3):
    total = num_1 + num_2 + num_3
    return total

print(f"Add (without *args): {add(1, 2, 3)}")  # Output: Add (without *args): 6

# With `*args`, you can pass any number of positional arguments.
def add_with_args(*args):
    total = sum(args)  # `args` is a tuple containing all positional arguments
    return total

print(f"Add (with *args): {add_with_args(1, 2, 3, 4, 5)}")  # Output: Add (with *args): 15

# -----------------------------------------------------------------------------
# Example of `**kwargs`
# -----------------------------------------------------------------------------

# Without `**kwargs`, you need to define a fixed number of keyword parameters.
def add_with_kwargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value  # `kwargs` is a dictionary containing all keyword arguments
    return total

print(f"Add (with **kwargs): {add_with_kwargs(num_1=1, num_2=2, num_3=3, num_4=4)}")  # Output: Add (with **kwargs): 10

# -----------------------------------------------------------------------------
# Combining `*args` and `**kwargs`
# -----------------------------------------------------------------------------

# You can use both `*args` and `**kwargs` in the same function to handle both
# positional and keyword arguments.

def combined_example(*args, **kwargs):
    print(f"Positional arguments (*args): {args}")  # Prints all positional arguments as a tuple
    print(f"Keyword arguments (**kwargs): {kwargs}")  # Prints all keyword arguments as a dictionary

# Example usage
combined_example(1, 2, 3, name="John", age=25)
"""
Output:
Positional arguments (*args): (1, 2, 3)
Keyword arguments (**kwargs): {'name': 'John', 'age': 25}
"""

# -----------------------------------------------------------------------------
# Practical Use Cases
# -----------------------------------------------------------------------------

"""
1. Flexible Function Definitions:
   - Use `*args` and `**kwargs` when you want to create functions that can handle
     a variable number of inputs.

2. Wrapper Functions:
   - Use `*args` and `**kwargs` in wrapper functions to pass arguments to the
     wrapped function without knowing the exact signature.

3. Decorators:
   - Use `*args` and `**kwargs` in decorators to make them work with any function,
     regardless of the number of arguments.
"""

# Example: Wrapper Function
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

print(f"Multiply (with logger): {multiply(3, 4)}")
"""
Output:
Calling function multiply with args: (3, 4), kwargs: {}
Function multiply returned: 12
Multiply (with logger): 12
"""

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

"""
- `*args` is used to pass a variable number of positional arguments to a function.
- `**kwargs` is used to pass a variable number of keyword arguments to a function.
- Both `*args` and `**kwargs` make functions more flexible and reusable.
- They are commonly used in wrapper functions, decorators, and other scenarios
  where the number of arguments is not known in advance.
"""

# End of File

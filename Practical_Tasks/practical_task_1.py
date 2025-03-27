# Learning Objectives:
# ---------------------
# 1. Understand and apply inheritance in Python.
# 2. Learn to use different class attributes and methods.
# 3. Implement here subclassing to create a specialised course for OOP.
# 4. Gain the ability to use constructor methods and method overriding.
# 5. Understand how to generate my unique IDs for each course

# Written by: Gower Campbell & Cogrammer


# A Base class for the course:
class Course:
    # My Class attributes:
    name = "\nFundamentals of Computer Science"
    contact_website = "\nwww.hyperiondev.com"
    address = "\nCape Town"

    # My Instance initializer:
    def __init__(self, name):
        self.name = name

    # A method to display contact details.
    def contact_details(self):
        return f"""\nPlease contact us by visiting our website:
        {self.contact_website}"""

    # The method to display head office location.
    def head_office_location(self):
        print("\nHead office location:", self.address)


# Subclass for the Object-Oriented Programming course.
class OOPCourse(Course):
    _current_id = 12345

    def __init__(self, name, description, trainer):
        super().__init__(name)  # Inherit properties from the Course class
        self.description = description  # Set course description
        self.trainer = trainer  # Set trainer name
        self.course_id = self._generate_unique_id()  # Generate a unique ID

    @classmethod
    def _generate_unique_id(cls):
        unique_id = cls._current_id  # Accessing the current unique ID
        cls._current_id += 1  # Increment this unique ID for the next course
        return f"\n#{unique_id}"  # Returns the ID in the correct format

    def trainer_details(self):
        print(f"""\nThis course is about {self.description} and it is 
taught by {self.trainer}.""")

    def show_course_id(self):
        print(f"\nThe course ID is: {self.course_id}")

# Example usage:
course = Course("Intro to Programming")
print(course.contact_details())
course.head_office_location()

course_1 = OOPCourse("OOPCourse", "OOP Fundamentals", "Mr Anon A. Mouse")
print(course_1.contact_details())
course_1.trainer_details()
course_1.show_course_id()

# Reflection:
# -----------
# Through this practical_task_1, I gained a deeper understanding of OOP
# programming, and techniques you can use to apply class attributes like 
# _current_id to generate unique identifiers for different instances. 

# I learned how to leverage the super() function to inherit attributes 
# from the parent class and extend them in the subclass. Additionally, 
# I developed methods specific to the subclass, such as the trainer_details
# and show_course_id, and explored method overriding to customise inherited
# behaviour. 

# This overall, reinforced my knowledge of inheritance, encapsulation, and method 
# customisation, which are very key to writing modular, reusable, and maintainable 
# code in Python.

"""
Bibliography:
-------------
- Python Documentation - 
     Classes: https://docs.python.org/3/tutorial/classes.html
- Python Documentation - 
     Methods: https://docs.python.org/3/tutorial/classes.html#methods
- Tabulate Library: 
     https://pypi.org/project/tabulate/
- Python's Official Dictionary: 
     https://docs.python.org/3/library/functions.html
"""

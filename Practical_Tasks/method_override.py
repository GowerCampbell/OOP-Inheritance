# Learning Objectives:
# - Understand inheritance and method overriding in Python classes.

# - Learn how to validate user input and handle exceptions using try & except.

# - Explore the use of class attributes and instance methods.

# - Apply conditional logic to classify users based on age.

# Written by: Gower Campbell

class Person:
    """
    A class to represent a person and validate their attributes.

    Attributes:
        VALID_EYE_COLORS (set): A set of valid eye colors.
        VALID_HAIR_COLORS (set): A set of valid hair colors.
    """
    VALID_EYE_COLORS = {
        "blue", "brown", "green", "hazel", "gray", "amber"} # Valid eye colors
    VALID_HAIR_COLORS = {
        "black", "brown", "blonde", "red", "gray", "white"} # Valid hair colors

    def __init__(self, name, age, eye_color, hair_color):
        """
        Initializes an instance of the Person class with basic attributes.

        :param name: The name of the person.
        :param age: The age of the person.
        :param eye_color: The eye colour of the person.
        :param hair_color: The hair colour of the person.
        """
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        """
        Placeholder method meant to be overridden in subclasses (Adult, Child).
        """
        raise NotImplementedError(
            """\nThis method should be overridden in subclasses.""")

    def display_info(self):
        """
        Displays the character's information in a formatted way.
        """
        print("\n--- Character Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Eye Color: {self.eye_color.capitalize()}")
        print(f"Hair Color: {self.hair_color.capitalize()}")
        self.can_drive()  # Display driving eligibility
        print("-----------------------------")


class Adult(Person):
    def can_drive(self):
        """
        Overridden method for adults.
        Prints a message indicating that the adult is old enough to drive.
        """
        print(f"\n{self.name} is Old enough to Drive.")


class Child(Person):
    def can_drive(self):
        """
        Overridden method for children.
        Prints a message indicating that the child is too young to drive.
        """
        print(f"\n{self.name} is too Young to Drive.")


def get_valid_age():
    """
    Prompts the user to input their age and validates it.
    Ensures the age is a non-negative integer.

    :return: A valid age (integer >= 0).
    """
    valid_age = False
    while not valid_age:
        try:
            age = int(input("\nPlease input your age: "))  #Input an age
            if age < 0:
                raise ValueError("\nAge cannot be negative.")
            # Validation for non-negative age
            valid_age = True
            return age
        except ValueError as e:
            print(f"\nInvalid input: {e}")  # Error message for invalid input


def get_valid_string(prompt):
    """
    Prompts the user for a valid string input (only letters).

    :param prompt: The prompt message displayed to the user.
    :return: A valid string.
    """
    valid_string = False
    while not valid_string:
        value = input(prompt).strip()  # Get and strip input
        if value.isalpha():  # Check if the string contains only letters
            valid_string = True
            return value
        print("\nInvalid input. Please enter only letters.")


def get_valid_color(prompt, valid_colors):
    """
    Prompts the user for a colour and validates it against a set of allowed colours.

    :param prompt: The prompt message displayed to the user.
    :param valid_colors: A set of valid colour options.
    :return: A valid colour from the set.
    """
    valid_color = False
    while not valid_color:
        value = input(prompt).strip().lower()  # Get and format input
        if value in valid_colors:  # Validate colour
            valid_color = True
            return value
        print(f"""Invalid input: Please enter one of the following: {', '.join(
            valid_colors)}.""")


def display_menu():
    """
    Displays the character creation menu options.
    """
    print("\n--- Character Creation Menu ---")
    print("1. View Character Information")
    print("2. Confirm and Finalize Character")
    print("3. Exit")
    print("-------------------------------")


def main():
    """
    Main function to handle character creation and menu navigation.
    """
    # Character Creation
    print("\n<-------- Character Creation -------->")
    name = get_valid_string("\nPlease input your name: ")  
    age = get_valid_age()  
    eye_color = get_valid_color(
        """\nPlease input an eye color: """, Person.VALID_EYE_COLORS)
    hair_color = get_valid_color(
        """\nPlease input a hair color: """, Person.VALID_HAIR_COLORS) 

    # Determine if the person is an Adult or Child based on their age
    if age >= 18:
        person = Adult(name, age, eye_color, hair_color) # Adult Object
    else:
        person = Child(name, age, eye_color, hair_color) # Child Object

    # Menu loop
    running = True
    while running:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            # Display character information
            person.display_info()
        elif choice == "2":
            # Confirm and finalize character
            print("\n--- Character Finalized ---")
            person.display_info()
            print("Thank you for creating your character!")
            running = False  # Exit the loop
        elif choice == "3":
            # Exit the program
            print("\nExiting character creation. Goodbye!")
            running = False  # Exit the loop
        else:
            print("Invalid choice. Please select a valid option (1-3).")


# Run the program
if __name__ == "__main__":
    main()

#----- My Reflections ------

# I learned how inheritance and method overriding can work together when using
# classes from my studies to create both an Adult and Child subclass within the
# base class Person that will inherit its attributes and methods. The program I
# developed imcludes functions to determines whether the user should be able to
# drive through uncorperating try and execept blocks to handle validation and 
# ensure that I can collect a range of information, while tailoring the outputs
# based on the users age or color preference without risking a stack overflow.

"""
# Bibliography:
# - Python Inheritance: 
#   https://docs.python.org/3/tutorial/classes.html#inheritance
# - Python Exception Handling:
#   https://docs.python.org/3/tutorial/errors.html
# - Method Overriding Concepts: 
#   https://realpython.com/python-super/"
"""

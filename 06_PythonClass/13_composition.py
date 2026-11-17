
'''
Composition:
Composition is an OOP concept where one class contains
an object of another class as an attribute.

It represents a "has-a" relationship.
For example, a Student has a Laptop.
'''


# Component class representing a laptop
class Laptop:

    # Initialize the laptop's attributes
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    # Display laptop details
    def display_details(self):
        print(f"Laptop brand: {self.brand}")
        print(f"RAM: {self.ram} GB")


# Main class that contains a Laptop object
class Student:

    # Student has a laptop, demonstrating composition
    def __init__(self, name, age, laptop):
        self.name = name
        self.age = age
        self.laptop = laptop

    # Display the student's details
    def display_student(self):
        print(f"Student name: {self.name}")
        print(f"Age: {self.age}")

    # Delegate laptop details to the Laptop object
    def display_laptop(self):
        self.laptop.display_details()


# Create a Laptop object
laptop1 = Laptop("Acer", 8)

# Pass the Laptop object into the Student object
student1 = Student("Shishir", 25, laptop1)

# Display student information
student1.display_student()

# Display laptop information through the Student object
print("\n=== Laptop Details ===")
student1.display_laptop()

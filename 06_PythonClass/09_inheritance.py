
# Parent class/Base class
class Student:

    # Class attribute shared by students unless overridden on an instance
    university = "Bishop's University"

    # Constructor initializes each student's instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method displays the student's details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")

    # Instance method introduces the student
    def introduce(self):
        print(f"My name is {self.name}. I am a student.")


# Child class inherits attributes and methods from Student
class Graduate(Student):

    # Child constructor adds a research topic to the inherited attributes
    def __init__(self, name, age, research_topic):
        # super() calls the parent constructor to initialize name and age
        super().__init__(name, age)
        self.research_topic = research_topic

    # Child-specific method displays the graduate student's research topic
    def display_research(self):
        print(f"Research topic: {self.research_topic}")

    # Method overriding provides a specialized introduction
    def introduce(self):
        print(f"My name is {self.name}. I am a graduate student.")

    # Overridden behavior can be extended using the parent's method
    def display_all_details(self):
        super().display_details()
        self.display_research()


# Create an object of the parent class
student1 = Student("Rahim", 21)

# Create an object of the child class
graduate1 = Graduate(
    "Shishir",
    25,
    "Predicting brain structure from lifestyle data"
)

# Call the inherited parent method on a parent object
print("=== Regular Student ===")
student1.display_details()
student1.introduce()

# Call inherited and child-specific methods on a graduate object
print("\n=== Graduate Student ===")
graduate1.display_all_details()
graduate1.introduce()

# Demonstrate that the child inherits the parent's class attribute
print("\n=== University ===")
print(graduate1.university)

# Demonstrate that a child can override a class attribute on its class
Graduate.university = "McGill University"
print(graduate1.university)  # McGill University
print(student1.university)   # Bishop's University

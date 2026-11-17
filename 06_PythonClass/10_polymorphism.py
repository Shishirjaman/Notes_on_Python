'''
Polymorphism means "many forms."

It allows different objects to use the same method name
but behave differently depending on their class.

Here, Student, GraduateStudent, and PhDStudent all have
an introduce() method, but each class produces different output.

Python automatically calls the appropriate method for each object.

'''

# Parent class/base class
class Student:

    # Class attribute shared by students unless overridden
    university = "Bishop's University"

    # Constructor initializes each student's instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method that child classes can override
    def introduce(self):
        print(f"My name is {self.name}. I am a student.")

    # Displays the student's basic details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")


# Child class inherits attributes and methods from Student
class GraduateStudent(Student):

    # Constructor adds a research topic to the inherited attributes
    def __init__(self, name, age, research_topic):
        # Initialize name and age using the parent constructor
        super().__init__(name, age)
        self.research_topic = research_topic

    # Override the parent's method to provide specialized behavior
    def introduce(self):
        print(
            f"My name is {self.name}. "
            "I am a graduate student."
        )

    # Child-specific method displays the research topic
    def display_research(self):
        print(f"Research topic: {self.research_topic}")


# Another child class inherits from Student
class PhDStudent(Student):

    # Constructor adds a research area
    def __init__(self, name, age, research_area):
        # Reuse the parent's constructor
        super().__init__(name, age)
        self.research_area = research_area

    # Override the same method with different behavior
    def introduce(self):
        print(
            f"My name is {self.name}. "
            "I am a PhD student."
        )

    # Child-specific method displays the research area
    def display_research(self):
        print(f"Research area: {self.research_area}")


# Create objects of different classes
student1 = Student("Rahim", 21)
graduate1 = GraduateStudent(
    "Shishir",
    25,
    "Predicting brain structure from lifestyle data"
)
phd1 = PhDStudent("Karim", 28, "Artificial Intelligence")


# Store different object types in one list
students = [student1, graduate1, phd1]


# Polymorphism: call the same method on different objects
for student in students:
    student.introduce()


# Display the details of each student using inherited behavior
print("\n=== Student Details ===")
for student in students:
    student.display_details()


# Call child-specific methods on the appropriate objects
print("\n=== Research Details ===")
graduate1.display_research()
phd1.display_research()

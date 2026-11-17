
'''
Aggregation:
Aggregation is an OOP relationship where one class
contains or uses objects of another class.

The contained objects can exist independently of
the container object.

Example: A University has Students, but Students
can exist even if the University object is removed.
'''


# Independent class representing a student
class Student:

    # Initialize the student's attributes
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    # Display the student's information
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")


# University class aggregates Student objects
class University:

    # Receive existing student objects
    def __init__(self, name, students):
        self.name = name
        self.students = students

    # Display university information
    def display_university(self):
        print(f"University: {self.name}")

    # Display all students associated with the university
    def display_students(self):
        for student in self.students:
            student.display_details()
            print()


# Create student objects independently
student1 = Student("Shishir", 101)
student2 = Student("Rahim", 102)

# Create a list of existing student objects
student_list = [student1, student2]

# Pass the existing objects to the University
university1 = University("Bishop's University", student_list)

# Display university and student details
university1.display_university()
print("\n=== Students ===")
university1.display_students()

# The student objects can still be used independently
print("=== Independent Student Object ===")
student1.display_details()

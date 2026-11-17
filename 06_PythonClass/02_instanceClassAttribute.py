
class Student:
    # Class attribute: common to students
    university = "Bishop's University"

    def __init__(self, name, student_id, age):
        # Instance attributes: individual student data
        self.name = name
        self.student_id = student_id
        self.age = age


student1 = Student("Rahim", 101, 22)
student2 = Student("Karim", 102, 24)

print(student1.name)
print(student2.name)

print(Student.university)
print(student1.university)

# if we change class attribute by an object(here, student1), it will change for that object only.
student1.university = "Concordia University"

print(student1.university)
print(student2.university)
print(Student.university)

# if we modify the class attribute outside of the class it changes for all objects
# Except that object that is explicitly defined defined different class attribute name/value.
Student.university = "McGill University"

print(student1.university)
print(student2.university)


class Student:
    # Class attribute
    university = "Bishop's University"

    def __init__(self, name, age, mark):
        # Instance attributes
        self.name = name
        self.age = age
        self.mark = mark

    # Instance method
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Mark: {self.mark}")

    # Class method
    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    # Static method
    @staticmethod
    def is_passed(mark):
        return mark >= 50


student1 = Student("Shishir", 25, 85)

# Instance method
student1.display_details()

# Class method
Student.change_university("McGill University")
print(Student.university)

# Static method
print(Student.is_passed(85))
print(Student.is_passed(40))
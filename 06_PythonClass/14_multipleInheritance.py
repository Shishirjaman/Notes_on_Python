
'''
Multiple inheritance:
TeachingAssistant inherits from Student and Employee.
'''

class Student:
    def __init__(self, student_id):
        self.student_id = student_id  # Instance attribute for the student

    def study(self):
        print("The student is studying.")


class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id  # Instance attribute for the employee

    def work(self):
        print("The employee is working.")


class TeachingAssistant(Student, Employee):
    def __init__(self, student_id, employee_id, subject):
        Student.__init__(self, student_id)  # Initialize Student attributes
        Employee.__init__(self, employee_id)  # Initialize Employee attributes
        self.subject = subject  # Attribute specific to TeachingAssistant


ta = TeachingAssistant("S101", "E205", "Python")  # Create an object

print(ta.student_id)  # Inherited data initialized by Student
print(ta.employee_id)  # Inherited data initialized by Employee
print(ta.subject)  # Own attribute

ta.study()  # Inherited method from Student
ta.work()  # Inherited method from Employee

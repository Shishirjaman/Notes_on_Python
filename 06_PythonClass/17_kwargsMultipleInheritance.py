'''
**kwargs collects keyword arguments into a dictionary. 
Each class consumes the arguments it needs and passes the remaining arguments to the next class using super().
This example demonstrates cooperative multiple inheritance. It is a useful pattern when classes are deliberately
designed to work together. It is not necessary to use this pattern for every inheritance hierarchy.
'''

class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)  # Pass remaining arguments along the MRO
        self.name = name  # Store the person's name


class Student(Person):
    def __init__(self, student_id, **kwargs):
        super().__init__(**kwargs)  # Continue to the next initializer
        self.student_id = student_id


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)  # Continue to the next initializer
        self.employee_id = employee_id


class TeachingAssistant(Student, Employee):
    def __init__(self, name, student_id, employee_id):
        # Pass the arguments needed by the classes in the MRO
        super().__init__(
            name=name,
            student_id=student_id,
            employee_id=employee_id
        )


ta = TeachingAssistant("Shishir", "S101", "E205")

print(ta.name)
print(ta.student_id)
print(ta.employee_id)

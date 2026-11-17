
'''
diamond inheritance problem is when two inheritance paths lead to the same base class. For example:
Student inherits from Person. Employee also inherits from Person. TeachingAssistant inherits from both Student and Employee.
Python handles the lookup order using an algorithm called C3 linearization. the flow handled by super(). In multiple
inheritance, super() means “continue searching after the current class in the MRO.”
'''

class Person:
    def identify(self):
        print("Person")


class Student(Person):
    def identify(self):
        print("Student")
        super().identify()  # Continue to the next class in the MRO


class Employee(Person):
    def identify(self):
        print("Employee")
        super().identify()  # Continue to the next class in the MRO


class TeachingAssistant(Student, Employee):
    def identify(self):
        print("TeachingAssistant")
        super().identify()  # Continue through the MRO


ta = TeachingAssistant()
ta.identify()

print([cls.__name__ for cls in TeachingAssistant.mro()])

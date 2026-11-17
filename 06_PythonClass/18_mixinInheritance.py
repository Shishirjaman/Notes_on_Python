'''
A mixin is a small class that provides an additional capability to another class through inheritance. 
It is usually not intended to represent a complete standalone entity.
Here, LogMixin lets both classes share a capability without duplicating the logging code.
'''

class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")  # Provide reusable logging functionality


class Student(LogMixin):
    def __init__(self, name):
        self.name = name

    def study(self):
        self.log(f"{self.name} started studying.")  # Reuse the mixin method


class Employee(LogMixin):
    def __init__(self, name):
        self.name = name

    def work(self):
        self.log(f"{self.name} started working.")  # Reuse the same capability


student = Student("Shishir")
employee = Employee("Rahim")

student.study()
employee.work()

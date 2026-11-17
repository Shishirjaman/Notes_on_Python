'''
Abstract Class:
An abstract class is a class that acts as a blueprint
for its child classes. It can define abstract methods
that child classes must implement. We cannot create an
object of an abstract class if it has unimplemented
abstract methods.

Abstract Method:
An abstract method is a method declared using the
@abstractmethod decorator. It defines a required method
that concrete child classes must implement, but it
does not provide the actual implementation itself.

'''

# Import tools for creating abstract classes and methods
from abc import ABC, abstractmethod


# Abstract base class defines a common interface
class Student(ABC):

    # Constructor initializes the student's name
    def __init__(self, name):
        self.name = name

    # Abstract method: child classes must implement this method
    @abstractmethod
    def introduce(self):
        pass

    # Regular method: child classes inherit this implementation
    def display_name(self):
        print(f"Student name: {self.name}")


# Child class implements the abstract method
class GraduateStudent(Student):

    # Provide the required implementation of introduce()
    def introduce(self):
        print(f"My name is {self.name}. I am a graduate student.")


# Another child class implements the same abstract method differently
class PhDStudent(Student):

    # Provide the required implementation of introduce()
    def introduce(self):
        print(f"My name is {self.name}. I am a PhD student.")


# Create objects of the concrete child classes
graduate1 = GraduateStudent("Shishir")
phd1 = PhDStudent("Karim")


# Call the implemented methods
graduate1.introduce()
graduate1.display_name()

phd1.introduce()
phd1.display_name()

# Uncommenting this line raises a TypeError: because abstract class can't not create an object,
# however it's child class (abstract class is the parent class) can create as many object as it want.
# student1 = Student("Rahim")

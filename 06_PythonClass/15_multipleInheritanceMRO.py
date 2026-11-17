'''
Method Resolution Order(MRO) is the order Python follows when searching
for a method or attribute in a class hierarchy.
When two or more parent classes define the same method, the MRO determines which implementation Python finds first.
'''

class Student:
    def introduce(self):
        print("I am a student.")


class Employee:
    def introduce(self):
        print("I am an employee.")


class TeachingAssistant(Student, Employee):
    pass  # No new methods are needed for this example


ta = TeachingAssistant()

ta.introduce()  # Python finds Student.introduce() first


print(TeachingAssistant.mro())  # Display the method lookup order
print(TeachingAssistant.__mro__)  # Another way to inspect the lookup order
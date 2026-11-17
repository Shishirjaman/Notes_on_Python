'''
Encapsulation:
public attribute writing convention = self.attributeName
protected attribute writing convention = self._attributeName
private attribute writing convention = self.__attributeName
Getter method = use @property before that, it allows to get the method like a attribute
Setter method = use @getter_method_name.setter, it will validate and then update the setter method if we
                try to assign a value in the getter attribute(method)

'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name       # Public attribute
        self.age = age        # Property setter validates the grade
        self.grade = grade     # Property setter validates the grade

    @property   # Allows us to access the method like an attribute (getter)
    def age(self):
        return self._age # Protected-style attribute

    @age.setter # Allows us to validate and update the age when assigning a new value (setter)
    def age(self, new_age):
        if not isinstance(new_age, int) or isinstance(new_age, bool):
            raise TypeError("Age must be an integer.")

        if new_age < 0:
            raise ValueError("Age cannot be negative.")

        self._age = new_age

    @property   # Allows us to access the method like an attribute (getter)
    def grade(self):
        return self.__grade    # Private-style attribute

    @grade.setter   # Allows us to validate and update the age when assigning a new value (setter)
    def grade(self, new_grade):
        if not isinstance(new_grade, (int, float)) or isinstance(new_grade, bool):
            raise TypeError("Grade must be a number.")

        if not 0 <= new_grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.__grade = new_grade

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


student1 = Student("Shishir", 25, 85)

student1.display_details()

student1.age = 26 # actually calling age setter method because of @age.setter we can access it like attribute
student1.grade = 92 # actually calling grade setter method because of @grade.setter we can access it like attribute

print("Updated age:", student1.age) # actually calling age getter method because of @property we can access it like attribute
print("Updated grade:", student1.grade) # actually calling grade getter method because of @property we can access it like attribute

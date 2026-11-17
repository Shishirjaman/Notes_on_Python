# Creating a class named Employee
# Class bundles data and actions for a type of thing
# A class is a blueprint used to create objects.
# Here, Employee is the blueprint for storing employee information and actions.
class Employee:
    # Attributes of the class
    # Attributes are variables that belong to each Employee object.
    employeeCount:int = 0
    
    # ceating constructor of the class
    # A constructor is a special function that runs automatically
    # when a new Employee object is created.
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    # creating a method
    # A method is a function inside a class.
    # This method displays the information of one employee.
    def display_information(self, name):
        if self.name == name:
            print(f"Name : {self.name}")
            print(f"Email : {self.email}")
            print(f"Age : {self.age}")
            

# Creating an object of class Employee
# An object is a real instance created from a class blueprint.
employee1 = Employee('John Doe', 'doejohn123@yahoo.com', 35)
employee1.display_information("John Doe")

# we can change any object instance attributes by assigning a new value to it.
employee1.age = 15
employee1.name = 'Doe John'
employee1.display_information('Doe John')

# changing directly the attributes by assigning new value is not a good practice.
# So, for that we have some specific built in function/ method for attributes in python
# getattr() => takes object instance and the attributes name (in string) as input; returns the attributes value
name = getattr(employee1, 'name')
print(name)

# hasattr() => takes object instance and the attributes name (in string); returns boolean (True/False) based on exsists of the attribute
print(hasattr(employee1, 'salary'))

# setattr() => takes object instance, the attribute name(in string) and value as input and set the value as the new value of the attribute.
setattr(employee1, 'age', 20)
employee1.display_information('Doe John')

# delattr() => delete the attributes value using this function/methods
delattr(employee1, 'email')
employee1.display_information('Doe John')
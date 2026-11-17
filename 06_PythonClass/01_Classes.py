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
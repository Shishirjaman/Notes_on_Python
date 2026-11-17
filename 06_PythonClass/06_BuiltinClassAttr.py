class Employee:
    """This class represents an employee."""

    # Class variable: shared by all Employee objects
    employee_count = 0

    def __init__(self, name, email, age):
        # Instance attributes: each employee has their own values.
        # self.name, self.email, and self.age are instance attributes.
        # Each Employee object gets its own values for these attributes.
        self.name = name
        self.email = email
        self.age = age

        # Increase the class variable every time a new Employee is created.
        Employee.employee_count += 1

    # INSTANCE METHOD
    def display_details(self):
        # This method displays the information stored in the current object.
        print("Name:", self.name)
        print("Email:", self.email)
        print("Age:", self.age)
    
    # CLASS METHOD
    # When a method works with the class variables(employee_count) not with the object instance variables @classmethod written before that.
    # display_employee_count is a method that works with class variable.
    @classmethod
    def display_employee_count(cls):
        # cls refers to the Employee class, so we can access the class variable.
        # self → the individual object
        # cls  → the class
        print("Total Employees:", cls.employee_count)
        
    # STATIC METHOD
    @staticmethod
    def crew_member_salary():
        # This method doesn't need self or cls because salary is fixed
        # and doesn't depend on a particular employee or the class itself.
        print("Crew Member Salary:", 30000, "BDT")


# Creating Employee objects
emp1 = Employee("John", "John@example.com", 25)
emp2 = Employee("Rahim", "rahim@example.com", 30)

# Calling an instance method
# We need an object because display_details() uses self.
emp1.display_details()
emp2.display_details()

# Calling a class method
# We can call it using the class because it works with class-level data.
Employee.display_employee_count()

# Calling a static method
# We don't need an object or the class's data to calculate/display this salary.
Employee.crew_member_salary()


# We can also call the static method through an object.
emp1.crew_member_salary()


# -------------------------------------------------
# BUILT-IN / SPECIAL ATTRIBUTES
# -------------------------------------------------

# __dict__ contains the attributes and values stored in the object.
print(emp1.__dict__)

# __dict__ of the class contains class-level information and methods.
print(Employee.__dict__)

# __doc__ gives the documentation string written inside the class.
print(Employee.__doc__)

# __name__ gives the name of the class.
print(Employee.__name__)

# __module__ tells us the module in which the class was defined.
print(Employee.__module__)
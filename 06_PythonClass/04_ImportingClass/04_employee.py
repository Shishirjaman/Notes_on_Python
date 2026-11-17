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
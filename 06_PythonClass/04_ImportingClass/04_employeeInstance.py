import employee

# Creating Employee objects
emp1 = employee.Employee("John", "John@example.com", 25)
emp2 = employee.Employee("Rahim", "rahim@example.com", 30)

# Calling an instance method
# We need an object because display_details() uses self.
emp1.display_details()
emp2.display_details()

# Calling a class method
# We can call it using the class because it works with class-level data.
employee.Employee.display_employee_count()

# Calling a static method
# We don't need an object or the class's data to calculate/display this salary.
employee.Employee.crew_member_salary()


# We can also call the static method through an object.
emp1.crew_member_salary()
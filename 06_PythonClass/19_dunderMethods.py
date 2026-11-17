
'''
Dunder Methods:
Dunder methods are special methods whose names begin
and end with double underscores.

They allow custom objects to work with Python operations
such as print(), len(), ==, +, indexing, and for loops.

Examples:
__init__() initializes an object.
__str__() defines its readable representation.
__repr__() defines a representation useful for debugging.
__len__() defines the result of len(object).
__eq__() defines equality comparison.
__add__() defines addition between objects.
__iter__() returns an iterator.
__next__() returns the next item during iteration.
__getitem__() supports indexing with [].
__contains__() supports the in operator.

'''

# Define a class representing a collection of courses
class CourseCollection:

    # Initialize the student's name and course list
    def __init__(self, student_name, courses):
        self.student_name = student_name
        self.courses = courses
        self.index = 0

    # Define the readable representation used by print()
    def __str__(self):
        return f"{self.student_name}'s courses: {self.courses}"

    # Define a representation useful for debugging
    def __repr__(self):
        return (
            f"CourseCollection({self.student_name!r}, "
            f"{self.courses!r})"
        )

    # Define the result of len(object)
    def __len__(self):
        return len(self.courses)

    # Define equality based on the course lists
    def __eq__(self, other):
        if not isinstance(other, CourseCollection):
            return NotImplemented
        return self.courses == other.courses

    # Define addition to combine two course collections
    def __add__(self, other):
        if not isinstance(other, CourseCollection):
            return NotImplemented

        combined_courses = self.courses + other.courses
        return CourseCollection(
            f"{self.student_name} and {other.student_name}",
            combined_courses
        )

    # Return an iterator and reset its position
    def __iter__(self):
        self.index = 0
        return self

    # Return the next course or stop iteration
    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration

        course = self.courses[self.index]
        self.index += 1
        return course

    # Support indexing, such as collection[0]
    def __getitem__(self, index):
        return self.courses[index]

    # Support membership checks, such as "Python" in collection
    def __contains__(self, course):
        return course in self.courses


# Create two course collections
collection1 = CourseCollection(
    "Shishir",
    ["Python", "Machine Learning"]
)

collection2 = CourseCollection(
    "Rahim",
    ["Database", "Statistics"]
)


# __str__() is called by print()
print(collection1)

# __repr__() provides a debugging representation
print(repr(collection1))

# __len__() is called by len()
print("Number of courses:", len(collection1))

# __getitem__() is called by indexing
print("First course:", collection1[0])

# __contains__() is called by the in operator
print("Python" in collection1)

# __eq__() is called by the == operator
collection3 = CourseCollection(
    "Karim",
    ["Python", "Machine Learning"]
)
print("Collections have equal courses:", collection1 == collection3)

# __add__() is called by the + operator
combined = collection1 + collection2
print("Combined collection:", combined)

# __iter__() and __next__() enable iteration in a for loop
print("\nIterating through courses:")
for course in collection1:
    print(course)

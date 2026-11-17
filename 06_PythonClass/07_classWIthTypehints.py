'''
Regular class demonstrating common Python type hints.
'''

from typing import Any  # Any permits values of any type when necessary


class Student:
    # Constructor parameters use type hints to communicate expected types.
    def __init__(self, name: str, age: int, gpa: float, is_enrolled: bool, courses: list[str],
                grades: dict[str, float], contact: tuple[str, str], skills: set[str],
                advisor: str | None = None, student_id: int | str = "Not assigned",
                extra_info: Any = None, ) -> None:
        self.name: str = name  # Text
        self.age: int = age  # Whole number
        self.gpa: float = gpa  # Decimal number
        self.is_enrolled: bool = is_enrolled  # True or False

        self.courses: list[str] = courses  # List of strings
        self.grades: dict[str, float] = grades  # String keys, float values
        self.contact: tuple[str, str] = contact  # Fixed-length tuple of strings
        self.skills: set[str] = skills  # Unique strings

        self.advisor: str | None = advisor  # String or None
        self.student_id: int | str = student_id  # Integer or string
        self.extra_info: Any = extra_info  # Any type of value

    # -> str means this method is expected to return a string.
    def get_name(self) -> str:
        return self.name

    # -> int means this method is expected to return an integer.
    def get_course_count(self) -> int:
        return len(self.courses)

    # -> float means this method is expected to return a float.
    def calculate_average(self) -> float:
        if not self.grades:  # Avoid dividing by zero
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    # -> list[str] means the result should be a list of strings.
    def get_skills(self) -> list[str]:
        return sorted(self.skills)

    # -> None means the method is not expected to return a useful value.
    def display_details(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")
        print(f"Enrolled: {self.is_enrolled}")
        print(f"Courses: {self.courses}")
        print(f"Grades: {self.grades}")
        print(f"Contact: {self.contact}")
        print(f"Skills: {self.get_skills()}")
        print(f"Advisor: {self.advisor}")
        print(f"Student ID: {self.student_id}")
        print(f"Average grade: {self.calculate_average():.2f}")


# Create an object with values matching the annotated types.
student = Student( name="Shishir", age=25, gpa=3.8, is_enrolled=True, courses=["Python", "Machine Learning"],
                grades={"Python": 90.0, "Machine Learning": 95.0}, contact=("shishir@example.com", "0123456789"),
                skills={"Python", "Data Science", "SQL"}, advisor=None, student_id=101,
                extra_info={"research_area": "Brain structure prediction"} )

student.display_details()
print(student.get_name())
print(student.get_course_count())

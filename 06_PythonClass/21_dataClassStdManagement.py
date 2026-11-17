
'''
StudentProfile demonstrates default values and field factories.
'''

from dataclasses import dataclass, field


@dataclass
class StudentProfile:
    name: str
    age: int

    # Simple default values.
    university: str = "Bishop's University"
    is_enrolled: bool = True

    # Every profile receives its own independent list.
    courses: list[str] = field(default_factory=list)

    # Every profile receives its own independent dictionary.
    grades: dict[str, float] = field(default_factory=dict)

    # This private note is excluded from repr() and equality.
    _private_note: str = field(default="", repr=False, compare=False)

    # This field is computed after initialization, not passed to __init__().
    course_count: int = field(init=False)

    def __post_init__(self) -> None:
        # Update the computed field after construction.
        self.course_count = len(self.courses)

    def enroll(self, course: str) -> None:
        # Add a course only if it is not already present.
        if course not in self.courses:
            self.courses.append(course)
            self.course_count = len(self.courses)

    def add_grade(self, course: str, grade: float) -> None:
        # Store or update a grade for a course.
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.grades[course] = grade

    def average_grade(self) -> float:
        # Return zero when no grades have been recorded.
        if not self.grades:
            return 0.0

        return sum(self.grades.values()) / len(self.grades)


# Default university, enrollment status, courses, and grades are supplied.
student1 = StudentProfile("Shishir", 25)

# Create another object to demonstrate independent mutable defaults.
student2 = StudentProfile("Rahim", 27)

student1.enroll("Python OOP")
student1.enroll("Machine Learning")
student1.add_grade("Python OOP", 90.0)
student1.add_grade("Machine Learning", 95.0)

print(student1)
print(student1.course_count)
print(student1.average_grade())

# student2's lists and dictionaries are independent of student1's.
print(student2.courses)  # []
print(student2.grades)  # {}

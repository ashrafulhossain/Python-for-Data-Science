class Student:
    def __init__(self, grade_level):
        self.grade = grade_level

    def calculate_marks(self):
        base_marks = 100  # Base marks for each grade
        total_marks = base_marks * self.grade
        print(f"Total Marks: {total_marks}")


class FirstGrader(Student):
    pass


class FifthGrader(Student):
    pass


class TenthGrader(Student):
    pass


# Create objects
first_grader = FirstGrader(1)  # Grade 1
fifth_grader = FifthGrader(5)  # Grade 5
tenth_grader = TenthGrader(10)  # Grade 10

# Calculate marks
first_grader.calculate_marks()  # Output: Total Marks: 100
fifth_grader.calculate_marks()  # Output: Total Marks: 500
tenth_grader.calculate_marks()  # Output: Total Marks: 1000
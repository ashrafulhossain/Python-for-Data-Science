class Intern:
    def __init__(self, exp_level):
        self.exp = exp_level

    def call_salary(self):
        basic_salary = 10000  # Basic salary for an intern
        actual_salary = basic_salary * self.exp
        return actual_salary


class Junior:
    def __init__(self, exp_level):
        self.exp = exp_level

    def call_salary(self):
        basic_salary = 10000  # Basic salary for a junior
        actual_salary = basic_salary * self.exp
        return actual_salary


class MidLevel:
    def __init__(self, exp_level):
        self.exp = exp_level

    def call_salary(self):
        basic_salary = 10000  # Basic salary for a mid-level employee
        actual_salary = basic_salary * self.exp
        return actual_salary


class Senior:
    def __init__(self, exp_level):
        self.exp = exp_level

    def call_salary(self):
        basic_salary = 10000  # Basic salary for a senior employee
        actual_salary = basic_salary * self.exp
        return actual_salary


# Create objects
intern_obj = Intern(1)  # Intern with experience level 1
junior_obj = Junior(2)  # Junior with experience level 2
mid_level_obj = MidLevel(3)  # Mid-level with experience level 3
senior_obj = Senior(4)  # Senior with experience level 4

# Print salaries
print(f"Intern Salary: {intern_obj.call_salary()}")  # Output: Intern Salary: 10000
print(f"Junior Salary: {junior_obj.call_salary()}")  # Output: Junior Salary: 20000
print(f"Mid-level Salary: {mid_level_obj.call_salary()}")  # Output: Mid-level Salary: 30000
print(f"Senior Salary: {senior_obj.call_salary()}")  # Output: Senior Salary: 40000
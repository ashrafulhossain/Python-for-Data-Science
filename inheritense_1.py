class SoftwareDevelopment:
    def __init__(self, exp_work):
        self.exp = exp_work

    def call_salary(self):
        basic_salary = 10000
        actual_salary = basic_salary * self.exp
        print(f"Salary: {actual_salary}")


class Intern(SoftwareDevelopment):
    pass


class Junior(SoftwareDevelopment):
    pass


class MidLevel(SoftwareDevelopment):
    pass


class Senior(SoftwareDevelopment):
    pass


# Create objects
intern_obj = Intern(1)  # Intern with experience level 1
junior_obj = Junior(2)  # Junior with experience level 2
mid_level_obj = MidLevel(3)  # Mid-level with experience level 3
senior_obj = Senior(4)  # Senior with experience level 4

# Call the salary method for each object
intern_obj.call_salary()  # Output: Salary: 10000
junior_obj.call_salary()  # Output: Salary: 20000
mid_level_obj.call_salary()  # Output: Salary: 30000
senior_obj.call_salary()  # Output: Salary: 40000
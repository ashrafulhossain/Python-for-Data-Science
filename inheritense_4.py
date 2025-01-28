class Fitness:
    def __init__(self, exercise_type):
        self.exercise = exercise_type

    def calculate_calories(self):
        base_calories = 100  # Base calories burned per exercise
        total_calories = base_calories * self.exercise
        print(f"Calories Burned: {total_calories} kcal")


class Running(Fitness):
    pass


class Cycling(Fitness):
    pass


class Swimming(Fitness):
    pass


# Create objects
running = Running(3)  # Running (3x intensity)
cycling = Cycling(2)  # Cycling (2x intensity)
swimming = Swimming(4)  # Swimming (4x intensity)

# Calculate calories burned
running.calculate_calories()  # Output: Calories Burned: 300 kcal
cycling.calculate_calories()  # Output: Calories Burned: 200 kcal
swimming.calculate_calories()  # Output: Calories Burned: 400 kcal
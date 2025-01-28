class Restaurant:
    def __init__(self, dish_type):
        self.dish = dish_type

    def calculate_price(self):
        base_price = 200  # Base price for each dish
        total_price = base_price * self.dish
        print(f"Total Price: ${total_price}")


class Appetizer(Restaurant):
    pass


class MainCourse(Restaurant):
    pass


class Dessert(Restaurant):
    pass


# Create objects
appetizer = Appetizer(1)  # Appetizer
main_course = MainCourse(2)  # Main Course
dessert = Dessert(1)  # Dessert

# Calculate prices
appetizer.calculate_price()  # Output: Total Price: $200
main_course.calculate_price()  # Output: Total Price: $400
dessert.calculate_price()  # Output: Total Price: $200
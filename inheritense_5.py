class ElectricityBill:
    def __init__(self, usage_level):
        self.usage = usage_level

    def calculate_bill(self):
        base_cost = 5  # Base cost per unit of electricity
        total_bill = base_cost * self.usage
        print(f"Electricity Bill: ${total_bill}")


class Fan(ElectricityBill):
    pass


class AC(ElectricityBill):
    pass


class Refrigerator(ElectricityBill):
    pass


# Create objects
fan = Fan(10)  # Fan usage (10 units)
ac = AC(50)  # AC usage (50 units)
refrigerator = Refrigerator(20)  # Refrigerator usage (20 units)

# Calculate bills
fan.calculate_bill()  # Output: Electricity Bill: $50
ac.calculate_bill()  # Output: Electricity Bill: $250
refrigerator.calculate_bill()  # Output: Electricity Bill: $100
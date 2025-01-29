class Shape:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__(l, w)

    def area(self):
        return self.l * self.w


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)  # Storing radius in both l and w for consistency
        self.r = radius

    def area(self):
        return 3.1416 * self.r ** 2


# Example Usage
r = Rectangle(10, 20)
print("Rectangle Area:", r.area())

c = Circle(7)
print("Circle Area:", c.area())
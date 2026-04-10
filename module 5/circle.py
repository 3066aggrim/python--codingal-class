class circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


radius = float(input("Enter radius: "))

c = circle(radius)

print("Area is:", c.area())
print("Circumference is:", c.circumference())

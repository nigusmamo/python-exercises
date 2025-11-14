import math

class Circle:
    def __init__(self,radius = 1):
        self.radius = radius
    def get_area(self):
        print("the area of the circle is:",round(self.radius * self.radius * math.pi,2))
    def get_perimeter(self):
        print("the perimeter of the circle is:", round(2 * math.pi * self.radius,2))
    def get_radius(self):
        print(f"the radius of the circle is:",self.radius)

c1 = Circle(5)
c2 = Circle()
c3 = Circle()

c1.get_area()
c2.get_perimeter()
c3.get_radius()

print(Circle(5).get_area())
print(Circle(2).get_perimeter())
print(Circle().get_radius())







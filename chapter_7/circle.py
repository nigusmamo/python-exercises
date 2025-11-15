from geometric_object import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self,radius):
        super().__init__()
        self.__radius = radius
    def get_Radius(self):
        return self.__radius
    def set_radius(self,radius):
        self.__radius = radius
    def get_area(self):
        return math.pi * (self.__radius * self.__radius)
    def get_diameter(self):
        return 2 * self.__radius
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
    def printCircle(self):
        print(f"{self.__str__()} + radius:  + {str(self.__radius)}")

c1 = Circle(3)
c2 = Circle(4)
c3 = Circle(6)
c4 = Circle(9)

for g in (c1,c2,c3,c4):
    print(g.get_area())
    print(g.get_diameter())
    print(g.get_perimeter())


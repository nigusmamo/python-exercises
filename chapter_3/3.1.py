import math

radius = float(input("enter the number of radius..."))
side = 2 * radius * math.sin(math.pi / 5)

area = 3 / 2 * (math.sqrt(3)) * side ** 2
# display the answer
print ("The area of the pentagon is",area)
import math

numberofside = int(input("enter the number of side..."))

lengside = float(input("enter the side ..."))

area = (numberofside * (lengside ** 2))/ (4 * (math.tan(math.pi /  numberofside )))

print ("The area of the poiygon is",area)
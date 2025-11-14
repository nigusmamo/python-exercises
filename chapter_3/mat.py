import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discrminant = pow(b,2) - (4 * (a*c))

if discrminant == 0:
    print(f"The equation has one solution: {b / (2 * a)}")
elif discrminant > 0:
    print(f"The equation has two solution: {(b + math.sqrt(discrminant)) / (2 * a)} and {(b - math.sqrt(discrminant)) / (2 * a)}")
else :
    print(f"The equation has no solution!")


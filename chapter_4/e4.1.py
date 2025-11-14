import math

a , b , c = eval(input("Enter three numbers a,b,c..."))

D = ((b ** 2) - (4 * a * c))

if D > 0:
    x = math.sqrt(D)
    R1 = (-b + x) / (2 * a)
    R2 = (-b - x) / (2 * a)
    print ("The roots are",R1,"and",R2)
if D == 0 :
    answer = -b / (2 * a)
    print ("The root is",answer)
if D < 0 :
    print ("The equation has no real root!")
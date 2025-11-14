pounds = float(input("enter the number of pound..."))
inch = int(input("enter the number of inch..."))

weight =  0.45359237 * pounds
height = 0.0254 * inch
BMI = weight / height ** 2

# Display the result
print ("BMI IS",round(BMI,2))


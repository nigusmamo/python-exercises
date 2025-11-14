pounds = float(input("enter the number of pound..."))
inch = float(input("enter the number of inch..."))
feet = float(input("enter the number of feet..."))

kilogram_per_pound = 0.45359237
meter_per_inch = 0.0254
meter_per_feet = 0.3048


weightinkilogram =  kilogram_per_pound * pounds
heightinmeter1 = meter_per_inch * inch  
heightinmeter2 = meter_per_feet * feet 
totalheight = heightinmeter1 + heightinmeter2

BMI = weightinkilogram / totalheight ** 2

# Display the result

print ("BMI is",round(BMI,2))
if BMI < 18:
    print ("you are under weight")
elif BMI < 25 :  
    print ("you are Normal")
elif BMI < 30 :
    print ("you are Overweight") 
elif BMI < 50 :
    print("obese")     
else :
    print ("you are overobese")






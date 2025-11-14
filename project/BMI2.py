weight = float(input("enter the number of kilogram..."))
height = float(input("enter the number of meter..."))
BMI = weight / height ** 2
print ("your BMI is",round(BMI,2))
if BMI < 18:
    print ("then you are under weight")
elif BMI < 25 :  
    print ("then you are Normal")
elif BMI < 30 :
    print ("then you are Overweight") 
elif BMI < 50 :
    print("then you are obese")     
else :
    print ("then you are overobese")
if BMI < 18 :
   
    additionalweight = -((weight) - (height ** 2) * 18)

    print ("so,you should add",round(additionalweight,2),"kg of", "additionalweight")
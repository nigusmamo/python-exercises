weight = float(input("enter the number weight in kilogram..."))
height = float(input("enter the number hight in meter..."))

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
# advice
additionalweight = 52.02 - weight
if weight < 52.02 :
    print ("so,you should add",round(additionalweight,2),"kg of", "additionalweight")
lossweight = weight - 72.25
if weight > 72.25 :
    print ("you should loss",round(lossweight,2),"kg","weight")



weight = float(input("enter weight in kilogram..."))
height = float(input("enter height in meter..."))
W = weight 
H = height 
BMI = W / H ** 2

# print ("your BMI is",round(BMI,2))

# advice
if BMI < 18:
    print ("your BMI is",round(BMI,2),"you should gain some weight")
    normalweight = (H ** 2) * 18
    print ("you should gain" ,round(normalweight - weight,2),"kg","weight")
elif BMI < 25 :
    print ("your BMI is",round(BMI,2),"you are normal")
else :
    print ("your BMI is",round(BMI,2),"you should loss some weight") 
    overweight = (H ** 2) * 30
    print ("you should loss" ,-round(weight - overweight,2),"kg","weight") 




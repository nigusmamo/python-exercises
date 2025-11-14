weight  = int(input("Enter weight in kilogram..."))
height_in_centimeter = int(input("Enter height in centimeter..."))
height_in_meter = height_in_centimeter / 100
W = weight
H = height_in_meter
BMI = W / (H ** 2)
if BMI < 18 :
    normal_weight = (H ** 2) * 18
    weight_gain = (normal_weight) - (weight)
    print ("Your BMI is ",round(BMI,2),"then you are under weight")
    print ("so, you should gain ",round(weight_gain,2),"kg","weight")
elif BMI < 25 :
    print ("Your BMI is",BMI)
    print ("congratulations! you are normal")
else :
    over_weight = (H ** 2) * 25
    weight_loss =  (weight) - (over_weight) 
    print ("your BMI is",round(BMI,2),"then you are obes")
    print ("so, you should loss ",round(weight_loss,2),"kg","weight")
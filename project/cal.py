num1 = int(input("Enter the first num: ")) 
num2 = int(input("Enter the second num: "))
oprator = input("Enter the oprator '+,-,*,/': ")
if oprator == "+":
    print("the sum of ",num1,"+",num2,"is",num1+num2)
elif oprator == "-":
    print("the difference of ",num1,"-",num2,"is",num1-num2)
elif oprator == "*":
    print("the product of ",num1,"*",num2,"is",num1*num2)
elif oprator == "/":
    print("the quetiont of ",num1,"/",num2,"is",num1/num2)
else:
    print("An error occured you may be enter invalid oprator!")
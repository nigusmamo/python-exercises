import random

number1 = random.randint(0,99)
number2 = random.randint(0,99)

useranswer = int(input((" What is the sum of " + str(number1) + " + "  + str(number2) + " = ? ")))
answer = number1 + number2
if answer == useranswer :
    print ("True")
else :
    print ("False")

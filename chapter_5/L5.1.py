import random 

num1 = random.randint(0,9)
num2 = random.randint(0,9)

if num1 < num2 :
   num1 , num2 = num2 , num1

answer = eval(input("what is " + str(num1) + " - " + str(num2) + " ? "))
while num1 - num2 != answer :
   answer = eval(input("wrong answer! try again in. what is " + str(num1) + " - " + str(num2) + " ? "))
   print ("You got it!")

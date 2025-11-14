
num = "beka"

while num == "beka":
    num = int(input("enter num "))
    
print ("the sum is ")



fname = input("enter your fname: ")
length = len(fname)
if length < 5:
    sname = input("enter your sname: ")
    name = fname +  sname
    final_name = name.upper()
    print (final_name)
else :
    fname = fname.lower()
    print (fname)



name = input("enter your name in lower case: ")
name = name.title()
print(name)




name = input("enter your name: ")
num = int(input("how many times print your name?"))
for x in range(num):
  for i in name:
    print(i)




num = int(input("enter.."))
for i in range(6,num-1,-1):
    print(i)


num = int(input("enter.."))
for i in range(3,27,3):
    answer = i / num
    print (i," ÷ ", num," = ",answer)






name = input("enter your name: ")
num = int(input("how many times print your name?"))
for i in range(num):
    print(name)



num = int(input("enter a number b/n 10 and 20: "))

while num < 10 or num > 20:
    if num < 10:
        print ("Too low")
    else :
        print ("Too high")
    num = int(input("pleas try again! "))
print ("Thank you!!!")




import random

score = 0
for i in range(1,6):
 num1 = random.randint(0,50)
 num2 = random.randint(0,50)
 correct = num1 + num2
 print (num1," + ",num2," = ")
 answer = int(input("your answer: "))
 print ()
 if answer == correct :
     score = score + 1
     print ("you scored ",score,"out of 5 ")



total = 0
while total <= 50 :
    num = int(input("enter the num: "))
    total += num
    print ("the total is ",total)




again = "yes"
while again == "yes" :
    print ("hellow")
    again = input("do you went to loop again ? ")



name = input("enter your name: ")
num = int(input("enter num: "))
for i in range(num):
    print (i)




num = int(input("enter.."))
for i in range(1,6):
    answer = i * num
    print (i," x ", num," = ",answer)
num = int(input("enter.."))
for i in range(50,num-1,-1):
    print (i)




for i in range(1,10,2):

    print (i)
for i in "word":
    print(i)
name = input("enter your name ")
num = int(input("enter the num.."))
for x in range(num):
    for i in name :
       print (i)
#nam = input("enter your name: ")
#for i in nam:
  #  print (i)
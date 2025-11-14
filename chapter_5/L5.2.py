import random

secret = random.randint(0,100)
print ("guess a magic number between 0 and 100")
guess = eval(input("enter your guess.."))

if guess == secret :
    print ("yes,the number is ",secret)

elif guess > secret :
    print ("your guess is too high!")

else :
    print ("your guess is too low!")

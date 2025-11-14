import random

guess = input("Enter your guess...")
secret = random.randint(0,1)
print ("secret is",secret)
if (secret == 1) and (guess == "head") or (secret == 0) and (guess == "tail") :
    print ("Your guess is correct")
else :
    print ("Your guess is INcorrect")
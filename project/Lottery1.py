import random

Lottery = random.randint(100,999)
Guess = int(input("Enter your lottery pick (3 digits)...",))

lottery_digit1 = Lottery // 100
lottery_digit2 = Lottery % 100 // 10
lottery_digit3 = Lottery % 100 % 10

guess_digit1 = Guess // 100
guess_digit2 = Guess % 100 // 10
guess_digit3 = Guess % 100 % 10 

print ("lottery number is",Lottery)
print ("Your guess is",Guess)

if Lottery == Guess :
    print ("Exact matches you win $10,000")
elif (lottery_digit1 == guess_digit1) and (lottery_digit2 == guess_digit3) and (lottery_digit3 == guess_digit2) \
     (lottery_digit1 == guess_digit2) and (lottery_digit2 == guess_digit3) and (lottery_digit3 == guess_digit1) \
     (lottery_digit1 == guess_digit3) and (lottery_digit2 == guess_digit2) and (lottery_digit3 == guess_digit1) \
     (lottery_digit1 == guess_digit2) and (lottery_digit2 == guess_digit1) and (lottery_digit3 == guess_digit3) \
     (lottery_digit1 == guess_digit3) and (lottery_digit2 == guess_digit1) and (lottery_digit3 == guess_digit2) :
     print ("match all digits you win $3,000")
elif  (lottery_digit1 == guess_digit1
    or lottery_digit1 == guess_digit2
    or lottery_digit1 == guess_digit3
    or lottery_digit2 == guess_digit1
    or lottery_digit2 == guess_digit2
    or lottery_digit2 == guess_digit3
    or lottery_digit3 == guess_digit1
    or lottery_digit3 == guess_digit2
    or lottery_digit3 == guess_digit3) :
    print ("matches one didit you win $1,000")
else :
    print ("sorry, no match!")

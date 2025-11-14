import random

lottery = random.randint(10,99)
guess = int(input("Enter your lottery pick (tow digits)..."))

lottery_digit1 = lottery // 10
lottery_digit2 = lottery % 10

guess_digit1 = guess // 10
guess_digit2 = guess % 10
print ("lottery number is",lottery)
print ("Your guess is",guess)
if guess == lottery :
    print ("Exact match you win $ 10,000")

elif (guess_digit1 == lottery_digit2) \
    and (guess_digit2 == lottery_digit1) : 
                        
    print ("match all digits you win $ 3,000") 
elif (guess_digit1 == lottery_digit1 
    or guess_digit1 == lottery_digit2
    or guess_digit2 == lottery_digit1
    or guess_digit2 == lottery_digit2 ) :
     print ("mutch one digit you win $ 1,000")
else :
     print ("sorry, no mutch!!!")
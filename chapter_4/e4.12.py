number = eval(input("Enter an intiger..."))
print (number,"is divisible by 5 and 6 ?",(number % 5 == 0) and (number % 6 == 0))

print (number,"is divisible by 5 or 6 ?",(number % 5 == 0) or (number % 6 == 0))

if (number % 5 == 0 or number % 6 == 0) and \
not (number % 2 == 0 and number % 3 == 0) :
    print (number, "is divisible by 5 or 6, but not both ?",(number % 5 == 0) or (number % 6 == 0))


   
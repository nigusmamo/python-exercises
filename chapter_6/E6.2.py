def sumdigits(n):
# Extract digits
    ndigit1 = n // 100
    ndigit2 = n % 100 // 10
    ndigit3 = n % 10
    return ndigit1 + ndigit2 + ndigit3
# display the result
print ("sum digit of number is",sumdigits(n=int(input("Enter three digit number: "))))


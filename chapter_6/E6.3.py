def revers(num):
# Extract digits
    ndigit1 = num // 100
    ndigit2 = num % 100 // 10
    ndigit3 = num % 10
    revers = [ndigit3,ndigit2,ndigit1]
    for i in revers:
        print (i,end = '')
def main():
    
    print ("the revers is: ",revers(num = int(input("Enter a three digit number: ")) ))
main()



# print ("The reverse is ",revers(num = eval(input("Enter a three digit number: "))))

  
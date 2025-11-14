Limit = int(input("Enter the limit: "))
for i in range(1,Limit):
    if (i % 3 == 0) or (i % 5 == 0):
        print (i)
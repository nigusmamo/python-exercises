exchange_rate = float(input("Enter the exchange rate from dollars to RMB..."))
conversion = int(input("Enter 0 to convert dollars to RMB and 1 vice versa..."))
if conversion == 0 :
    amount_of_dollars = int(input("enter amount of dollars..."))
    dollars_to_RMB = exchange_rate * amount_of_dollars
    print ("$",amount_of_dollars,"is",round(dollars_to_RMB,2),"yuan")
if conversion == 1 :
    amount_of_RMB = int(input("enter amount of RMB..."))
    RMB_to_dollars = amount_of_RMB / exchange_rate
    print (amount_of_RMB,"yuan is","$",round(RMB_to_dollars,2))

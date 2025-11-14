rows = int(input("Enter the number of row you want to draw: "))
# You can change this to any number

for i in range(rows, 0, -1):
    print("* " * i)

for i in range(1, rows + 1):
    print("* " * i)

from tkinter import *

# wid = input("Enter the width of rectangle: ")
# hei = input("Enter the height of rectangle: ")
# bgcolor = input("Enter color of rectangle you went see: ")

# x_position = int(input("Enter x-position: "))
# y_position = int(input("Enter y-position: "))

window = Tk()
window.title("rectangle with users input")
shape = Canvas(window,width = 200, height = 10, bg = "yellow").place(x = 300, y = 300)
a = Canvas.create_rectangle(width = 200, height = 10)
a.pack()
window.mainloop()


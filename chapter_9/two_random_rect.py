from tkinter import *
import random
width_1 = random.randint(100,200)
height_1 = random.randint(50,100)
x_position = random.randint(0,100)
y_position = random.randint(0,100)

width_2 = random.randint(100,200)
height_2 = random.randint(50,100)
x_position2 = random.randint(0,100)
y_position2 = random.randint(0,100)

colors = ["red","white","blue","yellow","green","gray","purple","violet","indigo","tomato"]
bgcolor = random.choices(colors)
bgcolor_2 = random.choices(colors)

window = Tk()
window.title("two random rectangls")
rectangle = Canvas(window,width = width_1, height = height_1, bg = bgcolor).place(x = x_position, y = y_position)
rectangle_2 = Canvas(window,width = width_2, height = height_2, bg = bgcolor_2).place(x = x_position2, y = y_position2)

window.mainloop()

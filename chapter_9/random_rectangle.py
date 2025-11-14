from tkinter import *
import random

wid = random.randint(100,200)
hei = random.randint(10,100)
colors = ["red","white","blue","yellow","green","gray","purple","violet","indigo","tomato"]
bgcolor = random.choices(colors)

x_position = random.randint(0,100)
y_position = random.randint(0,100)

window = Tk()
window.title("random sized rectangle")
rectangle = Canvas(window,width = wid, height = hei, bg = bgcolor).place(x = x_position , y = y_position)

window.mainloop()

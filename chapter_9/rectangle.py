from tkinter import *

window = Tk()
window.title("rectangle with users input")
shape = Canvas(window,width = 200, height = 10, bg = "yellow").place(x = 300, y = 300)
a = Canvas.create_rectangle(width = 200, height = 10)
a.pack()
window.mainloop()


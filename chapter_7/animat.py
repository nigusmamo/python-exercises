from tkinter import *

class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("animation")
        self.canvas = Canvas(window,width=500,height=500,bg = "white")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame,text = "rectangle",fg = "red").grid(row = 1, column = 1,command = draw_rectangle(self))
        Button(frame,text = "oval",fg = "red").grid(row = 1, column = 2)
        Button(frame,text = "arc",fg = "red").grid(row = 1, column = 3)
        window.mainloop()
    def draw_rectangle(self):
        self.canvas.create_rectangle(10,10,190,90,tag = "rect")
    def draw_oval(self):
        self.canvas.create_oval(10,10,190,90,tag = "oval")
    def draw_arc(self):
        self.canvas.create_arc(10,10,190,90,tag = "rect")

CanvasDemo()








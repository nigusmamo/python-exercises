from tkinter import *

class Event:
    def __init__(self):
        window = Tk()
        window.title("animation")
        canvas = Canvas(window,width=500,height=500,bg = "white")
        canvas.pack()
        canvas.bind("<Key>",self.processKey(self))
        canvas.focus_set()

        window.mainloop()
    def processKey(self,event):
        print("keysym:",event.Keysym)
        print("char:",event.char)
Event()

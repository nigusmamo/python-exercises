from tkinter import *
class Animation:
    def __init__(self):
        self.radius = 50
        window = Tk()
        window.title("animat objects")
        width = 250
        canvas = Canvas(window,width = 250, height = 10, bg = "white")
        canvas.pack()

        x = 0
        canvas.create_text(x,30,text = "Message moving...",tags = "text")
        dx = 3
        while True:
            canvas.move("text",dx,0)
            canvas.after(400)
            canvas.update()
            if x < width:
                x += dx
            else:
                x = 0
                canvas.delete("text")
                canvas.create_text(x,30,text = "Message moving...",tags = "text")

        window.mainloop()

Animation()


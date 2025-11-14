from tkinter import *

window = Tk()

window.title("gui game")
def processok():
    print("OK button is clicked")
def processcancle():
    print("CANCLE button is clicked")
    
okbtn = Button(window, text = "OK",fg = "#AB84F9",command = processok()).place(x = 50, y = 50)
canclebtn = Button(window,text = "CANCEL",fg = "red",command = processcancle()).place(x = 150, y = 50)
cbtn = Checkbutton(window,text = "it's checkbutton").place(x = 50, y = 100)
rbtn = Radiobutton(window,text = "green", fg = "green").place(x = 50, y = 10)
# rbtn.pack()
rbtn2 = Radiobutton(window,text = "yellow", fg = "yellow").place(x = 150, y = 10)
# rbtn2.pack()
rbtn3 = Radiobutton(window,text = "white", fg = "white").place(x = 250, y = 10)
frame = Frame(window)
frame.grid(row =1, column=1)

lable = Label(frame, text="Enter your name: ")
lable.pack()
name = StringVar()
entryname = Entry(frame,textvariable = name)

entryname.grid(row =1, column=1)
# rbtn3.pack()
# cbtn.pack()
# okbtn.pack()
# canclebtn.pack()

window.mainloop()
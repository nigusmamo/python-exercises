import turtle
import random
color = colors = ["red","blue","yellow","green","gray","purple","violet","indigo","tomato"]
bgcolor = random.choices(colors)
shape = random.randint(4,10)
turtle.pensize(1)
turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color(bgcolor)
turtle.circle(40, steps = shape)
turtle.end_fill()

turtle.done()


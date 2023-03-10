# Exercise 5 on "How to think like a computer scientist", ch. 11.
from os import name
from tkinter import filedialog
import turtle
name = filedialog.askopenfilename(title="Choose File")
t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
for line in name:
    if line == "UP/n":
        t.up()
    elif line == "DOWN/n":
        t.down()
    else:
        t.goto(float(line.split()[0]), float(line.split()[1]))

# wait
turtle.Screen().exitonclick()


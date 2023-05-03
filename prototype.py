import turtle
import random

# create LIFE
t = turtle.Turtle()

# generate a random point A and B
x_red = random.randint(-380, 200)
y_red = random.randint(-160, 250)

x_green = random.randint(-380, 200)
y_green = random.randint(-160, 250)

# The creations start!
t.penup()
t.goto(x_red, y_red)
t.pendown()
t.color("red")
t.dot()

# How fast it goes?
for i in range(20):
    t.forward(10)

# move it to the B point!
t.goto(x_green, y_green)
t.color("green")
t.dot()

# keep the window open until it is closed by the user
turtle.mainloop()

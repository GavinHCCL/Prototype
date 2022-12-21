import turtle
import random

# create a turtle object
t = turtle.Turtle()

# generate a random x and y coordinate
x_red = random.randint(-380, 200)
y_red = random.randint(-160, 250)

x_green = random.randint(-380, 200)
y_green = random.randint(-160, 250)

# move the turtle to the starting position for the red dot
t.penup()
t.goto(x_red, y_red)
t.pendown()

# set the turtle's color to red and draw a dot
t.color("red")
t.dot()

# move the turtle in small increments
for i in range(20):
    t.forward(10)

# move the turtle to the random position
t.goto(x_green, y_green)

# set the turtle's color to green and draw a dot
t.color("green")
t.dot()

# keep the window open until it is closed by the user
turtle.mainloop()

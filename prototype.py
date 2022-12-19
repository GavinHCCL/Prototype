import turtle
import random

# create a turtle object
t = turtle.Turtle()

# move the turtle to the starting position for the red dot
t.penup()
t.goto(-100, 0)
t.pendown()

# set the turtle's color to red and draw a dot
t.color("red")
t.dot()

# move the turtle in small increments
for i in range(20):
    t.forward(10)

# generate a random x and y coordinate
x = random.randint(-200, 200)
y = random.randint(-200, 200)

# move the turtle to the random position
t.goto(x, y)

# set the turtle's color to green and draw a dot
t.color("green")
t.dot()

# keep the window open until it is closed by the user
turtle.mainloop()

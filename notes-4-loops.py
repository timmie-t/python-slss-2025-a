# Loops
# Author: Timmie
# October 14

import random
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()

mikey.turtlesize(1)  # size
mikey.color("orange")

# make 100 cookies
for counter in range(10):
    # magnify the counter
    counter = counter * 50
    mikey.penup()
    mikey.setheading(0)
    # change the cookie colour
    mikey.color("brown")
    # draw a circle
    mikey.goto(-5, -30)
    mikey.pendown()
    mikey.circle(30)
    # put a chocolate chip on top left
    mikey.penup()
    mikey.goto(-10, 10)
    mikey.stamp()
    # chip top right
    mikey.goto(10, -10)
    mikey.stamp()
    # chip on bottom right
    mikey.goto(10, 10)
    mikey.stamp()
    # chip on bottom left
    mikey.goto(-10, -10)
    mikey.stamp()
    # chip in middle
    mikey.goto(0, 0)
    mikey.stamp()

mikey.speed(0)
# make cookies in random locations
# make a 1000 cookies
for _ in range(1000):
    x = random.randrange(-700, 700)
    y = random.randrange(-700, 701)
    make_cookie(x, y)

window.exitonclick()

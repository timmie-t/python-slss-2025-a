# Turtle Artist
# Author: Timmie
# 28 October

# Use turtle to draw a cheeseburger

import turtle

# Draw a cheeseburger

wn = turtle.Screen()
t = turtle.Turtle()

# Dictionary to hold burger colours
BURGER_COlORS = {
    "bun": "#EDAE49",
    "patty": "#854D27",
    "cheese": "#FFC800",
    "lettuce": "#00AF54",
    "tomato": "#FE5F55",
    "sesame": "#F0B67F",
}

# Draw the bottom bun
t.pendown()
t.pensize(15)
t.goto(0, 0)
t.color(BURGER_COlORS["bun"])
t.shape("circle")
t.left(180)
t.forward(100)
t.right(90)
t.forward(35)
t.penup()
t.goto(0, 0)
t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(35)
t.left(90)
t.forward(200)
t.backward(200)
t.right(90)
t.penup()

# Draw the burger patty
t.color(BURGER_COlORS["patty"])
t.goto(100, 48)
t.pendown()
t.right(20)
t.forward(20)
t.left(40)
t.forward(20)
t.left(70)
t.forward(57)  # Leaving a gap in the middle of the patty so the cheese does not overlap
t.color("white")
t.forward(90)
t.color(
    BURGER_COlORS["patty"]
)  # Changing the patty colour back to continue the patty layer
t.forward(53)
t.left(50)
t.forward(20)
t.left(60)
t.forward(24)
t.left(70)
t.goto(100, 48)
t.penup()

# Draw the cheese slice
t.color(BURGER_COlORS["cheese"])
t.goto(0, 75)
t.pendown()
t.left(15)
t.forward(100)
t.left(75)
t.forward(20)
t.left(90)
t.forward(200)
t.left(90)
t.forward(20)
t.goto(0, 75)
t.penup()

# Draw a piece of lettuce with a thinner width
t.color(BURGER_COlORS["lettuce"])
t.goto(95, 135)
t.pendown()
t.backward(20)
t.right(90)
t.forward(200)
t.left(90)
t.forward(20)
t.left(90)
t.forward(200)
t.penup()

# Draw a slice of tomato with the same width as the lettuce
t.color(BURGER_COlORS["tomato"])
t.goto(95, 170)
t.pendown()
t.left(90)
t.forward(20)
t.left(90)
t.forward(200)
t.left(90)
t.forward(20)
t.left(90)
t.forward(200)
t.penup()

# Draw the top bun with a "rounded" top
t.color(BURGER_COlORS["bun"])
t.goto(95, 205)
t.pendown()
t.left(90)
t.forward(35)
t.left(30)
t.forward(15)
t.left(60)
t.forward(180)
t.left(30)
t.forward(15)
t.left(60)
t.forward(40)
t.left(90)
t.forward(200)
t.penup()

# Stamp some sesame seeds on the top bun
t.color(BURGER_COlORS["sesame"])
t.shapesize(0.5)
print(t.pos())
t.goto(55, 235)
t.stamp()
t.goto(-55, 235)
t.stamp()
t.goto(16, 235)
t.stamp()
t.goto(-16, 235)
t.stamp()
t.goto(75, 225)
t.stamp()
t.goto(-75, 225)
t.stamp()
t.goto(35, 225)
t.stamp()
t.goto(-35, 225)
t.stamp()
t.goto(0, 225)
t.stamp()

wn.exitonclick()

# from turtle import Turtle, Screen
# import random
# import turtle
# my_pen = Turtle()
# my_pen.shape("turtle")
# my_pen.color("red")

# for i in range(0,4):
#     my_pen.forward(100)
#     my_pen.right(90)

# turtle.colormode(255)
# my_pen.left(90)
# my_pen.penup()
# my_pen.forward(20)
# my_pen.pendown()
# dashlength = 10
# gaplength = 10

# for i in range(20):
#     if i%2 == 0:
#         my_pen.pendown()
#         my_pen.forward(dashlength)
#     else:
#         my_pen.penup()
#         my_pen.forward(gaplength)

# my_pen.up()
# my_pen.left(90)
# my_pen.forward(100)
# my_pen.left(90)
# my_pen.forward(300)

# my_pen.down()
# for n in range(100):
#     my_pen.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
#     for i in range(n + 2):
#         my_pen.forward(100)
#         my_pen.right(360/(n+2))

# screen = Screen()
# screen.exitonclick()


# import turtle
# import random

# # Set up the turtle
# t = turtle.Turtle()
# t.speed('fastest')

# # Set the pen color and line width
# turtle.colormode(255)
# t.pensize(width=6)
# # Draw a random line
# for i in range(1000):
#     t.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
#     x = random.randint(1,2)
#     if x == 1:
#         t.forward(30)
#     elif x == 2:
#         t.backward(30)

#     x = random.randint(3,4)
#     if x == 3:
#         t.left(90)
#     elif x == 4:
#         t.right(90)


# # Hide the turtle
# t.hideturtle()

# # Keep the window open until it's manually closed
# turtle.done()


# import turtle
# import random
# # Set up the turtle
# t = turtle.Turtle()
# t.speed("fastest")
# turtle.colormode(255)

# # Set the pen color and line width
# t.pencolor('black')
# t.pensize(2)

# # Draw a circle
# radius = 100  # the radius of the circle



# while True:
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     t.color(r,g,b)
#     t.circle(radius)
#     t.right(10)

# # Hide the turtle
# t.hideturtle()

# # Keep the window open until it's manually closed
# turtle.done()


import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

#loop to draw
x = -200
y = -200
t.goto(x,y)
t.pendown()

for i in range(121):
    t.pencolor(random.choice(colors))
    t.pendown()
    t.dot(30)
    t.penup()
    t.forward(40)
    x += 40

    if x > 200:
        x = -200
        t.goto(x,y + 40)
        y += 40

# hide the turtle
t.hideturtle()

turtle.done()

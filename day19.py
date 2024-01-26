# import turtle

# t = turtle.Turtle()
# screen = turtle.Screen()

# def moveforward():
#     t.forward(1)

# def moveback():
#     t.backward(1)

# def moveleft():
#     t.left(1)

# def moveright():
#     t.right(1)

# screen.listen()
# screen.onkeypress(fun=moveforward, key='w')
# screen.onkeypress(fun=moveleft, key='a')
# screen.onkeypress(fun=moveright, key='d')
# screen.onkeypress(fun=moveback, key='s')


# screen.exitonclick()


import random
import turtle
import time
turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=800, height=600)
players = []
colors = ['red', 'green', 'blue', 'orange', 'purple', 'black', 'brown', 'cyan', 'pink']
x_positions = []
x = -300
y = -200

game_control = turtle.Turtle()
game_control.penup()
game_control.goto(200,0)
game_control.pendown()
game_control.goto(200,200)
game_control.goto(200,-200)

for i in range(0,9):

    player = turtle.Turtle()
    player.color(colors[i])
    player.penup()
    player.shape('turtle')
    y += 50
    x_positions.append(x)
    player.goto(x, y)
    players.append(player)

state = True
while state:

    for i in range(0 , 9):
        z = random.randint(0,5)
        players[i].forward(z)
        x_positions[i] += z
        if x_positions[i] >= 200:
            winner = colors[i]
            print(f'winner is {winner}')
            state = False
            break
        print(x_positions)


screen.exitonclick()















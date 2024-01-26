import turtle
import time
import random
from turtle import Turtle

# snake class
class Snake:

    def __init__(self):
        self.starting_position = [(0,0),(-20,0), (-40,0)]
        self.snake_body = []
        self.DISTANCE = 20
        self.create_snake()
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in self.starting_position:
            snake = turtle.Turtle()
            snake.shape('square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def get_fat(self):
        snake = turtle.Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        last_x = self.snake_body[-1].xcor()
        last_y = self.snake_body[-1].ycor()
        snake.goto(last_x,last_y)
        self.snake_body.append(snake)



    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0 , -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(self.DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != self.DOWN:
            self.snake_body[0].setheading(self.UP)

    def down(self):
        if self.snake_body[0].heading() != self.UP:
            self.snake_body[0].setheading(self.DOWN)

    def left(self):
        if self.snake_body[0].heading() != self.RIGHT:
            self.snake_body[0].setheading(self.LEFT)

    def right(self):
        if self.snake_body[0].heading() != self.LEFT:
            self.snake_body[0].setheading(self.RIGHT)



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=('Arial',16,'normal'))

    def write_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial',16,'normal'))



screen = turtle.Screen()
WIDTH = 800
HEIGHT = 600
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Snake game')
screen.bgcolor('black')
screen.tracer(0)

snake_ = Snake()
score_ = Scoreboard()

screen.listen()
screen.onkey(snake_.up,"Up")
screen.onkey(snake_.down,"Down")
screen.onkey(snake_.left,"Left")
screen.onkey(snake_.right,"Right")

is_game_on = True
food = Food()

while is_game_on:
    screen.update()
    time.sleep(0.10)
    snake_.move()

    #detect food collution
    if snake_.head.distance(food) < 15:
        food.refresh()
        score_.increase_score()
        snake_.get_fat()

    #detect wall collution``
    wall = WIDTH/2 - 20
    wall_height = HEIGHT/2 - 20
    if snake_.head.xcor() > wall or snake_.head.xcor() < -wall or snake_.head.ycor() > wall_height or snake_.head.ycor() < -wall_height:
        is_game_on = False
        score_.game_over()

    #detect head collution with tail
    for segment in snake_.snake_body[1:]:
        if snake_.head.distance(segment) < 10:
            is_game_on = False
            score_.game_over()







screen.exitonclick()

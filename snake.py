from random import random
from turtle import Turtle
from time import sleep
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
WALL_X = 280
WALL_Y = 280

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]
    def create_snake(self):
        for i in range(3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.setheading(0)
            self.snake.append(t)
            t.goto(START_POSITION[i])
    def add_snake_len(self):
        t = Turtle("square")
        t.hideturtle()
        t.color("white")
        t.penup()
        t.setheading(0)
        self.snake.append(t)
        t.showturtle()
    def move(self):
        for i in range(len(self.snake)-1 , 0 , -1):
            x_cor = self.snake[i-1].xcor()
            y_cor = self.snake[i-1].ycor()
            self.snake[i].goto(x_cor,y_cor)
        self.snake[0].forward(MOVE_DISTANCE)
    def detect_collision(self):
        if self.snake_head.xcor() >= WALL_X or self.snake_head.xcor() <= -WALL_X:
            return True
        elif self.snake_head.ycor() >= WALL_Y or self.snake_head.ycor() <= -WALL_Y:
            return True
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
    def right(self):
    

        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

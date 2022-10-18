from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5,1)
        self.speed(0)
        randomX = random.randint(-270,270)
        randomY = random.randint(-270,270)
        self.goto(randomX,randomY)
    def randomFood(self):
        randomX = random.randint(-270,270)
        randomY = random.randint(-270,270)
        self.goto(randomX,randomY)

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.highest_score = "0"
        self.score = 0
        self.speed(0)
        self.goto(0,270)
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("White")
        #self.find_highest_score()
        self.write(f"Scoreboard:{self.score}",False,"center",("Arial",24,"normal"))
    def update_scoreboard(self,score):
        self.score = score
        self.clear()
        self.write(f"Scoreboard:{self.score}",False,"center",("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER!",False,"center",("Arial",48,"normal"))
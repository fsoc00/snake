from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
def screen_setup(Screen):
    Screen.setup(600,600)
    Screen.bgcolor("black")
    Screen.title("Snake Game")
    Screen.tracer(0)
def screen_listen(Screen):
    Screen.listen()
    Screen.onkey(snake.up,"w")
    Screen.onkey(snake.down,"s")
    Screen.onkey(snake.left,"a")
    Screen.onkey(snake.right,"d")
snake = Snake()
food = Food()
sb = Scoreboard()
while_game_is_on = True
game_score = 0
screen_setup(screen)
screen_listen(screen)
while while_game_is_on:
    screen.update()
    sb.update_scoreboard(game_score)
    if snake.detect_collision():
        while_game_is_on = False
        #sb.set_highest_score()
        sb.game_over()
    elif snake.snake_head.distance(food) < 17:
        game_score += 1
        food.randomFood()
        snake.add_snake_len()
    for i in snake.snake[1:]:
        if snake.snake_head.distance(i) < 10:
            #sb.set_highest_score()
            while_game_is_on = False
            sb.game_over()
    sleep(0.1)
    snake.move()
screen.exitonclick()
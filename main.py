from turtle import Screen
import time
from snake import Snake
import food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Sssnake")
screen.tracer(0)
food = food.Food()
snake = Snake()
scoreboard = Scoreboard()
game_on = True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.change_dir()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.incrase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()










screen.exitonclick()
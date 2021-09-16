#snake game nokia 3310
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
# setting up screen
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game nokia 3310")
screen.tracer(0)
# TODO 1. creating a snake body
snake=Snake()
# TODO 4. creating food
food=Food()
# TODO 5. keep track of score
scoreboard=ScoreBoard()
# TODO 3. control the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_game_on=True
# TODO 2. move whole body to move along without breaking
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
    # Detect collision with the wall
    if snake.head.xcor() >280 or snake.head.ycor() >280 or snake.head.xcor() <-280 or snake.head.ycor() <-280:
        scoreboard.game_over()
        is_game_on=False
    # Detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()

from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #DETECT COLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.change_place()
        snake.extend()
        score.add()

    #DETECT COLISION WITH WALL
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #DETECT COLISION WITH TAIL
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            score.reset()
            snake.reset()

















screen.exitonclick()
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def sle():
    time.sleep(1)


def stop():
    global move
    move = 0
    sc.stop()


def play():
    sc.update()
    global move
    move = 1


def exit_game():
    global is_game_on
    is_game_on = False


DIS_TO_WALL = 285
move = 1
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
s = Snake()
f = Food()
sc = Scoreboard()
# Taking Commands from Keyboard.
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")
screen.onkey(stop, "p")
screen.onkey(play, "c")
screen.onkey(exit_game, "q")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    s.move_snake(move=move)
    # Detects if snake eat food
    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        sc.increase()
    # Detect the head collision with of snake head with wall
    if s.head.xcor() > DIS_TO_WALL or s.head.xcor() < -DIS_TO_WALL or s.head.ycor() > DIS_TO_WALL or \
            s.head.ycor() < -DIS_TO_WALL:
        sc.reset()
        sc.game_over()
        is_game_on = False
    # Detect if snake collide with itself
    for segments in s.segment[1:]:
        if s.head.distance(segments) < 5:
            sc.reset()
            sc.game_over()
            is_game_on = False
screen.exitonclick()

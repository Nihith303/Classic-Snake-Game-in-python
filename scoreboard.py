from turtle import Turtle
from time import sleep
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("info.txt") as h:
                self.highscore = int(h.read())
        except FileNotFoundError:
            self.highscore = 0
        self.penup()
        self.color('white')
        self.update()
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Your score :{self.score} High Score:{self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.goto(0, 0)
            with open("info.txt", 'w') as a:
                a.write(str(self.highscore))
        self.update()
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=('Courier', 48, 'normal'))

    def stop(self):
        self.goto(0, 0)
        self.write("    Game Paused\nEnter 'c' to continue", align=ALIGNMENT, font=('TimesNewRoman', 28, 'normal'))

from turtle import Turtle
from random import randint, choice
list_color = ["green", "yellow", "orange", "red"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.color(choice(list_color))
        self.goto(rand_x, rand_y)
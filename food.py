from turtle import Turtle
import random
FOOD_POSITION=280
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        location_x=random.randint(-FOOD_POSITION,FOOD_POSITION)
        location_y = random.randint(-FOOD_POSITION, FOOD_POSITION)
        self.goto(location_x, location_y)

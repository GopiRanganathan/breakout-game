from turtle import Turtle
COLOR=['#cd0000', '#ef6000', '#f0cb01', '#15d500', '#0057e7']
YPOS = [300, 280, 260, 240, 220]
XPOS = [-275, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, 275]
class Bricks:
    def __init__(self):
        """create bricks of 12 pieces in each of 5 rows"""
        self.bricks = []
        self.create_bricks()
    
    def create_bricks(self):
        """to create bricks"""
        for i in range(5):
            for j in range(12):
                new_brick = Turtle()
                new_brick.color(COLOR[i])
                new_brick.shape('square')
                new_brick.shapesize(0.5, 2)
                new_brick.penup()
                new_brick.goto(x =XPOS[j], y= YPOS[i] )
                self.bricks.append(new_brick)

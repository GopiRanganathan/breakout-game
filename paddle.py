from turtle import Turtle
class Paddle():
    def __init__(self):
        """creates and manage paddle movement"""
        self.paddle_segment = []
        self.create_paddle()
        self.left_segment = self.paddle_segment[0]
        self.right_segment = self.paddle_segment[-1]
     

    def create_paddle(self):
        """to create paddle"""
        for xpos in [-40, -20, 0, 20, 40]:
            segment = Turtle()
            segment.color('white')
            segment.shape('square')
            segment.penup()
            segment.goto(x=xpos, y=-330)
            self.paddle_segment.append(segment)

    
    def move_right(self):
        """to move the paddle to right"""
        x = self.right_segment.xcor()
        y = -330
        if x <= 260 and x > -280:
            for seg in range(4):
                new_x = self.paddle_segment[seg+1].xcor()
                self.paddle_segment[seg].goto(new_x,y)
            self.right_segment.goto(x=x+20,y=y)

       

    def move_left(self):
        """to move the paddle to left"""
        x = self.left_segment.xcor()
        y = -330
        if x < 260 and x >= -280:
            for seg in range(4, 0, -1):
                new_x = self.paddle_segment[seg-1].xcor()
                self.paddle_segment[seg].goto(new_x,y)
            self.left_segment.goto(x=x-20, y=y)
        

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """creates ball and manages its movement"""
        super().__init__()
        self.color('#bcbcbc')
        self.shape('circle')
        self.penup()
        self.goto(-80, -20)
        self.x_move = 5
        self.y_move = -10
    
    def move(self):
        """to move ball continuously"""
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x_move, y + self.y_move)

    def collide_with_paddle(self, paddle):
        """to check ball if collided with paddle, bounce by changing its direction"""
        for seg in paddle:
            if self.distance(seg) < 10 and self.ycor() > -340:
                self.y_move *= -1

    def collide_with_wall(self):
        """to check ball if collide with upper or right or left wall, bounce"""
        if abs(self.xcor()) >= 290:
            self.x_move *= -1
        if self.ycor() > 330:
            self.y_move *= -1
    
    def collide_with_bricks(self, bricks, score):
        """to check ball if collide with any of the brick, remove the brick and add score"""
        for brick in bricks:
            if self.distance(brick) <25:
                self.y_move *= -1
                brick.hideturtle()
                brick.goto(x=400, y=400)
                bricks.remove(brick)
                score.score += 10
                score.update_score()


    def paddle_failed(self, score):
        """to check if ball fell, decrease the lives and go to start position"""
        if self.ycor() < -340:
            score.lives -= 1
            score.update_lives()
            self.goto(-80, -40)
from turtle import Turtle

class Score:
    def __init__(self):
        """manages score and lives"""
        self.score = 0
        self.lives = 3
        with open('score.txt') as file:
            value = file.read()
        self.high_score=int(value)
        self.score_board = self.create_turtle(140, 330)
        self.lives_board = self.create_turtle(-270, 330)
        self.heart = ''
        self.update_lives()
        self.update_score()


    def create_turtle(self, xpos, ypos):
        """to create turtle to write"""
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(x=xpos, y=ypos)
        return new_turtle
    
    def update_score(self):
        """to update score in the window"""
        self.score_board.clear()
        if self.high_score < self.score:
            self.high_score = self.score
        self.score_board.write(f"Score:{self.score} High:{self.high_score}", align="left", font=('Courier', 10, 'normal'))
    
    def update_lives(self):
        """to update lives in the window"""
        self.heart = ''
        self.lives_board.clear()
        for _ in range(self.lives):
            self.heart += '♥ ' 
        self.lives_board.write(f"{self.heart}", align="left", font=('Courier', 10, 'normal'))
    
    def update_highscore(self):
            """to update highscore in the file"""
            with open('score.txt', 'w') as file:
                file.write(str(self.high_score))

    



    
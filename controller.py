from turtle import Turtle
from score import Score

class Controller(Turtle, Score):
    def __init__(self):
        """to control pause, resume, game over and win"""
        super().__init__()
        self.is_pause = False
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 330)
        self.write("press P to pause", align='center', font=('Courier', 10, 'bold'))
       
    def show_game_over(self, score):
        """to show the user game over"""
        self.game_over = self.create_turtle(0, 0)
        score.update_highscore()
        self.game_over.write("Game Over!", align='center', font=('Courier',50, 'bold'))
        self.game_over.goto(0, -50)
        self.game_over.write("Press R to Restart or Q to Quit.", align='center', font=('Courier',20, 'bold'))

    def pause_info(self):
        """to pause the game and show the info"""
        self.is_pause = True
        self.pause = self.create_turtle(0,0)
        self.pause.write("press ← or → to move paddle\n   Press SPACE to resume", align='center', font=('Courier',20, 'bold'))
    
    def resume(self):
        """to resume the game"""
        self.pause.clear()
        self.is_pause = False
    
    def show_win(self, score):
        """to show the user win"""
        self.win = self.create_turtle(0, 0)
        score.update_highscore()
        self.win.write("You won!", align='center', font=('Courier',50, 'bold'))
        self.win.goto(0, -50)
        self.win.write("Press R to Restart or Q to Quit.", align='center', font=('Courier',20, 'bold'))





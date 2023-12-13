from turtle import Screen
import time
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from score import Score
from controller import Controller
import sys
import subprocess

# WINDOW SETUP

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 700)
screen.title('Breakout Game')
screen.tracer(0)

def restart_program():
    """ to rerun the program"""
    screen.bye()
    python = sys.executable
    subprocess.call([python] + sys.argv)

def quit():
    """to exit the program"""
    screen.bye()

# creating intsances
paddle = Paddle()
bricks = Bricks()
ball = Ball()
score = Score()
controller = Controller()

# GAME LOOP
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.03)
    screen.listen()
    # EVENTS and their functions
    screen.onkey(controller.pause_info, 'p')
    screen.onkey(controller.resume, 'space')
    screen.onkeypress(paddle.move_right, 'Right')
    screen.onkeypress(paddle.move_left, 'Left')
    if not controller.is_pause:
        ball.move()
    ball.collide_with_paddle(paddle.paddle_segment)
    ball.collide_with_wall()
    ball.collide_with_bricks(bricks.bricks, score)
    ball.paddle_failed(score)

# if lives are gone, stop the game
    if score.lives == 0:
        is_game_on = False
        controller.show_game_over(score)
    
    # if all the bricks are destroyed, win
    if bricks.bricks==[]:
        is_game_on = False
        controller.show_win(score)

# to quit or restart the game
screen.listen()
screen.onkey(restart_program, 'r')
screen.onkey(quit, 'q')



screen.exitonclick()


from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

if __name__ == "__main__":
    #Setup game screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    #Store objects in variable
    paddle_1 = Paddle((350, 0))
    paddle_2 = Paddle((-350, 0))
    ball = Ball()
    scoreboard =Scoreboard()

    #Bind movement commands to keys
    screen.listen()
    screen.onkey(paddle_1.up, "Up")
    screen.onkey(paddle_1.down, "Down")
    screen.onkey(paddle_2.up, "w")
    screen.onkey(paddle_2.down, "s")
    
    #Start game
    game_is_on = True
    while game_is_on:
        time.sleep(0.005)
        screen.update()
        ball.move()

        #Detect wall collision
        if (ball.ycor() > 280) or (ball.ycor() < -280):
            ball.bounce_y()

        #Detect paddle collision
        if (ball.distance(paddle_1) < 50 and ball.xcor() > 320) or (ball.distance(paddle_2) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        #Detect player 1 goals
        if (ball.xcor() < -380):
            ball.reset_pos()
            scoreboard.player_1_point()

        #Detect player 2 goals
        if (ball.xcor() > 380):
            ball.reset_pos()
            scoreboard.player_2_point()

    screen.exitonclick()
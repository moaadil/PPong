import turtle
import os

wn = turtle.Screen()
wn.title("MoPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops the window from updating(to increase the speed of the game)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)    #speed of animation ;(sets the sped to max possible speed)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  #square is 20p* 20p by default
paddle_b.penup() #dont draw anything
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15   #everytime the ball moves it moves by 0.15 diagonally 
ball.dy = -0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
	y = paddle_a.ycor() 
	y += 20         #add 20p 
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()	#updates the screen everytime the loop starts

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)  #moves diagonally
    ball.sety(ball.ycor() + ball.dy)  

	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #reverses  the direction
        os.system("aplay bounce.wav&") #in the background

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  #reverse if a wins
        score_a += 1   
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #using format method to print the score

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()  #to prevent overwriting(very fast)
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() -45):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() -45):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
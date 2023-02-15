import turtle 
import winsound

window = turtle.Screen()
window.title("Pong by Stanley")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0) # Stop the Window from updating, helps speed up the game

# Score Tracker
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation, sets speed to maximum 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup() # turtles draw line when moving, we dont want it. Initialises in centre of screen and moves to position
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.shapesize
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font =("Courier", 24, "normal"))

# Movement Functions
def paddle_a_up():
    if paddle_a.ycor() <= 230:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() >= -230:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() <= 230:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() >= -230:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)
    
    # Scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font =("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font =("Courier", 24, "normal"))

    # Paddle and Ball collision
    if (ball.xcor() > 335 and ball.xcor() < 345) and (ball.ycor() <= paddle_b.ycor() + 50 and ball.ycor() >= paddle_b.ycor() - 50):
        ball.setx(335)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)
    elif (ball.xcor() < -335 and ball.xcor() > -345) and (ball.ycor() <= paddle_a.ycor() + 50 and ball.ycor() >= paddle_a.ycor() - 50):
        ball.setx(-335)
        ball.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)
import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)
# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Ball movement
ball.dx, ball.dy = .1, -.1

# Scoring
left_score = 0
right_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {left_score} | Player B: {right_score}", align="center", font=("Courier", 18, "normal"))


# Function
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    if y >= 240:
        left_paddle.sety(240)
    else:
        left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    if y <= -240:
        left_paddle.sety(-240)
    else:
        left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    if y >= 240:
        right_paddle.sety(240)
    else:
        right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    if y <= -240:
        right_paddle.sety(-240)
    else:
        right_paddle.sety(y)


# Keyboard Bindings
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

# Main Game Loop
while True:
    win.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        left_score += 1
        pen.clear()
        pen.write(f"Player A: {left_score} | Player B: {right_score}", align="center", font=("Courier", 18, "normal"))
        ball.dx = -.1
        ball.dy = .1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        right_score += 1
        pen.clear()
        pen.write(f"Player A: {left_score} | Player B: {right_score}", align="center", font=("Courier", 18, "normal"))
        ball.dx = .1
        ball.dy = .1

    # Collision Physics
    if 340 < ball.xcor() < 350 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.dx *= -1.1
        ball.dy *= 1.1

    if -350 < ball.xcor() < -340 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50:
        ball.dx *= -1.1
        ball.dy *= 1.1

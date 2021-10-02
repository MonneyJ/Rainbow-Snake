import turtle
import time
import random

"""
This Rainbow Snake game was programmed by Monney Joshua
as a kid i read a story book about two young siblings who were explorers,they went to find a rainbow snake
it was told that the rainbow snake was the one which created rivers and streams in the forest when it moved along
the ground with its body
"""
delay = 0.1

# window background
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Rainbow Snake(Monney Studios)")
window.tracer(0)

# snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()
snake.color("white")
snake.goto(0, 0)
snake.direction = "stop"

# snake food
snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.penup()
snake_food.shape('circle')
snake_food.color('red')
x = random.randint(-280, 280)
y = random.randint(-280, 240)
snake_food.goto(x, y)

score = 0
high_score = 0

# score board
snake_score = turtle.Turtle()
snake_score.speed(0)
snake_score.penup()
snake_score.color("white")
snake_score.goto(-14, 250)
snake_score.hideturtle()
snake_score.write(f"Scores: {score}\t\tHigh score: {high_score}", align="center", font=("Courier", 18, "bold"))

# name
name = turtle.Turtle()
name.speed(0)
name.penup()
name.color("white")
name.goto(290, -290)
name.hideturtle()
name.write("Monney Studios", align="right", font=("Scream Real", 8, "normal"))

# snake bodies
snake_bodies = []


# switch directions
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_left():
    if snake.direction != "right":
        snake.direction = "left"


# animate snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        y += 20
        snake.sety(y)

    if snake.direction == "down":
        y = snake.ycor()
        y -= 20
        snake.sety(y)

    if snake.direction == "right":
        x = snake.xcor()
        x += 20
        snake.setx(x)

    if snake.direction == "left":
        x = snake.xcor()
        x -= 20
        snake.setx(x)

    # user input
    window.listen()
    window.onkeypress(snake_up, "Up")
    window.onkeypress(snake_down, "Down")
    window.onkeypress(snake_right, "Right")
    window.onkeypress(snake_left, "Left")


# game loop
while True:

    # boundary limit
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        for segments in snake_bodies:
            segments.goto(1000, 1000)

        snake_bodies.clear()
        score = 0
        snake_score.clear()
        snake_score.write(f"Scores: {score}\t\tHigh score: {high_score}", align="center",
                          font=("Courier", 18, "bold"))

    if snake.distance(snake_food) < 20:
        snake_food.goto(1000, 1000)
        snake_food.clear()
        snake_food = turtle.Turtle()
        snake_food.speed(0)
        snake_food.penup()
        snake_food.goto(x, y)
        food_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        pick_colours = random.choice(food_colours)
        food_shapes = ['triangle', 'circle']
        pick_shapes = random.choice(food_shapes)
        snake_food.color(pick_colours)
        snake_food.shape(pick_shapes)
        x = random.randint(-280, 280)
        y = random.randint(-260, 240)
        snake_food.goto(x, y)

        if score == high_score:
            high_score += 10
        score += 10
        snake_score.clear()
        snake_score.write(f"Scores: {score}\t\tHigh score: {high_score}", align="center",
                          font=("Courier", 18, "bold"))

        new_snake_body = turtle.Turtle()
        new_snake_body.speed(0)
        new_snake_body.penup()
        new_snake_body.shape("square")
        body_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        pick_body_colours = random.choice(body_colours)

        new_snake_body.color(pick_body_colours)
        snake_bodies.append(new_snake_body)

    for index in range(len(snake_bodies) - 1, 0, -1):
        x = snake_bodies[index - 1].xcor()
        y = snake_bodies[index - 1].ycor()
        snake_bodies[index].goto(x, y)

    if len(snake_bodies) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_bodies[0].goto(x, y)

    move()
    for segments in snake_bodies:
        if segments.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            for segment in snake_bodies:
                segment.goto(1000, 1000)

            snake_bodies.clear()
            score = 0
            snake_score.clear()
            snake_score.write(f"Scores: {score}\t\tHigh score: {high_score}", align="center",
                              font=("Courier", 18, "bold"))

    time.sleep(delay)
    window.update()

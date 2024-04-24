import turtle
import random
import time

delay = 0.1
score = 0
Highestscore = 0

# snake bodies
bodies = []

# getting screen and canvas
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("yellow")
s.setup(width=600, height=600)

# creating snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
# func to hide turtle
food.ht()
# 1st food display at 0,200
food.goto(0, 200)
food.st()

# score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0 | Highest Score: 0")

# creating functions for movement of snake


def moveup():
    if head.direction != "down":
        head.direction = "up"


def movedown():
    if head.direction != "up":
        head.direction = "down"


def moveleft():
    if head.direction != "right":
        head.direction = "left"


def moveright():
    if head.direction != "left":
        head.direction = "right"


def movestop():
    head.direction = "stop"


# moving snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Event handling | Key Mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# main loop
while True:
    s.update()  # this will update the screen

    # collinsion with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # check for the collison with food
    if head.distance(food) < 20:
        # using random for providing food at new position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)  # append new body

        # increase the Score
        score += 10
        # change delay
        delay -= 0.001
        # update the highest score
        if score > Highestscore:
            Highestscore = score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, Highestscore))

    # move the snake body
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check for head collisions with the body segments
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the bodies
            for body in bodies:
                body.goto(1000, 1000)
            # clear the bodies list
            bodies.clear()

            # reset the score
            score = 0

            # reset the delay
            delay = 0.1

            # update the score display
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(
                score, Highestscore))

    time.sleep(delay)

turtle.mainloop()

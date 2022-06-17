# DRAW A RANDOM WALK

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random.color = (r, g, b)
    return random.color

direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(250):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


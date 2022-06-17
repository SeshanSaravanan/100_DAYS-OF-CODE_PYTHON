# Drawing a square shape
from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.down()

screen = Screen()
screen.exitonclick()
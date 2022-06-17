# Drawing a square shape
from turtle import Turtle, Screen

square = Turtle()
square.shape("turtle")
square.color("black")

for _ in range(4):
    square.forward(100)
    square.right(90)

screen = Screen()
screen.exitonclick()
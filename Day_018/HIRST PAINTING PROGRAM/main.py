# import colorgram
#
# The below commented code are to extract the colors in the image
# rgb_colors = []
# colors = colorgram.extract('download.jpg', 20)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")
color_list = [(236, 234, 230), (238, 229, 234), (228, 238, 232), (227, 233, 240), (237, 40, 115), (142, 27, 70),
              (219, 162, 59),
              (238, 71, 36), (14, 144, 89), (182, 166, 43), (31, 126, 191), (54, 190, 229), (245, 221, 50),
              (179, 41, 96),
              (128, 190, 101), (78, 27, 81), (39, 172, 118), (250, 225, 1), (210, 61, 31), (214, 131, 167)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_counts in range(1, (number_of_dots + 1)):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

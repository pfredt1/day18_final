import random
import turtle
from turtle import Turtle
from turtle import Screen
turtle.colormode(255)
import colorgram
colorgram.extract
colors = colorgram.extract('file.png', 50)
tim = Turtle()



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
# tim.color(random_color())


rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
x_pos = -300
y_pos = 300
tim.penup()




# get color
# make dot
# move to new pos
# repeat 7 times




count = 0
for z in range(10):

    for y in range(10):
        tim.setpos(x_pos, y_pos)
        tim.dot(20, random.choice(rgb_colors))
        x_pos += 50

        count += 1
    x_pos -= 500

    y_pos -= 50
    tim.setpos(x_pos, y_pos)
print("hi")









screen = Screen()
screen.exitonclick()

#Lola Weis
#CS-175
#Turtle Graphic


import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10


turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


for x in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
print("STOP")



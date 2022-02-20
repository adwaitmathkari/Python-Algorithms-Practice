from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")

step = 100
step2 = 0
def draw_square(length,angle):
    global step2
    for b in range (0,4):
            turtle.forward(length+step2)
            turtle.right(angle+b)
    step2+=1
    if step2<step:
        draw_square(length, angle)
        

draw_square(100,90)
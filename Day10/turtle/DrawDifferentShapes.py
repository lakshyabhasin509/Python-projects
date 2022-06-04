from turtle import Turtle,Screen
import random
timm=Turtle()
colors=["DeepSkyBlue","DeepSkyBlue","OrangeRed","Magenta","LightSalmon","Cyan"]
def drawPolygons(number):
    if(number<3):return
    curr=3
    timm.speed(curr)
    ran=random

    timm.pensize(2)
    while curr<=number:
        timm.pencolor(random.choice(colors))
        for _ in range(curr):

            timm.forward(100)
            angle=360/curr
            timm.right(angle)
        curr+=1

drawPolygons(10)

screen=Screen()

screen.exitonclick()

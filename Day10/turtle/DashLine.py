from turtle import Turtle,Screen

timm=Turtle()

def createDashLine(distance):
    flag=0
    i=1
    while i<distance:
        i+=10
        timm.forward(10)
        if(flag==0):
            timm.penup()
            flag=1
        else:
            timm.pendown()
            flag=0

createDashLine(100)



screen=Screen()

screen.exitonclick()

from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("red")
t.hideturtle()
def polygon(length,width,angle):
    t.setheading(angle)
    for steps in range(20):
        t.fd(width)
        t.left(angle)
        t.fd(length)

polygon(50,25,30)     

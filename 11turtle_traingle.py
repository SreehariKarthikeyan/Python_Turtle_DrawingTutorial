from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("red")
t.hideturtle()
def triangle(length,angle=120):
    for steps in range(3):
        t.fd(length)
        t.left(angle)
triangle(200)
    

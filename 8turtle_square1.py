from turtle import Turtle
t=Turtle()
t.screen.bgcolor("black")
t.color("red")
t.hideturtle()
def square(length):
    for steps in range(4):
        t.fd(length)
        t.left(90)
square(100)

    
    

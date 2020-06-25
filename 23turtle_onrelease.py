from turtle import Turtle
t=Turtle()
def draw_circle(x,y):
    t.circle(50)

def erase_drawing(x,y):
    t.clear()

t.onclick(draw_circle)
t.onrelease(erase_drawing)

from turtle import Turtle
import random
t=Turtle()
t.screen.bgcolor("black")
def randomwalk(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(["blue","red","green"]))
        random.choice([right,left])
        t.fd(distance)

randomwalk(100,50)        
               

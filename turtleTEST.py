import turtle
import math 
screen = turtle.Screen()
t = turtle.Turtle()

turtlepower = []

turtle.tracer(0, 0)
for i in range(999):
    t.forward(10)
    t.left(math.sin(i/10)*25)
    t.left(20)


for i in range(999):
    turtle.stamp()

turtle.update()
turtle.done()
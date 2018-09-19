import turtle
jack = turtle.Turtle()
def polygon(t, n, length):
    angle = 360/ n 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(jack, 7, 70)

import turtle
my_turtle = turtle.Turtle()
my_turtle.right(90)
my_turtle.forward(80)
my_turtle.left(90)
my_turtle.forward(80)
my_turtle.left(90)
my_turtle.forward(80)
my_turtle.left(90)
my_turtle.forward(80)
my_turtle = turtle.Turtle
import turtle
jack = turtle.Turtle()
def polygon(t, n, length):
    angle = 360/ n 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(jack, 7, 70)
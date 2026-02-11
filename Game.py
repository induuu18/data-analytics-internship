import turtle
pi = turtle.Turtle()
pi.fd(150)
pi.lt(60)
pi.fd(150)
pi.lt(60)
pi.fd(150)
pi.lt(60)
pi.fd(150)
pi.lt(60)
pi.fd(150)
pi.lt(60)
pi.fd(150)
pi.lt(60)

#OR
import turtle
piggy = turtle.Turtle()
def polygon(L,n):
    angle = 360/n
    for i in range (n):
        piggy.fd(L)
        piggy.lt(angle)
polygon(150,6)
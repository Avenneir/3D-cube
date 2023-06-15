import turtle
import time

l = int(input("Enter Cube Length: "))
a = int(input("Enter Cube Angle: "))

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D Cube")
s.screensize(800,500,bg = "black")
t.pencolor("gold")
t.pensize(5)

def square(l):
    for i in range(4):
        t.forward(l)
        t.left(90)

def cube(l,a):
    square(l)
    t.left(a)
    t.forward(l)
    #time.sleep(2)
    t.right(a)
    #time.sleep(2)
    square(l)

    t.left(90)
    t.forward(l)
    t.left(90+a)
    t.forward(l)
    t.right(a+180)
    t.forward(l)
    t.left(a)
    t.forward(l)
    t.right(a+90)
    t.forward(l)
    t.right(90-a)
    t.forward(l)

for i in range(10):
    cube(l,a)
    t.forward(l)
turtle.done()
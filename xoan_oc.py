import turtle

t=turtle.Turtle()

d = int(input("nhap do rong cua vong xoan oc: "))

step = 0.1

t.goto(0,0)

while (t.distance(0,0) < d):
    t.forward(step)
    t.left(10)
    step+=0.1
    
turtle.done()
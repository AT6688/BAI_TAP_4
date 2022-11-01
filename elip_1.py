import turtle

t=turtle.Turtle()

r=int(input("nhap vao ban kinh r cua elip: "))

step = 1

t.right(45)

while(step < 3):
    t.circle(r,90)
    t.circle(r/2,90)
    step+=1

turtle.done()
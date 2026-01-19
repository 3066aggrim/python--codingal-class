import turtle
turtle.Screen().setup(300, 400)
decagon = turtle.Turtle()
numsides = 10
sidelength = 100
angle = 360.0/numsides

for i in range(numsides):
    decagon.forward(sidelength)
    decagon.right(angle)

turtle.done()

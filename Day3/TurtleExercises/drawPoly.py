from turtle import *


def drawCircle(xcoord, ycoord, wide =10, diameter=60, color="black"):
    setPosition(xcoord, ycoord)
    pencolor(color)
    width(wide)
    circle(diameter)

def setPosition(x, y):
    penup()
    goto(x, y)
    pendown()

def drawShape(numberofSides, sideLength, xcoord, ycoord):
    setPosition(xcoord, ycoord)
    numSide = numberofSides #5
    side_length = sideLength #70
    angle = 360 / numSide 
    for i in range(numSide):
        forward(side_length)
        right(angle)

def drawStar(size, xcoord, ycoord):
    setPosition(xcoord, ycoord)
    for i in range(6):
        left(216)
        forward(size)


# drawShape(3, 60)
# drawShape(4, 60)
# drawShape(5, 60)


# triangle = drawShape(3, 60, 200, 200)
# square = drawShape(4, 60, 200, 140)
# pentagon = drawShape(5, 60, 200, 60)
# hexagon = drawShape(6, 40, 200, -40)
# octagon = drawShape(8, 30, 100, 200)
# star = drawStar(60, 140, 100)




# if __name__ == "__main__":
#     # triangle()
#     # square()
#     mainloop()
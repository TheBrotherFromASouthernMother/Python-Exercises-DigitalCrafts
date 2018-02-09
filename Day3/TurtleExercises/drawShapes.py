from turtle import *


def drawCircle(xcoord, ycoord, wide =10, size=60, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    width(wide)
    color(linecolor)
    #begin_fill()  
    if fillstate== True:
        begin_fill()  
        circle(size)
        end_fill()
    else:
        circle(size)
    
   # end_fill()

def setPosition(x, y):
    penup()
    home()
    goto(x, y)
    pendown()



def drawShape(numberofSides, size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    numSide = numberofSides #5
    side_length = size #70
    angle = 360 / numSide 
    color(linecolor)
    if fillstate == True:
       begin_fill()
       for i in range(numSide):
            forward(side_length)
            left(angle)
       end_fill()
    else:
        for i in range(numSide):
            forward(side_length)
            right(angle)


def drawShapeInverted(numberofSides, size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    numSide = numberofSides #5
    side_length = size #70
    angle = 360 / numSide 
    color(linecolor)
    if fillstate == True:
       begin_fill()
       for i in range(numSide):
            forward(side_length)
            right(angle)
       end_fill()
    else:
        for i in range(numSide):
            forward(side_length)
            right(angle)

    

def drawStar(size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    color(linecolor)
    if fillstate == True:
        begin_fill()
        for i in range(6):
            forward(size)
            left(216)
        end_fill()
    else:
        for i in range(6):
            forward(size)
            left(216)

   

def drawRhombus(size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    longside = 20 * size
    sides = 12 * size
    color(linecolor)
    begin_fill()
    forward(longside)
    left(110)
    forward(sides)
    left(70)
    forward(sides)
    left(70)
    forward(sides)
    end_fill()


def drawRhombusInverted(size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    longside = 20 * size
    sides = 12 * size
    color(linecolor)
    begin_fill()
    forward(longside)
    right(110)
    forward(sides)
    right(70)
    forward(sides)
    right(70)
    forward(sides)
    end_fill()


def drawParallelogram(size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    sides = 12 * size
    color(linecolor)
    begin_fill()
    forward(sides)
    left(110)
    forward(sides)
    left(70)
    forward(sides)
    left(110)
    forward(sides)
    end_fill()

def drawParallelogramInverted(size, xcoord, ycoord, linecolor="black", fillstate=False):
    setPosition(xcoord, ycoord)
    sides = 12 * size
    color(linecolor)
    begin_fill()
    forward(sides)
    right(110)
    forward(sides)
    right(70)
    forward(sides)
    right(110)
    forward(sides)
    end_fill()





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
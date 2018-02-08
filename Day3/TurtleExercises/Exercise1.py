from turtle import *
shape("turtle")


def drawTriangle(somefunction, direction):
    somefunction(direction)
    #draw a triangle
    for i in range(3):
        right(120)
        forward(100)

def drawStar(somefunction, direction):
    somefunction(direction)
    for i in range(6):
        right(216)
        forward(50)

def drawSquare(someFunction, direction):
    for i in range (4):
        

def setPosition(direction):
    direction = direction.lower()
    if direction == "left":
        penup()
        goto(-200, -200)
        down()
    elif direction == 'right':
        penup()
        goto(200, -200)
        down()
    elif direction == "top-right":
        penup()
        goto(200, 200)
        down()
    elif direction == "top-left":
        penup()
        goto(-200, 200)
        down()


#draw a pentagon
def drawPolygon(numberSide, sideLength, name, firstShape=False, lastShape=False, someFunction=None, direction=None):
    if someFunction:
        someFunction(direction)
    numSide = numberSide #5
    side_length = sideLength #70
    angle = 360 / numSide 
    if firstShape == True:
        home()
    begin_poly()
    for i in range(numSide):
        forward(side_length)
        left(angle)
        forward(side_length)
    end_poly()
    p = get_poly()
    register_shape(name, p)
    if lastShape:
        mainloop()
    

pentagon = drawPolygon(5, 30, "pentagon", True)

octagon = drawPolygon(8, 30, "octagon", False, False, setPosition, "right" )

star = drawStar(setPosition, "top-right")

triangle = drawTriangle(setPosition, "top-left")

hexagon = drawPolygon(6, 30, "hexagon",False, True, setPosition, "left")

print("trueifthing")

if __name__ == "__main__":
    pentagon()
    octagon()
    star()
    triangle()
    hexagon()
        
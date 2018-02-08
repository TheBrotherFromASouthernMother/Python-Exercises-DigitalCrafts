from turtle import *

shape("turtle")

#draw a triangle
# right(120)
# forward(200)
# right(120)
# forward(200)
# right(120)
# forward(200)


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

#draw a hexagon
hexagon = drawPolygon(6, 30, "hexagon",False, True, setPosition, "left")

print("trueifthing")

if __name__ == "__main__":
    pentagon()
    octagon()
    hexagon()
        
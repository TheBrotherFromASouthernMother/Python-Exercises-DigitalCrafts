from turtle import *

shape("turtle")

#draw a triangle
# right(120)
# forward(200)
# right(120)
# forward(200)
# right(120)
# forward(200)




#draw a pentagon
def drawPolygon(numberSide, sideLength, name):
    numSide = numberSide #5
    side_length = sideLength #70
    angle = 360 / numSide 
    home()
    begin_poly()
    for i in range(numSide):
        fd(side_length)
        left(angle)
        fd(side_length)
    end_poly()
    p = get_poly()
    register_shape(name, p)
    mainloop()

pentagon = drawPolygon(5, 70, "pentagon")

if __name__ == "__main__":
        pentagon()
        
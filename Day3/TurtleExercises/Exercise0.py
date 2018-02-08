from turtle import *

shape("turtle")


# for i in range(6):
#     right(216)
#     forward(150)


# #draw a cirlce
# up()
# forward(50)
# left(90)
# forward(50)
# left(90)

def drawCirlce(wide=20, diameter=120 ):
    pencolor('#005ce6')
    width(wide)
    circle(diameter)

# move into position
def position():
    up()
    forward(50)
    left(90)
    forward(50)
    left(90)
    down()

def drawSquare():
    # draw the square
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)

if __name__ == "__main__":
    drawCirlce()
    mainloop()



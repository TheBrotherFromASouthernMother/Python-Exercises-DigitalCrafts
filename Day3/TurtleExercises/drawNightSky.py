from drawShapes import *
from turtle import bgcolor
from random import randint

# def Size():
#     randomSize = randint()
#     if randomSize < 75:
#         return randomSize
#     else:
#         randomSize = 30
#         return randomSize
# def coordinate():
#     randomCoord = randint()
#     if randomCoord < 300
#         return randomCoord
#     else:
#         randomCoord -= 100

def printSky():
    bgcolor("#6762A6")
    for i in range(300):
        drawStar(randint(2, 30),randint(-300, 300),randint(-300, 300), "white", True) 


speed(0)
printSky()
mainloop()
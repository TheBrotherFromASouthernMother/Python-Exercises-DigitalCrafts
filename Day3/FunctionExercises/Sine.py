from matplotlib import pyplot as plot

from math import sin as sine

def f(x):
    return sine(x)

def printPlots():
    xs = []
    ys = []
    for x in range(-5, 6):
        xs.append(x)
        ys.append(f(x))
    plot.plot(xs, ys)
    plot.show()
    

printPlots()
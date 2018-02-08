from numpy import arange

from matplotlib import pyplot as plot 

from math import sin

def f(x):
    return sin(x)

def printPlots():
    xs = []
    ys = []
    for x in arange(-5, 6, 0.1):
        xs.append(x)
        ys.append(f(x))
    plot.plot(xs, ys)
    plot.show()
    

printPlots()
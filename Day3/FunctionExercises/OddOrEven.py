import matplotlib
from matplotlib import pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

def printPlots():
    xs = []
    ys = []
    for x in range(-5, 6):
        xs.append(x)
        ys.append(f(x))
    plot.bar(xs, ys)
    plot.show()


printPlots()
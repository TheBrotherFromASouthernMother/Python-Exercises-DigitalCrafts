import matplotlib
from matplotlib import pyplot as plot

def f(x):
    return x ** 2

xs = []
ys = []

for x in range(-100, 101):
    xs.append(x)
    ys.append(f(x))


plot.plot(xs, ys)
plot.show()
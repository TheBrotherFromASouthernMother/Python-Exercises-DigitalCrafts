import matplotlib
from matplotlib import pyplot as plot


def f(x):
    # put your code here
    return x + 1
xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()


degreesCelsius = float(input("What's the temperature in C? "))
degreesFarenheit = (1.8 * degreesCelsius) + 32.0

from matplotlib import pyplot as plot 

def f(x):
    return (1.8 * x) + 32.0


def plotTemp(x):
    xs = [x]
    ys = [f(x)]

    plot.plot(xs, ys, marker="o", markersize=5, color="blue")
    plot.show()

if __name__ == "__main__":
    plotTemp(degreesCelsius)

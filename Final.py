import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy


def caluloX(x, y):
    print("Printeando para X: ", a*x + b * y)
    # return a*x + b * y
    return 0
def caluloY(x, y):
    print("Printeando para Y: ", c * x + d * y )
    # return c * x + d * y
    return 0

def valoresFuturos(valueX, valueY, counter):
    if counter > 10: return
    plt.scatter(valueX, valueY, c='#1B58D6')
    plt.draw()
    valoresFuturos(valueX + caluloX(valueX,valueY)/10,valueY + caluloY(valueX,valueY)/100, counter +1)

def valoresPasados(valueX, valueY, counter):
    if counter > 10: return
    plt.scatter(valueX, valueY, c='#3DA416')
    plt.draw()
    valoresFuturos(valueX - caluloX(valueX,valueY)/10,valueY - caluloY(valueX,valueY)/100, counter +1)


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        if event.inaxes != self.line.axes: return
        xdata = event.xdata
        ydata = event.ydata
        valoresFuturos(xdata, ydata, 0)
        valoresPasados(xdata, ydata, 0)


a = int(input("ingrese valor a:"))
b = int(input("ingrese valor b:"))
c = int(input("ingrese valor c:"))
d = int(input("ingrese valor d:"))

p = -(a + d)
q = (a * d) - (b * c)

tempMatrix1 = sympy.Matrix([[0, 0], [0, 0]])
tempMatrix2 = sympy.Matrix([[0, 0], [0, 0]])

print(p, q)
if (math.pow(p, 2) - 4 * q) > 0:
    lambda1 = (-p - (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    lambda2 = (-p + (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    print("lambdas: ", lambda1, lambda2)

    tempMatrix1 = sympy.Matrix([[a - lambda1, b], [c, d - lambda1]])
    tempMatrix2 = sympy.Matrix([[a - lambda2, b], [c, d - lambda2]])




fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

t = np.array(range(-5, 5))
null1 = tempMatrix1.nullspace()
null2 = tempMatrix2.nullspace()

n1 = t * null1[0][0] / null1[0][1]
n2 = t * null2[0][0] / null2[0][1]

null2 = tempMatrix2.nullspace

x = np.array(range(-5, 5))
nulclina_x = (-a * x) / b
nulclina_y = (-c * x) / d

plt.plot(t, n1)
plt.plot(t, n2)
plt.plot(x, nulclina_x, label='Nuclina X')

plt.plot(x, nulclina_y, label='Nuclina Y')
plt.legend()

plt.show()

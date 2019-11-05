import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy


def caluloX(x, y):
    derivadax = (a*x + b*y)**2
    derivaday = (c*x + d*y)**2
    normalizado = math.sqrt(derivadax + derivaday)
    return ((a/normalizado)*x + (b/normalizado) * y)/10

def caluloY(x, y):
    derivadax = (a*x + b*y)**2
    derivaday = (c*x + d*y)**2
    normalizado = math.sqrt(derivadax + derivaday)
    return ((c/normalizado) * x + (d /normalizado) * y)/10

def valoresFuturos(valueX, valueY, counter):
    if counter > 100: return
    plt.scatter(valueX, valueY, c='#1B58D6', s= 10)
    plt.draw()
    valoresFuturos(valueX + caluloX(valueX,valueY),valueY + caluloY(valueX,valueY), counter +1)

def valoresPasados(valueX, valueY, counter):
    if counter > 100: return
    plt.scatter(valueX, valueY, c='#3DA416', s= 10)
    plt.draw()
    valoresPasados(valueX - caluloX(valueX,valueY),valueY - caluloY(valueX,valueY), counter +1)


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


a = float(input("ingrese valor a:"))
b = float(input("ingrese valor b:"))
c = float(input("ingrese valor c:"))
d = float(input("ingrese valor d:"))

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
ax.set_title('Clickea para ver los valores futuros')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

t = np.array(range(-10, 10))
null1 = tempMatrix1.nullspace()
null2 = tempMatrix2.nullspace()

n1 = t * null1[0][0] / null1[0][1]
n2 = t * null2[0][0] / null2[0][1]

n1 = np.array(n1, dtype=np.complex_)
n2 = np.array(n2, dtype=np.complex_)

null2 = tempMatrix2.nullspace

x = np.array(range(-10, 10))
nulclina_x = (-a * x) / b
nulclina_y = (-c * x) / d

if (not np.iscomplex(n1).any()):
    plt.plot(t, n1)
if (not np.iscomplex(n2).any()):
    plt.plot(t, n2)

plt.plot(x, nulclina_x, '--', label='Nuclina X')
plt.plot(x, nulclina_y, '--', label='Nuclina Y')
plt.legend()

plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy


def caluloX(x, y):
    derivadax = (a*x + b*y)**2
    derivaday = (c*x + d*y)**2
    normalizado = math.sqrt(derivadax + derivaday)
    return ((a/normalizado)*x + (b/normalizado) * y)/2

def caluloY(x, y):
    derivadax = (a*x + b*y)**2
    derivaday = (c*x + d*y)**2
    normalizado = math.sqrt(derivadax + derivaday)
    return ((c/normalizado) * x + (d /normalizado) * y)/2

def valoresFuturos(valueX, valueY, counter):
    if counter > cantidadPuntps: return
    plt.scatter(valueX, valueY, c='#1B58D6', s= 3)
    plt.draw()
    valoresFuturos(valueX + caluloX(valueX,valueY),valueY + caluloY(valueX,valueY), counter + 1)

def valoresPasados(valueX, valueY, counter):
    if counter > cantidadPuntps: return
    plt.scatter(valueX, valueY, c='#3DA416', s= 3)
    plt.draw()
    valoresPasados(valueX - caluloX(valueX,valueY),valueY - caluloY(valueX,valueY), counter + 1)


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
cantidadPuntps = float(input("ingrese la cantidad de puntos a graficar:"))

p = -(a + d)
q = (a * d) - (b * c)

tempMatrix1 = sympy.Matrix([[0, 0], [0, 0]])
tempMatrix2 = sympy.Matrix([[0, 0], [0, 0]])

print("El valor de P es: ", p)
print("El valor de Q es: ", q)

if (math.pow(p, 2) - 4 * q) > 0:
    lambda1 = (-p - (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    lambda2 = (-p + (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    print("lambdas: ", lambda1, lambda2)

    tempMatrix1 = sympy.Matrix([[a - lambda1, b], [c, d - lambda1]])
    tempMatrix2 = sympy.Matrix([[a - lambda2, b], [c, d - lambda2]])


fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([-25, 25, -25, 25])
ax.set_title('Clickea para ver los valores futuros')
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

t = np.array(range(-25, 25))
null1 = tempMatrix1.nullspace()
null2 = tempMatrix2.nullspace()

n1 = np.array(range(-25, 25))
n2 = np.array(range(-25, 25))

n1 = np.array(n1, dtype=np.complex_)
n2 = np.array(n2, dtype=np.complex_)

try:
    graficar = True
    n1 = t * (null1[0][0] / null1[0][1])
    n2 = t * (null2[0][0] / null2[0][1])
except IndexError:
    graficar = False
    n1 = np.array(range(-25, 25))
    n2 = np.array(range(-25, 25))


null2 = tempMatrix2.nullspace

x = np.array(range(-25, 25))
if(b != 0):
    nulclina_x = (-a * x) / b
else:
    nulclina_x = 0 * x

if(d != 0):
    nulclina_y = (-c * x) / d
    graficarInvertido = False
else:
    graficarInvertido = True
    nulclina_y = 0 * x


print(graficar)
if (not np.iscomplex(n1).any() and graficar):
    try:
        plt.plot(t, n1)
        print("")
    except Exception:
        print("")
if (not np.iscomplex(n2).any() and graficar):
    try:
        plt.plot(t, n2)
        print("")
    except Exception:
        print("")

plt.plot(x, nulclina_x, '--', label='Nuclina X')
if (not graficarInvertido):
    plt.plot(x, nulclina_y, '--', label='Nuclina Y')
else:
    plt.plot(nulclina_y, x, '--', label='Nuclina Y')
plt.legend()

plt.show()
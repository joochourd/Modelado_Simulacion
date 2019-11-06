# Modelado y simulación

## Un tp sobre los temas vistos en la materia de modelado y simulacion

El trabajo fue realizado en python, usando las librerias numpy para operaciones algebraicas sobre matrices y matplot para graficar los diferentes componentes necesarios.

A continuacion explicaremos las diferentes partes del codigo: 

### Node

Aqui pedimos los diferentes inputs que necesitamos para construir la matriz y la cantidad de puntos que se desea graficar:

a = float(input("ingrese valor a:"))
b = float(input("ingrese valor b:"))
c = float(input("ingrese valor c:"))
d = float(input("ingrese valor d:"))
cantidadPuntps = float(input("ingrese la cantidad de puntos a graficar:"))

#### Conseguimos los valores de P y Q

p = -(a + d)
q = (a * d) - (b * c)


#### Observamos si encontramos raices reales y si es asi las calculamos 

if (math.pow(p, 2) - 4 * q) > 0:
    lambda1 = (-p - (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    lambda2 = (-p + (math.sqrt(math.pow(p, 2) - 4 * q))) / 2
    print("lambdas: ", lambda1, lambda2)

    tempMatrix1 = sympy.Matrix([[a - lambda1, b], [c, d - lambda1]])
    tempMatrix2 = sympy.Matrix([[a - lambda2, b], [c, d - lambda2]])

#### Calculamos los null spaces usando funciones propias de la libreria numpy
    null1 = tempMatrix1.nullspace()
    null2 = tempMatrix2.nullspace()

## Por ultimo, si es posible, graficamos los autovectores
    print(graficar)
    if (not np.iscomplex(n1).any() and graficar):
        try:
            plt.plot(t, n1)
        except Exception:
            print("No se pueden graficar")
    if (not np.iscomplex(n2).any() and graficar):
        try:
            plt.plot(t, n2)
        except Exception:
            print("No se pueden graficar")

## Que sucede cuando clickeamos sobre un punto ?
### Definimos una funcion que recibe los puntos y grafica los valores futuros y pasados
    def __call__(self, event):
    if event.inaxes != self.line.axes: return
    xdata = event.xdata
    ydata = event.ydata
    valoresFuturos(xdata, ydata, 0)
    valoresPasados(xdata, ydata, 0)

## Funciones

### Las funciones de futuros y pasados funcionan de la misma manera pero con distinto signo. Por temas de simplicidad, solo explicaremos la funcion valoresFuturos (xdata, ydata)

    def valoresFuturos(valueX, valueY, counter):
    if counter > cantidadPuntps: return
    plt.scatter(valueX, valueY, c='#1B58D6', s= 3)
    plt.draw()
    valoresFuturos(valueX + caluloX(valueX,valueY),valueY + caluloY(valueX,valueY), counter + 1)

Dentro de esta funcion podemos ver que empezamos checkeando por una condicion de corte y si no se cumple procedemos a graficar el punto seleccionado. 
A continuacion llamamos a la funcion calculoX y calculoY para obtener los valores del gradiente de la funcion en el punto seleccionado. Con estos valores, llamamos recursivamente a la funcion de valores futuros para graficar el proximo punto

## Como funciona calculoX y calculoY ?

    derivadax = (a*x + b*y)**2
    derivaday = (c*x + d*y)**2
    normalizado = math.sqrt(derivadax + derivaday)
    return ((a/normalizado)*x + (b/normalizado) * y)

Podemos ver que lo que hacemos en esta funcion es calcular las derivadas parciales en el punto que pasamos y luego normalizamos el vector gradiente para obtener la direccion de la pendiente de la funcion y avanzar sobre este unitariamente


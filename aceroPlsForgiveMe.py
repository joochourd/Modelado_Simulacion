import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy

a = int(input("ingrese valor a:"))
b = int(input("ingrese valor b:"))
c = int(input("ingrese valor c:"))
d = int(input("ingrese valor d:"))

p = -(a + d)
q = (a * d) - (b * c)

tempMatrix1 = sympy.Matrix([[0, 0], [0, 0]])
tempMatrix2 = sympy.Matrix([[0, 0], [0, 0]])

print (p, q)
if(math.pow(p, 2) - 4 * q) > 0:
    lambda1 = (-p-(math.sqrt(math.pow(p, 2) - 4 * q)))/2
    lambda2 = (-p+(math.sqrt(math.pow(p, 2) - 4 * q)))/2
    print ("lambdas: ", lambda1, lambda2)

    tempMatrix1 = sympy.Matrix([[a - lambda1, b], [c, d-lambda1]])
    tempMatrix2 = sympy.Matrix([[a - lambda2, b], [c, d-lambda2]])
    
t = np.array(range(-5, 5))
null1 = tempMatrix1.nullspace()
null2 = tempMatrix2.nullspace()

n1 = t*null1[0][0]/null1[0][1]
n2 = t*null2[0][0]/null2[0][1]

null2 = tempMatrix2.nullspace


x = np.array(range(-5, 5))
nulclina_x = (-a * x) / b
nulclina_y = (-c * x) / d


plt.plot(t, n1)
plt.plot(t, n2)
plt.plot(x, nulclina_x)
plt.plot(x, nulclina_y)
plt.show()

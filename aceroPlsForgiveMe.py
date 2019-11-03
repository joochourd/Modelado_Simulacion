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
    

x = np.array(range(-5, 5))
nulclina_x = (-a * x) / b
nulclina_y = (-c * x) / d



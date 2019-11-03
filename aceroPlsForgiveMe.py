import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import sympy

a = int(input("ingrese valor a:"))
b = int(input("ingrese valor b:"))
c = int(input("ingrese valor c:"))
d = int(input("ingrese valor d:"))
A = [[a, b], [c, d]]
A = sympy.Matrix(A)

p = -(a + d)
q = (a * d) - (b * c)

print (p, q)

lambda1 = (-p-(math.sqrt(math.pow(p, 2) - 4 * q)))/2
lambda2 = (-p+(math.sqrt(math.pow(p, 2) - 4 * q)))/2
print (lambda1, lambda2)

tempMatrix1 = sympy.Matrix([[a - lambda1, b], [c, d-lambda1]])
tempMatrix2 = sympy.Matrix([[a - lambda2, b], [c, d-lambda2]])
print(tempMatrix1.nullspace())
print(tempMatrix2.nullspace())

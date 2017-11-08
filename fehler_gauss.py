import numpy as np
from uncertainties import ufloat
import sympy
#from uncertainties.unumpy import sin
T,D,I = sympy.var('T,D,I')
T = ufloat(0.864, 0.031)
D = ufloat(0.011, 0.000073)
I = ufloat(-0.0017, 0.00034)


F = ((D * T**2)/(4 * 3.1415**2)) - I #Funktion

print('F = {}'.format(F))



#from sympy import var, sin

#x, y, z = var('x y z')

#Q = x**2 * sin(y) + z

#print(G.diff(T))
#print(G.diff(D))
#print(G.diff(I))

import numpy as np
from uncertainties import ufloat
import sympy
#from uncertainties.unumpy import sin
b,c = sympy.var('b,c')
b = ufloat(2.00431293962, 0.0178320962572)
c = ufloat(-0.0635812289017, 0.0379460605295)

M,L = sympy.var('M,L')

M = ufloat(42,1)
L= ufloat(0.1, 0.0001)
l = 632.990*10**-9

F = 1/b *(np.pi/2 -c) #Funktion
n= (M*l)/(L) +1
print('F = {}'.format(F))
print('n = {}'.format(n))

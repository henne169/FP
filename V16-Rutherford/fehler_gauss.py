import numpy as np
from uncertainties import ufloat
import sympy
#from uncertainties.unumpy import sin
X,Y,Z = sympy.var('X,Y,Z')
X = ufloat(1.36, 0.04)
Y = ufloat(1, 0.04)
Z = ufloat(0.36, 0.06)

#F = X-Y
F = 5.48 * Z / X

print('F = {}'.format(F))

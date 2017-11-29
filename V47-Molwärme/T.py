import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
from numpy import linspace, pi,exp, sin, cos, tan, loadtxt, savetxt, mean, zeros, size, log, sum, sqrt, arctan
from uncertainties import ufloat
import scipy.stats as st
from scipy.constants import c, e, h
from astropy.io import ascii


#plt.rcParams['figure.figsize'] = (10, 8)
#plt.rcParams['font.size'] = 13

T = np.genfromtxt("T.txt", unpack=True)
a = 0.00134
b = 2.296
c = -243.02
#T = a*R**2 + b*R + c
R = -b/(2*a) + ( (b/(2*a))**2 - ((c-T)/a) )**(1/2)
R_1 = R*10**(-3)
ascii.write([R_1, T], 'T_1.tex', format='latex')

#plt.plot(z
#R 'rx', label='Messdaten')
#plt.legend(loc='best')
#plt.ylabel(r'B / [mT]')
#plt.xlabel(r'z / [mm]')
#plt.savefig('B-Feld.pdf')
#plt.show()

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

a,b,c = np.genfromtxt('probe1.txt', unpack = True)
d,e,f = np.genfromtxt('probe2.txt', unpack = True)
g,e,h = np.genfromtxt('probe3.txt', unpack = True)

A = a #*10**(-6)
Q = (1/2)*((b-c)**2)**(1/2)
R = (1/2)*((e-f)**2)**(1/2)
S = (1/2)*((e-h)**2)**(1/2)
T = Q/1.36
U = R/1.296
V = S/5.11


plt.plot(A, T, 'go', label = 'Probe1 (Dotiert)')
plt.plot(A, U, 'bo', label = 'Probe2 (Dotiert)')
plt.plot(A, V, 'ro', label = 'Probe3 (Undotiert)')

plt.legend(loc="best")
plt.ylabel(r' Rotationswinkel $\theta/L$ / [degree/mm] ')
plt.xlabel(r' Wellenlänge $\lambda$ / [$10^{-6}$m] ')

plt.savefig('winkelplot.pdf')
plt.show()

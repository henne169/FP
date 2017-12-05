import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
import sympy
from numpy import linspace, pi,exp, sin, cos, tan, loadtxt, savetxt, mean, zeros, size, log, sum, sqrt, arctan
from uncertainties import ufloat
import scipy.stats as st
from scipy.constants import c, e, h
from astropy.io import ascii
from scipy import integrate
from math import cos, exp

################################################################################
#Umrechnung: Temperatur in Widerstand

#T = np.genfromtxt("T.txt", unpack=True)
#a = 0.00134
#b = 2.296
#c = -243.02
##T = a*R**2 + b*R + c
#R = -b/(2*a) + ( (b/(2*a))**2 - ((c-T)/a) )**(1/2)
#R_1 = R*10**(-3)
#ascii.write([R_1, T], 'T_1.tex', format='latex')

################################################################################
#Berechnung der Energien

#U,I,t = sympy.var('U,I,t')
#
#U = ufloat(19.12, 0.01)
#I = ufloat(181.5*10**(-3), 0.0001)
#t = ufloat(361, 5)
#
#F =  U*I*t #Funktion
#
#print('F = {}'.format(F))

################################################################################
#Berechnung der Molwärmen bei Konstantem Druck

#E,M,T,m = sympy.var('E,M,T,m')
#
#m = 342
#M = 63.546
#T = ufloat(10, 0.1)
#E = ufloat(1253, 17)
#
#C = (E*M)/(T*m)
#print('C = {}'.format(C))

################################################################################
#Berechnung der Molwärmen bei konstantem Volumen

#C,a,k,V,T = sympy.var('C,a,k,V,T')
#
#k = 140*10**9
#V = 7.1*10**(-6)
#C = 23.3
#T = 300
#a = 16.65*10**(-6)
#
#F = C - 9*k*V*T*a**2
#print('F = {}'.format(F))

################################################################################
#keine Ahnung

#def f(x):
#    return ((x**3)*(exp(x)))/(exp(x) - 1)
#integral = integrate.quad(f, 0, 1)
#print integral


################################################################################
#Plot

x,T = np.genfromtxt("bla.txt", unpack=True)
y,T = np.genfromtxt("bla2.txt", unpack=True)

plt.plot(x,T, 'rx', label='Empirische Molwärme')
plt.plot(y,T, 'bx', label='Theoretische Molwärme')

plt.legend(loc='best')
plt.ylabel(r'$C_V$ / [J/mol K]')
plt.xlabel(r'$T$ / [K]')
plt.savefig('C_V_T.pdf')
plt.show()

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
##Osz-plot1
#
#p,t = np.genfromtxt("osz2.txt", unpack=True)
#plt.plot(p,t, 'rx', label='Messwerte')
#plt.grid()
#plt.legend(loc='best')
#plt.ylabel(r'$P$ / [mV]')
#plt.xlabel(r'$t$ / [s]')
#plt.savefig('osz2_2.pdf')
#plt.show()
#
#################################################################################
##osz-plot2
#
#x,y = np.genfromtxt("osz1.txt", unpack=True)
#plt.plot(x,y, 'rx', label='Messwerte')
#plt.grid()
#plt.legend(loc='best')
#plt.ylabel(r'$P$ / [mV]')
#plt.xlabel(r'$t$ / [s]')
#plt.savefig('osz1_2.pdf')
#plt.show()
#
################################################################################
#lin. reg. Goldfoliendicke

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 13

u,q = np.genfromtxt("pulshohe_druck_mit_folie.txt", unpack=True)
s,t = np.genfromtxt("pulshohe_druck_ohne_folie.txt", unpack=True)

def f(q, a, b):
    return a * q + b
params1, covariance1 = curve_fit(f, q, u)
# covariance is the covariance matrix
errors1 = np.sqrt(np.diag(covariance1))
print('a =', params1[0], '±', errors1[0])
print('b =', params1[1], '±', errors1[1])
x_plot = np.linspace(-1,180)

def g(t, m, n):
    return m * t + n
params, covariance = curve_fit(g, t, s)
# covariance is the covariance matrix
errors = np.sqrt(np.diag(covariance))
print('m =', params[0], '±', errors[0])
print('n =', params[1], '±', errors[1])
s_plot = np.linspace(-1,180)

plt.xlim(0,180)
#plt.ylim(0,30)

plt.grid()
plt.plot(q, u, 'rx', label="Messdaten mit Goldfolie")
plt.plot(t, s, 'bx', label="Messdaten ohne Goldfolie")
plt.plot(x_plot, f(x_plot, *params1), 'r-', label='Lineare Regression mit Goldfolie', linewidth=1)
plt.plot(s_plot, g(s_plot, *params), 'b-', label='Lineare Regression ohne Goldfolie', linewidth=1)
plt.legend(loc="best")
plt.xlabel(r'Druck [mbar]')
plt.ylabel(r'Pulshöhe [V]')
plt.savefig('pulshohe_druck2.pdf')
plt.show()
################################################################################
#Foliendicke Tabelle
#
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

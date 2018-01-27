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
#
#plt.rcParams['figure.figsize'] = (10, 8)
#plt.rcParams['font.size'] = 13
#
#u,q = np.genfromtxt("pulshohe_druck_mit_folie.txt", unpack=True)
#s,t = np.genfromtxt("pulshohe_druck_ohne_folie.txt", unpack=True)
#
#def f(q, a, b):
#    return a * q + b
#params1, covariance1 = curve_fit(f, q, u)
## covariance is the covariance matrix
#errors1 = np.sqrt(np.diag(covariance1))
#print('a =', params1[0], '±', errors1[0])
#print('b =', params1[1], '±', errors1[1])
#x_plot = np.linspace(-1,180)
#
#def g(t, m, n):
#    return m * t + n
#params, covariance = curve_fit(g, t, s)
## covariance is the covariance matrix
#errors = np.sqrt(np.diag(covariance))
#print('m =', params[0], '±', errors[0])
#print('n =', params[1], '±', errors[1])
#s_plot = np.linspace(-1,180)
#
#plt.xlim(0,180)
##plt.ylim(0,30)
#
#plt.grid()
#plt.plot(q, u, 'rx', label="Messdaten mit Goldfolie")
#plt.plot(t, s, 'bx', label="Messdaten ohne Goldfolie")
#plt.plot(x_plot, f(x_plot, *params1), 'r-', label='Lineare Regression mit Goldfolie', linewidth=1)
#plt.plot(s_plot, g(s_plot, *params), 'b-', label='Lineare Regression ohne Goldfolie', linewidth=1)
#plt.legend(loc="best")
#plt.xlabel(r'Druck [mbar]')
#plt.ylabel(r'Pulshöhe [V]')
#plt.savefig('pulshohe_druck2.pdf')
#plt.show()
################################################################################
##Foliendicke
#X = sympy.var('X')
#X = ufloat(1.45, 0.25)
#e = 1.6*10**(-19)                   #Elementarladung C
#c = 299792458                       #Vakuumlichtgeschwindigkeit m/s
#u = 1.66*10**(-27)                  #atomare Masseneinheit kg
#E = e*X*(10**6)                     #Energieverlust J
#m = e*(0.510998946*(10**6))/(c**2)  #Ruhemasse Elektron
#T = e*5.48*10**6                    #Energie des Alphateilchens J
#a = 4*u                             #Masse des Alphateilchens kg
#v = ((2*T)/(a))**(1/2)              #geschwindigkeit des Alphateilchens
#I = e*9.225                         #Ionisationsenergie von Gold J
#w = 8.85*10**(-12)                  #elektrische Feldkonstante
#z = 2#*e                             #Ladung des Alphateilchens
#Z = 79                              #Ordnungszahl von Gold
#l = 196.966569*u                    #Masse Goldatom kg
#p = 19302                           #Dichte Gold kg/m**3
#n = p/l
#
#F = -E*(m*(v**2)*(4*np.pi*w)**2)/(4*np.pi*(e**4)*(z)*n*Z) *log( (2* m * v**2)/(I) )**(-1)
#
#print('D = {}'.format(F))
#print('N=',n)
#print('v=',v)

################################################################################
###Berechnung der Rate und der theoretischen WQ's
#o,c,t = np.genfromtxt('streuwinkel.txt', unpack = True)
#R = c/t
#D_R = R**(1/2)
#x = np.pi*o/180
#A = 1/((4*np.pi*8.85*10**(-12))**2)
#z = 2
#Z = 79
#e = 1.6*10**(-19)
#E = 5.48*(10**6)*e
#B = ((z*Z*e**2)/(4*E))**2
#C = 1/(np.sin(x/2)**4)
#D = A*B*C
#
#ascii.write([o,D], 'WQ-tab2.tex', format='latex')
#
#
################################################################################
##Berechnung der empirischen Wirkungsquerschnitte
#R = sympy.var('R')
#R = ufloat(0.603, 0.777)
#A = ufloat(15.75, 3.98)
#N = 5.9*10**(28)
#X = 2*10**(-6)
#O = 9.8*10**(-3)
#F = R/( A*N*X*O )
#
#print('WQ = {}'.format(F))
#
################################################################################
# WQ - Plot

A,B,C,D = np.genfromtxt("WQ-plot.txt", unpack=True)
#y,T = np.genfromtxt("bla2.txt", unpack=True)

errB = C
plt.errorbar(A, B, xerr=0, yerr=errB, fmt='bx',label="Empirischer Wirkungsquerschnitt")

plt.plot(A,D, 'rx', label='Theoretischer Wirkungsquerschnitt')
#plt.plot(A[:3],B[:3], 'go', label= 'Fehlerbehaftete Größen')
#plt.xlim(80,310)
plt.grid()
plt.ylim(-5,)
plt.legend(loc='best')
plt.ylabel(r'Wirkungsquerschnitt / [$10^{-22}$m$^{-1}$]')
plt.xlabel(r'Streuwinkel / [°]')
plt.savefig('WQ.pdf')
plt.show()

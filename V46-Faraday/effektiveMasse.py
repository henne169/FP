import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
from numpy import linspace, pi,exp, sin, cos, tan, loadtxt, savetxt, mean, zeros, size, log, sum, sqrt, arctan
from uncertainties import ufloat
import sympy
import scipy.stats as st
from scipy.constants import c, e, h
from astropy.io import ascii

B,e,z,c,N,n,a = sympy.var('B,e,z,c,N,n,a')

B = 407*10**(-3)
e = 1.602*10**(-19)
z = 8.854*10**(-12)
c = 2.9979*10**8
N = 1.2*10**(8)
n = 3.57
a = ufloat(0.0885, 0.043)

X = ( ((e**3)*N*B) / (8*(np.pi**2)*z*(c**3)*n*a) )**(1/2)

print('m*_1 = {} kg'.format(X))

B = 407*10**(-3)
e = 1.602*10**(-19)
z = 8.854*10**(-12)
c = 2.9979*10**8
N = 2.8*10**(18)
n = 3.57
a = ufloat(0.504, 0.151)

Y = ( ((e**3)*N*B) / (8*(np.pi**2)*z*(c**3)*n*a) )**(1/2)

print('m*_2 = {} kg'.format(Y))

P = X/(9.109*10**(-31))
Q = Y/(9.109*10**(-31))

print('m*_1 = {} m_e'.format(P))
print('m*_2 = {} m_e'.format(Q))

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

a,b,c = np.genfromtxt('probe1.txt', unpack = True)
d,e,f = np.genfromtxt('probe2.txt', unpack = True)
g,e,h = np.genfromtxt('probe3.txt', unpack = True)

A = a*10**(-6)
Q = (1/2)*((b-c)**2)**(1/2)
R = (1/2)*((e-f)**2)**(1/2)
S = (1/2)*((e-h)**2)**(1/2)
T = Q/1.36
U = R/1.296
V = S/5.11
ascii.write([A,Q,R,S,T,U,V], 'winkeltabelle3.tex', format='latex')

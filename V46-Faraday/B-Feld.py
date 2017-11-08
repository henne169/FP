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
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 13

z, B = np.genfromtxt("B-Feld.txt", unpack=True)

plt.plot(z,B, 'rx', label='Messdaten')
plt.legend(loc='best')
plt.ylabel(r'B / [mT]')
plt.xlabel(r'z / [mm]')
plt.savefig('B-Feld.pdf')
plt.show()

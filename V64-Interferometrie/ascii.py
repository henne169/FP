import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
from astropy.io import ascii

grad, I_min, I_max  = np.genfromtxt('kontrast.txt', unpack=True)
K= (I_max - I_min) / (I_max + I_min)
Winkel = grad-180
ascii.write([np.round(Winkel,0),np.round(I_min,2),np.round(I_max,2),np.round(K,2)], 'tabellekontrast.tex', format='latex')

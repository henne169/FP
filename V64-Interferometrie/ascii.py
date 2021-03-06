import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
from astropy.io import ascii

#grad, I_min, I_max  = np.genfromtxt('kontrast.txt', unpack=True)
#K= (I_max - I_min) / (I_max + I_min)
#Winkel = grad-180
#ascii.write([np.round(Winkel,0),np.round(I_min,2),np.round(I_max,2),np.round(K,2)], 'tabellekontrast.tex', format='latex')

Winkela, Anzahl  = np.genfromtxt('glasmessung1.txt', unpack=True)
Winkelb, Anzahl2  = np.genfromtxt('glasmessung2.txt', unpack=True)
Winkelc, Anzahl3  = np.genfromtxt('glasmessung3.txt', unpack=True)

T = 1 * 10**-3
lam = 632.990 *10**-9
tetha_0 = 0.175
Winkel = Winkela * (np.pi)/180
Winkel2 = Winkelb * (np.pi)/180
Winkel3 = Winkelc * (np.pi)/180


n1 = (- T * 2* tetha_0 * Winkel) / (Anzahl * lam  - T*(2*tetha_0 *Winkel))
n2 = (- T * 2* tetha_0 * Winkel2) / (Anzahl2 * lam  - T*(2*tetha_0 *Winkel2))
n3 = (- T * 2* tetha_0 * Winkel3) / (Anzahl3 * lam  - T*(2*tetha_0 *Winkel3))


ascii.write([Winkela,Anzahl,np.round(n1,3),Winkelb,Anzahl2,np.round(n2,3),Winkelc,Anzahl3,np.round(n3,3)], 'Glasmessungen2.tex', format='latex')

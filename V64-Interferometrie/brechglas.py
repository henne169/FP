#Brechunsindizes
import numpy as np
from uncertainties import ufloat
import sympy

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

n = [n1,n2,n3]

m = np.mean(n)
s = np.std(n)
print('Mittelwert = ' ,m)
print('Standartabweichung =', s)

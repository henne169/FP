import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt
from astropy.io import ascii

a, b, c, d = np.genfromtxt('winkel.txt', unpack = True)

B = ((b-d)**2)**(1/2)
C = ((c-d)**2)**(1/2)


#ascii.write([a, B, C], 'winkeldifftab.tex', format='latex')

x = a**2
y = C

plt.plot(x, y, 'r.')

def f(x,p,q):
    return p * x + q
params, covariance = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance))
print('p =', params[0], '±', errors[0])
print('q =', params[1], '±', errors[1])
#print('r =', params[2], '±', errors[2])

x_plot = np.linspace(0 , 10) #
plt.plot(x, y, 'rx', label="Messdaten")
plt.plot(x_plot, f(x_plot, *params), 'b-', label='Ausgleichskurve', linewidth=1)

plt.legend(loc="best") #Positioniert automatisch die Legende
plt.xlabel(r'$\lambda^2$ / [$10^{-6}$m]')
plt.ylabel(r'$\theta/L$ / [Degree/mm]')
plt.savefig('winkeldiffplot2.pdf')
plt.show()

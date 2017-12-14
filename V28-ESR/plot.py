import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp


plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 13


nu_e = np.array([10.623,14.732,20.555,23.887,29.391])
B = np.array([ 308.008,524.924,737.232,830.569,1027.756])

def f(nu_e, a, b):
    return a * nu_e + b

params, covariance = curve_fit(f, nu_e, B)
# covariance is the covariance matrix
errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


x_plot = np.linspace(10,35)   #nicht sicher, aber jedes mal beifügen

plt.grid()
plt.plot(nu_e, B, 'rx', label="mittlere Feldstärken pro Signalfrequenz")
plt.plot(x_plot, f(x_plot, *params), 'm-', label='Linear Fit', linewidth=1)
plt.legend(loc="best")
plt.xlabel(r'$\nu_e \, [MHz]$')
plt.ylabel(r'$B \,[\mu T] $')
plt.savefig('plot.pdf')   #wichtig, wenn man protokolle schreibt
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp


plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 13


grad, I_min, I_max= np.genfromtxt('kontrast.txt', unpack=True)

K = (I_max - I_min) / (I_max + I_min)
#def f(weg, a, b):
#    return a * weg + b

#params, covariance = curve_fit(f, weg, energie)
## covariance is the covariance matrix
#errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


x_plot = np.linspace(180, 360)   #nicht sicher, aber jedes mal beifügen
#plt.ylim([-0.5,4.5])
plt.grid()
plt.plot(grad, K, 'mx', label="Messwerte")
#plt.plot(x_plot, f(x_plot, *params), 'm-', label='Linear Fit', linewidth=1)
plt.legend(loc="best")
plt.xlabel(r'$np.phi$ [°]')
plt.ylabel(r'$K$' )
plt.savefig('verlust2.pdf')   #wichtig, wenn man protokolle schreibt
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp


plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 13


grad1, I_min, I_max= np.genfromtxt('kontrast.txt', unpack=True)
grad= grad1-180
K = (I_max - I_min) / (I_max + I_min)

def f(grad,a,b,c,d):
    return a * np.abs(np.sin(b*np.deg2rad(grad)+c))+d

params, covariance = curve_fit(f, grad, K, p0=[0.9,2,0.1,0.1])
## covariance is the covariance matrix
errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])
print('d =', params[3], '±', errors[3])
b=params[1]
c=params[2]
print('phi =', np.rad2deg(1/b*(np.pi/2 -c)))
plt.ylim(0,1)
plt.xlim(-15,195)
x_plot = np.linspace(-15, 195,1000)   #nicht sicher, aber jedes mal beifügen
#plt.ylim([-0.5,4.5])
plt.grid()
plt.plot(grad, K, 'mx', label="Messwerte")
plt.plot(x_plot, f(x_plot, *params), 'm-', label='Linear Fit', linewidth=1)
plt.legend(loc="best")
plt.xlabel(r'$\phi$ [°]')
plt.ylabel(r'$K$' )
plt.savefig('kontrast.pdf')   #wichtig, wenn man protokolle schreibt
plt.show()

import numpy as np
import math
from scipy.stats import sem
import uncertainties.unumpy as uns
from uncertainties import ufloat

x = np.genfromtxt('debyetemp.txt', unpack=True)
print('Der Mittelwert von x ist', np.mean(x))
print('Fehler des Mittelwertes von x ist', np.std(x, ddof=1) / np.sqrt(len(x)))

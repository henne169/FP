import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import uncertainties as unc
import uncertainties.unumpy as unp
from astropy.io import ascii

x=np.array([50.43,64.52,58.41,61.09,0,0,0])
y=np.array([49.86,50.83,50.99,50.68,50.47,0,0])
z=np.array([49.25,50.68,50.65,53.04,51.06,49.21,51.60])
o=np.array([49.19,50.68,51.32,51.43,50.68,49.71,0])
p=np.array([50.54,51.43,51.49,50.42,0,0,0])

ascii.write([x,y,z,o,p,], 'procm.tex', format='latex')

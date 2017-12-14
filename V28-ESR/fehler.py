import numpy as np
from uncertainties import ufloat
import sympy
from uncertainties.unumpy import sin

x=np.array([50.43,64.52,58.41,61.09])
y=np.array([49.86,50.83,50.99,50.68,50.47])
z=np.array([49.25,50.68,50.65,53.04,51.06,49.21,51.60])
o=np.array([49.19,50.68,51.32,51.43,50.68,49.71])
p=np.array([50.54,51.43,51.49,50.42])

I_a = np.array([254.61,404.56,558.58,618.63,759.45])
I_p = np.array([184.55,
343.88,
492.57,
565.60,
705.93])

mu = 4* np.pi * 10**(-7)
B_a = 8/np.sqrt(125) * mu * 156/0.1 *I_a
B_p = 8/np.sqrt(125) * mu * 156/0.1 *I_p


print('B_a=', B_a)
print('B_p=', B_p)


print('Mittelwert 10,623 MHZ, 1cm =', np.mean(x))
print('Mittelwert 14,732 MHZ, 1cm =', np.mean(y))
print('Mittelwert 20,555 MHZ, 1cm =', np.mean(z))
print('Mittelwert 23,887 MHZ, 1cm =', np.mean(o))
print('Mittelwert 29,391 MHZ, 1cm =', np.mean(p))

print('Fehler auf den Mittelwert 10,623 MHZ', np.std(x, ddof=1) / np.sqrt(len(x)))
print('Fehler auf den Mittelwert 14,732 MHZ', np.std(y, ddof=1) / np.sqrt(len(y)))
print('Fehler auf den Mittelwert 20,555 MHZ', np.std(z, ddof=1) / np.sqrt(len(z)))
print('Fehler auf den Mittelwert 23,887 MHZ', np.std(o, ddof=1) / np.sqrt(len(o)))
print('Fehler auf den Mittelwert 29,391 MHZ', np.std(p, ddof=1) / np.sqrt(len(p)))















#b,c = sympy.var('b,c')
#b = ufloat(2.00431293962, 0.0178320962572)
#c = ufloat(-0.0635812289017, 0.0379460605295)
#
#M,L = sympy.var('M,L')
#
#
#M = ufloat(42,1)
#L= ufloat(0.1, 0.0001)
#l = 632.990*10**-9
#
#F = 1/b *(np.pi/2 -c) #Funktion
#n= (M*l)/(L) +1
#print('F = {}'.format(F))
#print('n = {}'.format(n))

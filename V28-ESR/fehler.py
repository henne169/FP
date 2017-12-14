import numpy as np
from uncertainties import ufloat
import sympy
from uncertainties.unumpy import sin

x=np.array([50.43,64.52,58.41,61.09])
y=np.array([49.86,50.83,50.99,50.68,50.47])
z=np.array([49.25,50.68,50.65,53.04,51.06,49.21,51.60])
o=np.array([49.19,50.68,51.32,51.43,50.68,49.71])
p=np.array([50.54,51.43,51.49,50.42])

B_a= np.array([357.14527,  567.48238  ,783.52855  ,867.76158 , 1065.29191])
B_p= np.array([258.87105  ,482.36564  ,690.93533  ,793.37561  ,990.2186 ])
I_a = np.array([254.61,404.56,558.58,618.63,759.45])
I_p = np.array([184.55,
343.88,
492.57,
565.60,
705.93])
mu = 4* np.pi * 10**(-7)
B_a1 = 8/np.sqrt(125) * mu * 156/0.1 *I_a
B_p1 = 8/np.sqrt(125) * mu * 156/0.1 *I_p

dB_a = 8/np.sqrt(125) * mu * 156/0.1 * B_a
dB_p = 8/np.sqrt(125) * mu * 156/0.1 * B_p

B1= np.array([357.145,258.871])
B2= np.array([567.482 ,482.366])
B3= np.array([783.529,690.935])
B4= np.array([867.762,793.376])
B5= np.array([1065.292,990.219])
oha = B_a - B_p
oha2 = B_p-B_a
erde1= np.mean((B_a-B_p)/2)

erde2=np.mean((B_p-B_a)/2)
print('dif1 =', oha)
print('dif2=',oha2)
print('B_a-B_p, erde 1 =', erde1)
print('Bp-Ba, erde 2 =', erde2)
print('Fehler erde 1= ',  np.std(oha, ddof=1) / np.sqrt(len(oha)))
print('fehler B1 =', np.std(B1)/np.sqrt(2))
print('fehler B2 =', np.std(B2)/np.sqrt(2))
print('fehler B3 =', np.std(B3)/np.sqrt(2))
print('fehler B4 =', np.std(B4)/np.sqrt(2))
print('fehler B5 =', np.std(B5)/np.sqrt(2))


print('Fehler von Ba=', dB_a)
print('Fehler von Bp=', dB_p)


print('B_a1=', B_a1)
print('B_p1=', B_p1)


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

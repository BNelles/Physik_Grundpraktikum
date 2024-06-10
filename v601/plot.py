import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import scipy.constants as const

#Normierung des Plots
#print(20.7/5)

d=(ufloat(3.8,0.1),ufloat(4.7,0.1),ufloat(4.4,0.1),ufloat(4.1,0.1),ufloat(4.2,0.1))
e=(3.8,4.7,4.4,4.1,4.2)
#print(np.mean(d))
a=np.mean(d)
#print(np.std(e))
dx=ufloat(2.1,0.1)
x=a/10 #normierung der Achse
#print(x)
dU=dx*x #Berechnung der Spannung
print(dU)
#Berechnung der Wellenlänge
l=(const.h*const.c)/(dU*const.e)
print(l)

d2=ufloat(5,0.1)
x2=2/d2
#print(x2*ufloat(4.5,0.2))
#print(x2*2.5)

#print(9-(6+x2*ufloat(4.5,0.2)))

T=np.genfromtxt("T.txt",unpack=True)
#print(T+273.15)
T=1/(T+273.15)
p=5.5*10**7*np.exp(-6876*T)
w=(2.9*10**(-6))/p*10**(2)
#print(w)
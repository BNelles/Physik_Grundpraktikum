import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

h1,t=np.genfromtxt("data/Herz.txt",unpack=True)

h=75-44.21-h1

h_m=ufloat(np.mean(h),np.std(h))*10**(-2)

d=43.7*10**(-2)
G=np.pi*(d/2)**2
ESV=1/3*G*h_m


t_m=ufloat(np.mean(t),np.std(t))/60

f=1/t_m

HZV=ESV*f

print(HZV)
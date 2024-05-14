import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import factorial
from numpy.random import default_rng
from uncertainties import ufloat
import uncertainties.unumpy as unp
import random

n,z=np.genfromtxt("data/data3.txt",unpack=True)
z_m=np.mean(z)
z_s=np.std(z)
z_v=np.var(z)

#n=np.sqrt(2*np.pi)
#
#def g(x,m,s):
#    return (1/(s*n))*np.exp(-1/2*((x-m)/s)**2)
#
#
#def p(v,x):
#    #for i in range (0):
#    # a=a+(v**i)/np.math.factorial(i)
#    return np.exp(-v)*(v**x)/factorial(x)
#
#
rng=default_rng(0)
poisson= rng.poisson(z_m, 100)
gauß= rng.normal(z_m,z_s, 100)
#print(poisson)
#
#
#x=np.linspace(1600,2100,500,dtype=int)

#print(x)

#A, covariance_matrix = curve_fit(g,z,z_m,z_s)
#errors1 = np.sqrt(np.diag(covariance_matrix))
#
#print(A)

#y=g(x,z_m,z_s)
#y2=p(z_v,x)
#
fig, ax1 = plt.subplots(1, 1, layout="constrained")
#ax1.plot(x, y,"*", label="Gauß-Verteilung")

#ax1.legend(loc="best")

#ax1.plot(x, y2, label="Poisson-Verteilung")
##ax1.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
##ax1.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
#ax1.legend(loc="best")
#


ax1.hist(z,bins=40,density=True,label="Messwerte")

ax1.hist(poisson,bins=40,density=True,alpha=0.2,color='r',label="Poisson-Verteilung")
ax1.hist(gauß,bins=40,density=True,alpha = 0.2,color='y',label="Gauß-Verteilung")
ax1.set_xlabel(r"$z$")
ax1.set_ylabel(r"$N$")

fig.savefig("build/Statistik.pdf")

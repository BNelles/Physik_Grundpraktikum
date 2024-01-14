import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat

a,b=np.genfromtxt("data3.txt" , unpack=True)
l,p,ö=const.physical_constants["magn. constant"]
x=a*l*(195/2)*(0.109**2)/((0.109**2+0.069**2)**(3/2)) 
y=1/b

params, covariance_matrix=np.polyfit(x,y, deg=1, cov=True)
errors=np.sqrt(np.diag(covariance_matrix))
x_plot=np.linspace(0.00075,0.00275)


fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, y, "o", label="Messwerte")
ax.plot(x_plot,params[0]*x_plot+params[1],label="lineare Regression",linewidth=1)
#ax.set_xlabel(r"$B \mathbin{/} \unit{\tesla}$")
#ax.set_ylabel(r"$\overline{T} \mathbin{/} \unit{\per\second}$")
ax.legend(loc="best")
print(params[0])
print(errors[0])

g=ufloat(params[0],errors[0])
P=4*np.pi**2*5*0.0000375*g 

G=ufloat(1.07,0.03)
S=ufloat(19.7,1.6)
print((P-G)/P)
print((P-S)/P)
print((G-S)/G)


fig.savefig("build/plot.pdf")
print(l*(195/2)*(0.109**2)/((0.109**2+0.069**2)**(3/2)))
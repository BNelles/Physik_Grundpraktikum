import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

def sinc(X,a,b):
    return a*(np.sin((b*X))/(X))**2

i,y = np.genfromtxt("data/data2.txt",unpack=True)

I=i-0.32
x=(y-25)

fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I,".k" ,label="Spalt 2")
ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
ax1.set_ylabel(r"$Stromstärke \mathbin{/} \unit{\nano\ampere}$")



params, covariance_matrix = curve_fit(sinc, x,I, p0=[80,0.5])
uncertainties=np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(-27,27,100)

print(params, uncertainties)
ax1.plot(x_plot,sinc(x_plot,params[0],params[1]),"-",label="Ausgleichskurve")
l=635*10**(-9)

ax1.legend(loc="best")

v=ufloat(params[1],uncertainties[1])
B=(v*l*10**3)/np.pi
print(B)
print((1.5*10**(-4)-B)/(1.5*10**(-4)))
fig.savefig("plot1.pdf")
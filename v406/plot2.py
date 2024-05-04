import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

i,y = np.genfromtxt("data/data3.txt",unpack=True)

I=i-0.32
x=(y-25)*10**(-3)

def f(X,a,b,c):
    return a*((np.cos(c*X)*np.sin(b*(X)))/(X))**2

fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I,".k" ,label="Doppelspalt")
ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")


params, covariance_matrix=curve_fit(f, x,I,p0=[1,10,0.1])
uncertainties=np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(-0.03,0.03,100)

print(params)
ax1.plot(x_plot,f(x_plot,params[0],params[1],params[2]),"-",label="Ausgleichskurve")
l=635*10**(-9)
v=ufloat(params[1],uncertainties[1])
w=ufloat(params[2],uncertainties[2])

ax1.legend(loc="best")

B=(v*l)/np.pi
C=(w*l)/np.pi
print(B,(10**(-4)-B)/(10**(-4)))
print(C,(4*10**(-4)-C)/(4*10**(-4)))
fig.savefig("plot2.pdf")
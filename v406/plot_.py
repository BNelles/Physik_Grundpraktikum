import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

i,y = np.genfromtxt("data/data1.txt",unpack=True)

I=(i-0.32)*10**(-9)
x=(y-25)*0.001

L=1
phi=x/L
l=635*10**(-9)

v=1.5*10**(-3)

def sinc(phi,A_0,b):
     return ((A_0)**2)*(b**2)*((l/(np.pi*b*np.sin(phi+v)))**2)*((np.sin((np.pi*b*np.sin(phi+v))/l))**2)

    #return  A_0*b*phi


    #return ((A_0)**2)*(b**2)*(635/(np.pi*b*np.sin(phi)))**2*(np.sin((np.pi*b*np.sin(phi))/635))**2






fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(phi, I,".", label="Spalt 1")
#ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$Stromstärke \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

params, covariance_matrix=curve_fit(sinc, phi,I)
uncertainties=np.sqrt(np.diag(covariance_matrix))


x_plot=np.linspace(0,55,1)

print(params, uncertainties)
print(params[0])
print(params[1])
print(uncertainties)
ax1.plot(phi,sinc(phi,params[0],params[1]))
plt.show()
#fig.savefig("build/plot.pdf")

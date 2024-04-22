import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

i,y = np.genfromtxt("data/data1.txt",unpack=True)

I=i-0.32
x=y-25

L=1000
phi=x/L
b=0.075
def sinc(phi,A_0):
    return ((A_0)**2)*(b**2)*(635/(np.pi*b*phi))**2*(np.sin((np.pi*b*phi)/635))**2

    #return A_0^2*b^2*(635/(np.pi*b*np.sin(phi)))^2*(np.sin((np.pi*b*np.sin(phi))/635))^2






fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(phi, I, label="Spalt 1")
#ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$Stromstärke \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

params, covariance_matrix=curve_fit(sinc, phi,I)
uncertainties=np.sqrt(np.diag(covariance_matrix))


x_plot=np.linspace(0,55,1)

print(params, uncertainties)
ax1.plot(phi,sinc(phi,params[0]))
plt.show()
#fig.savefig("build/plot.pdf")

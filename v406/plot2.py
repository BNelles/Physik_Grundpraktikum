import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

I,y = np.genfromtxt("data/data3.txt",unpack=True)
x=y-25
def sinc(X,a,b):
    return a*(np.sin(b*(X))/(X))**2

fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I,".k" ,label="Doppelspalt")
#ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

params, covariance_matrix=curve_fit(sinc, x,I, p0=[40,0.1])
uncertainties=np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(0,55,1)

print(params, uncertainties)
ax1.plot(x_plot,sinc(x_plot,*params,"-"))

fig.savefig("plot2.pdf")
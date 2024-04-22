import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def sinc(X,a,b):
    return a*(np.sin((b*X))/(X))**2

I,y = np.genfromtxt("data/data2.txt",unpack=True)
x=y-25

fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I,".k" ,label="Spalt 2")
#ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")


params, covariance_matrix = curve_fit(sinc, x,I, p0=[80,0.5])
uncertainties=np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(-27,27,100)

print(params, uncertainties)
ax1.plot(x_plot,sinc(x_plot,params[0],params[1]),"-")


fig.savefig("plot1.pdf")
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
#import uncertainties.unumpy as unp
from  uncertainties import ufloat

F,p=np.genfromtxt("data3.txt", unpack=True)
T=F+273.15

x=np.linspace(270,300)

fig, ax=plt.subplots()

ax.plot(
    T,p,"o"
)
ax.set(
    xlabel=r"$p \mathbin{/} \unit{\bar}"
    ylabel=r"$T \mathbin{/} \unit{\kelvin}$"
)
params, covariance_matrix = np.polyfit(T, p, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

ax.plot(
    x,params[0]*x+params[1],"--"
)
print(params[0],errors[0])
a=ufloat(params[0],errors[0])
L=a*const.R
print(L)
fig.savefig("verdampfplot.pdf")
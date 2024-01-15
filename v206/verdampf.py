import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
#import uncertainties.unumpy as unp
from  uncertainties import ufloat

F,P=np.genfromtxt("data3.txt", unpack=True)
T1=F+273.15
T=1000/(T1)
#print(T)
p=np.log((P+1)/0.9949)
x=np.linspace(3.3,3.7)

fig, ax=plt.subplots()

ax.plot(
    T,p,"o"
)
ax.set(
    xlabel=r"$ln(\frac{p}{p_0}$"
    ylabel=r"$\frac{1}{T} \mathbin{/} \unit{\per\milli\per\kelvin}$"
)
params, covariance_matrix = np.polyfit(T, p, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

ax.plot(
    x,params[0]*x+params[1],"--"
)
#print(params[0],errors[0])
a=ufloat(params[0],errors[0])*1000
L=-a/const.R
#print(L)
fig.savefig("verdampfplot.pdf")
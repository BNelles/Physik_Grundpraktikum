import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

d,t,N=np.genfromtxt("data/data1.txt", unpack=True)

h=971/900
n=N/t-h

fig, ax=plt.subplots(1,1,layout="constrained")

lN=np.log(n)

params, covariancematrix=np.polyfit(d, lN, deg=1, cov=True)
errors=np.sqrt(np.diag(covariancematrix))

x=np.linspace(1,21,1000)

ax.plot(x,params[0]*x+params[1],"--",label="lineare Regression")
#ax.set_xlabel(r"$d\text{/}\unit{\milli\meter}$")
#ax.set_ylabel(r"$ln(N)$")
ax.plot(d,lN,".k",label="Messdaten")
ax.legend(loc="best")
fig.savefig("build/eisen.pdf")

m=ufloat(params[0],errors[0])*10**(3)

print(m)



import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat 

d,t,N=np.genfromtxt("data/data3.txt",unpack=True)

h=589/900
n=N/t-h

fig, ax=plt.subplots(1,1,layout="constrained")

lN=np.log(n[0:9])
ln=np.log(-n[9:12])
params, covariancematrix=np.polyfit(d[0:9], lN[0:9], deg=1, cov=True)
errors=np.sqrt(np.diag(covariancematrix))


params2, covariancematrix2=np.polyfit(d[9:12], ln, deg=1, cov=True)
errors2=np.sqrt(np.diag(covariancematrix2))

x=np.linspace(1,360,1000)
ax.plot(d[9:12],ln,".b")
ax.plot(x,params[0]*x+params[1],"--",label="lineare Regression")
#ax.set_xlabel(r"$d\text{/}\unit{\micro\meter}$")
#ax.set_ylabel(r"$ln(N)$")
ax.plot(d[0:9],lN,".k",label="Messdaten")
ax.legend(loc="best")
fig.savefig("build/beta.pdf")

m=ufloat(params[0],errors[0])*10**(6)

print(m)
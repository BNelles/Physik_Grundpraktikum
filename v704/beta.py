import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat 
from uncertainties.umath import sqrt

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

x=np.linspace(0,500,1000)
ax.plot(d[9:12],ln,".b")
ax.plot(x,params[0]*x+params[1],"--",label="lineare Regression vor dem Knick")
ax.set_xlabel(r"$d\text{/}\unit{\micro\meter}$")
ax.set_ylabel(r"$ln(N)$")
ax.plot(d[0:9],lN,".k",label="Messdaten")
ax.plot(x,params2[0]*x+params2[1],"--",label="lineare Regression hinter dem Knick")

ax.legend(loc="best")


fig.savefig("build/beta.pdf")



m=ufloat(params[0],errors[0])*10**(6)
m2=ufloat(params2[0],errors2[0])*10**(6)
b=ufloat(params[1],errors[1])
b2=ufloat(params2[1],errors2[1])

#print(m)
#print(m2)

R=(b2-b)/(m-m2)
#print(R)

E=1.92*sqrt(R**2+0.22*R)
#print(E)
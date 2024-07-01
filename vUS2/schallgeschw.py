import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,t,t2,d=np.genfromtxt("data/schall.txt",unpack=True)
t=t/2*10**(-6)
x=x*10**(-3)
fig, ax=plt.subplots(1,1,layout="constrained")

ax.plot(t,x,".")

params, covariance_matrix=np.polyfit(t,x,deg=1,cov=True)
errors=np.sqrt(np.diag(covariance_matrix))
print(params[0])
x_plot=np.linspace(0,0.00003,100)
ax.plot(x_plot,params[0]*x_plot+params[1])

fig.savefig("build/schall.pdf")

c=ufloat(params[0],errors[0])
h=80*10**(-3)
x2=params[0]*t2*10**(-6)

d2=np.array(h-params[0]*t-x2)
n=np.array(np.linspace(1,11,11))
fig2, ax1=plt.subplots(1,1,layout="constrained")
#print(np.size(d2))
print(d2)
ax1.plot(n,d2,".k")
fig2.savefig("build/loecher.pdf")
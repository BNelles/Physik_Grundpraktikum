import matplotlib.pyplot as plt
import numpy as np


w,z=np.genfromtxt("data1.txt",unpack=True)
x=w*60
y=z+273.15

d,c=np.genfromtxt("data2.txt",unpack=True)
a=d*60
b=c+273.15

f1,cov1=np.polyfit(x,y,deg=2,cov=True)
unc=np.sqrt(np.diag(cov1))
f2=np.poly1d(f1)
x_x=np.linspace(0,24*60)
f=f2(x_x)

g1,cov2=np.polyfit(x,b,deg=2,cov=True)
unc=np.sqrt(np.diag(cov2))
g2=np.poly1d(g1)
g=g2(x_x)


fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, y, "x", label=r"$T_1$")
ax.plot(x, b, "x", label=r"$T_2$")
ax.plot(x_x,f, "b-", label=r"$T_1$ Fit") 
ax.plot(x_x,g, "-", color="orange",label=r"$T_1$ Fit") 

ax.set_ylabel(r"$T \mathbin{/} \unit{\kelvin}$")
ax.set_xlabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")



fig.savefig("build/plot.pdf")
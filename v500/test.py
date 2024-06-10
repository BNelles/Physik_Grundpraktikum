import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

u=(0.966,1.138,0.453,0.280)
f=(0.029,0.031,0.017,0.014)
UG_v=ufloat(0.966,0.029)
UG_b=ufloat(1.138,0.031)
UG_g=ufloat(0.453,0.017)
UG_o=ufloat(0.280,0.014)

1/435.8

w=(1/435.8,1/404.7,1/546,1/579.1)
w=(0.1,0.2,0.3,0.4)


UG=unp.uarray(u,f)

A,C=np.polyfit(w,u,deg=1,cov=True)
F=np.sqrt(C)

z=A[0]
print(w)
a=A[0]*w+A[1]

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(w, u, ".",label="I")
plt.errorbar(w,u,f)
ax1.plot(w,a,"k-",label="Ausgleichsgerade")
plt.errorbar(w,a,F)
#ax1.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
#ax1.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit


u0=np.array([0.98,1.13,0.45,0.25])

u=(0.966,1.138,0.453,0.280)
f=(0.029,0.031,0.017,0.014)
UG_b=ufloat(0.966,0.029)
UG_v=ufloat(1.138,0.031)
UG_g=ufloat(0.453,0.017)
UG_o=ufloat(0.280,0.014)

1/435.8
w=np.array([1/435.8,1/404.7,1/546,1/579.1])
w=w*10**9
w=w*3*10**8

UG=unp.uarray(u,f)

def Gerade(x,a,b):
    return a*x+b

A,C=curve_fit(Gerade,w,u,sigma=f)
#A,C=np.polyfit(w,u,deg=1,cov=True)
F=np.sqrt(np.diag(C))

B,K=curve_fit(Gerade,w,u0)
BF=np.sqrt(np.diag(K))

e=1.6*10**(-19)
#print(A[0]*e,F[0]*e)
#print(B[0]*e,BF[0]*e)

a=A[0]*w+A[1]
b=B[0]*w+B[1]

h=ufloat(A[0]*e,F[0]*e)
v=w[3]
W=h*v-e*UG_o
#print(W)

p1=ufloat(2.76,0.27)*10**(-19)
p2=ufloat(2.71,0.25)*10**(-19)
p3=ufloat(2.67,0.20)*10**(-19)
p4=ufloat(2.75,0.19)*10**(-19)

UGES=(p1+p2+p3+p4)/4
#print(UGES)


fig, (ax2,ax1) = plt.subplots(2, 1, layout="constrained")
ax2.plot(w, u0, ".",label="U_G")
ax2.plot(w,b,"k-",label="Ausgleichsgerade")
ax2.set_xlabel(r"$\omega \mathbin{/} \unit{\per\second}$")
ax2.set_ylabel(r"$U \mathbin{/} \unit{\volt}$")
ax2.legend(loc="best")


ax1.plot(w, u, ".",label="U_G")
plt.errorbar(w,u,f,fmt="none")
ax1.plot(w,a,"k-",label="Ausgleichsgerade")
ax1.set_xlabel(r"$\omega \mathbin{/} \unit{\per\meter}$")
ax1.set_ylabel(r"$U \mathbin{/} \unit{\volt}$")
ax1.legend(loc="best")

fig.savefig("build/Planck.pdf")
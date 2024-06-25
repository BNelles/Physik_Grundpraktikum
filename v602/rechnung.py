import numpy as np
from uncertainties import ufloat
from uncertainties.umath import sin
import scipy.constants as const
import matplotlib.pyplot as plt

#Vorbereitung
def s(E,z):
    return z-np.sqrt((E*10**3)/13.6-(1/137)**2*(z**4)/4)

Z=(30,31,35,37,38,40)
E=(9.65,10.37,13.47,15.20,16.10,17.99)
print(s(E[1],Z[1]))

#Kupfer
#K_Beta
d=201.4*10**(-12)
l=2*d*sin((np.pi*ufloat(20.2,0.2))/180)
E=(const.h*const.c)/l
#print(l*10**12,E/const.e)

#diff Beta
ld=2*d*sin((np.pi*0.6344)/180)
l1=l-ld/2
l2=l+ld/2
E=(const.h*const.c)*(1/l2-1/l1)
#print(ld*10**12,E/const.e)

#K_Alpha
l=2*d*sin((np.pi*ufloat(22.4,0.2))/180)
E=(const.h*const.c)/l
#print(l*10**12,E/const.e)

ld=2*d*sin((np.pi*0.6749)/180)
l1=l-ld/2
l2=l+ld/2
E=(const.h*const.c)*(1/l2-1/l1)
#print(ld*10**12,E/const.e)
#print((const.h*const.c)/(154*10**(-12))/const.e)

#Abschirmkonstanten

z=29
R=13.6
EK=8.98*10**3
EKa=8.08*10**3
Ekb=8.91*10**3

s1=z-np.sqrt(EK/R)
s2=z-2*np.sqrt((z-s1)**2-EKa/R)
s3=z-3*np.sqrt((z-s1)**2-Ekb/R)
#print(s1,s2,s3)

#Absorptionsspektren

Eb=(const.h*const.c)/(2*d*sin((np.pi*13)/180))/const.e/(10**3)


Eg=(const.h*const.c)/(2*d*sin((np.pi*17.25)/180))/const.e/(10**3)


Es=(const.h*const.c)/(2*d*sin((np.pi*11)/180))/const.e/(10**3)


Ez=(const.h*const.c)/(2*d*sin((np.pi*18.5)/180))/const.e/(10**3)


Ezr=(const.h*const.c)/(2*d*sin((np.pi*9.75)/180))/const.e/(10**3)

print(Eb)
print(Eg)
print(Es)
print(Ez)
print(Ezr)

Ek=np.array([Ez,Eg,Eb,Es,Ezr])
Z=np.array([30,31,35,38,40])
si=np.array([3.56,3.61,3.85,4.00,4.09])
Ze=Z-si

fig, ax=plt.subplots(1,1,layout="constrained")
params, covariance_matrix=np.polyfit(Ze**2,Ek,deg=1,cov=True)
errors=np.sqrt(np.diag(covariance_matrix))
ax.set_xlabel(r"$\text{Z}_{\symup{eff}^2}$")
ax.set_ylabel(r"$E_{\symup{K}} \text{/} \unit{\kilo\electronvolt} $")
ax.plot(Ze**2,Ek,".")
x=np.linspace(700,1300,10)
print(params[0],errors[0])
ax.plot(x,params[0]*x+params[1],label="Ausgleichskurve")
fig.savefig("build/absorb.pdf")
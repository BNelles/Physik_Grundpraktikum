import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy


p,c,z=np.genfromtxt("data/data2.txt",unpack=True)

c0=4/c[0]
E=c0*c
#print(E)
#p=p[:14]
#c=c[:14]
#z=z[:14]




x=0.05*(p/1013)

params, covariance_matrix = np.polyfit(x[:11], E[:11], deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))


x_plot=np.linspace(-0.01,0.04,1000)
fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, E,".k" ,label="Messwerte")
#ax1.errorbar(x,E, np.std(E),fmt=".k",label="Messwerte")
ax1.plot(x_plot,params[0]*x_plot+params[1],"--",label="Regression")

ax1.set_xlabel(r"$x \mathbin{/} \unit{\meter}$")
ax1.set_ylabel(r"$E \mathbin{/} \unit{\mega\electronvolt}$ ")
ax1.legend(loc="best")
print(params[0],errors[0])
fig.savefig("build/plot1.pdf")

y_plot=np.linspace(0.013,0.025,1000)
fig, ax2=plt.subplots(1,1, layout="constrained")
#ax2.plot(x, z,".k", label="Messwerte")
ax2.errorbar(x,z, np.sqrt(z),fmt=".k",label="Messwerte")
params1, covariance_matrix = np.polyfit(x[5:10], z[5:10], deg=1, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix))
ax2.plot(y_plot,params1[0]*y_plot+params1[1],label="Linearisierung des Abfalls")
#5-10
ax2.set_xlabel(r"$x \mathbin{/} \unit{\meter}$")
ax2.set_ylabel(r"Zählrate")
ax2.legend(loc="best")

b=ufloat(params1[1],errors1[1])
m=ufloat(params1[0],errors1[0])


zs=np.sqrt(z)
zu=unumpy.uarray(z,zs)
x2=(zu[0]-2*b)/(2*m)
print(x2)

fig.savefig("build/plot1zähl.pdf")

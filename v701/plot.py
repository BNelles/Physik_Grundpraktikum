import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy


p,c,z=np.genfromtxt("data/data1.txt",unpack=True)


c0=4/c[0]
E=c0*c
#print(E)
#p=p[:14]
#c=c[:14]
#z=z[:14]
zs=np.sqrt(z)
zu=unumpy.uarray(z,zs)
#print(zu)



x=0.06*(p/1013)



m=(zu[8]-zu[7])/(x[8]-x[7])
b=(zu[8]+zu[7]-m*(x[8]+x[7]))/2

x2=(zu[1]-2*b)/(2*m)
print(x2)

params, covariance_matrix = np.polyfit(x[:10], E[:10], deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(-0.001,0.035,1000)
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, E,".k" ,label="Messwerte")
ax.plot(x_plot,params[0]*x_plot+params[1],"--",label="Regression")


#ax.errorbar(x,E, np.sqrt(E),fmt=".k",label="Messwerte")


ax.set_xlabel(r"$x \mathbin{/} \unit{\meter}$")
ax.set_ylabel(r"$E \mathbin{/} \unit{\mega\electronvolt}$ ")
ax.legend(loc="best")
fig.savefig("build/plot.pdf")
#print(params[0],errors[0])

y_plot=np.linspace(0.02,0.025,1000)



fig, ax2=plt.subplots(1,1,layout="constrained")
#ax2.plot(x, z,".k", label="Messwerte")
ax2.errorbar(x,z, np.sqrt(z),fmt=".k",label="Messwerte")

m=(z[8]-z[7])/(x[8]-x[7])
b=(z[8]+z[7]-m*(x[8]+x[7]))/2


x2=(z[1]-2*b)/(2*m)
#print(x2)
ax2.plot(y_plot,m*y_plot+b,label="Linearisierung des Abfalls")
ax2.set_xlabel(r"$x \mathbin{/} \unit{\meter}$")
ax2.set_ylabel(r"Zählrate")
ax2.legend(loc="best")
fig.savefig("build/plotzähl.pdf")



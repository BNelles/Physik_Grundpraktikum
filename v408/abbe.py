import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp


G=3
Pg=25

Pl,Ps,B=np.genfromtxt('data/data3.txt', unpack=True)

V=B/G       #Abbildungsmaßstab
#print(V)
a1=1+V       #Hilfsvariablen
a2=1+1/V

g=Pl-Pg     #Abstände
b=Ps-Pl

fig, (ax1, ax2)=plt.subplots(2,1,layout="constrained")

ax1.plot(a2,g,".k", label=r"Messwerte")     #g zu 1+1/V

params1, covariance_matrix = np.polyfit(a2, g, deg=1, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(1,5,2)

ax1.plot(x_plot, params1[0]*x_plot+params1[1], "--", label=r"Ausgleichsgerade")

ax1.set_ylabel(r"$g' \mathrm{/} \unit{\centi\meter}$")
ax1.set_xlabel(r"$1+\frac{1}{V}$")


ax1.legend()


#print(params1,errors1)


ax2.plot(a1,b,".k",label=r"Messwerte")     #b zu 1+V

params2, covariance_matrix = np.polyfit(a1, b, deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix))
x_plot1=np.linspace(1,3,2)
ax2.plot(
    x_plot1,params2[0]*x_plot1+params2[1],"--",label=r"Ausgleichsgerade"
)

ax2.set_ylabel(r"$b' \mathrm{/} \unit{\centi\meter}$")
ax2.set_xlabel(r"$1+V$")



#print(params2,errors2)
f=unp.uarray([params1[0],params2[0]],[errors1[0],errors2[0]])
#print((f[0]+f[1])/2)
print("Hallo")
#plt.show()
ax2.legend()
fig.savefig("build/abbe.pdf")
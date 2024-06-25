import matplotlib.pyplot as plt
import numpy as np

#Braggbedingung
w,Z=np.genfromtxt("data/Bragg.txt",unpack=True)
w=w/2
fig1, ax1=plt.subplots(1,1,layout='constrained')
ax1.set_xlabel(r"$\theta \text{/}°$")
ax1.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax1.plot(w,Z,".")
#print((14-13.8)/14*100)
fig1.savefig("build/plot.pdf")

#Kupferemissionsspektrum
w1,Z1=np.genfromtxt("data/Emmisionsspektrum.txt",unpack=True)
w1=w1/2
fig2, ax2=plt.subplots(1,1,layout='constrained')
ax2.set_xlabel(r"$\theta \text{/}°$")
ax2.set_ylabel(r"$R \text{/} \unit{\per\second}$")
ax2.plot(w1,Z1,".")
fig2.savefig("build/emiss.pdf")

#print(Z1[77:85])
#print(w1[80:85])
params, covariance_matrix=np.polyfit(w1[77:82],Z1[77:82],deg=1,cov=True)
params1, covariance_matrix1=np.polyfit(w1[80:85],Z1[80:85],deg=1,cov=True)

x=(params1[1]-params[1])/(params[0]-params1[0])
x1=1/2*(x-params[1]/params[0])
x2=1/2*(x-params1[1]/params1[0])
#print(x2-x1)

print(Z1[91:96])
params2, covariance_matrix2=np.polyfit(w1[88:94],Z1[88:94],deg=1,cov=True)
params3, covariance_matrix3=np.polyfit(w1[91:96],Z1[91:96],deg=1,cov=True)

xm=(params3[1]-params2[1])/(params2[0]-params3[0])
x3=1/2*(x-params2[1]/params2[0])
x4=1/2*(x-params3[1]/params3[0])
print(x4-x3)

#Abschirmkonstanten


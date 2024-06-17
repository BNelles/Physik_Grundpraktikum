import matplotlib.pyplot as plt
import numpy as np

t,f= np.genfromtxt("data/data2.txt",unpack=True)

t=t-30.7*0.4
d=t*7/4

a1=90-np.rad2deg(np.arcsin(np.sin(np.deg2rad(15))*18/27))

v0=2*(10**6)
c=2700
K=(2*v0)/(c)
print(K)

v=f/((np.cos(np.deg2rad(a1)))/K)

#a1=90-np.arcsin(np.sin(15/360*2*np.pi)*18/27)*180/np.pi

#f1=f/(np.cos(a1/360*2*np.pi)*2*2*10**6/(3*10**8))

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,layout="constrained")
ax1.plot(d[0:11],v[0:11],"b.",label="10mm & 3l/min")
#ax1.set_xlabel(r"$D \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax1.legend(loc="best")

ax2.plot(d[11:26],v[11:26],"r.",label="10mm & 6l/min")
#ax2.set_xlabel(r"$D \mathbin{/} \unit{\milli\meter}$")
#ax2.set_ylabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax2.legend(loc="best")

ax3.plot(d[26:40],v[26:40],"g.",label="7mm & 3l/min")
#ax3.set_xlabel(r"$D \mathbin{/} \unit{\milli\meter}$")
#ax3.set_ylabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax3.legend(loc="best")


ax4.plot(d[40:54],v[40:54],"y.",label="7mm & 6l/min")
#ax4.set_xlabel(r"$D \mathbin{/} \unit{\milli\meter}$")
#ax4.set_ylabel(r"$v \mathbin{/} \unit{\meter\per\second}$")
ax4.legend(loc="best")

plt.show()
print(f/((np.cos(np.deg2rad(a1)))/((2*2*10**6)/(3*10**8))))
import matplotlib.pyplot as plt
import numpy as np

U_v0,A_v0=np.genfromtxt("data/blau.txt",unpack=True)
U_b,A_b=np.genfromtxt("data/violett.txt",unpack=True)
U_g,A_g=np.genfromtxt("data/grün.txt",unpack=True)
U_o,A_o=np.genfromtxt("data/orange.txt",unpack=True)

U_v=U_v0[0:11]
A_v=A_v0[0:11]

W_v=np.sqrt(A_v)
W_b=np.sqrt(A_b)
W_g=np.sqrt(A_g)
W_o=np.sqrt(A_o)

v, cv = np.polyfit(U_v, W_v, deg=1, cov=True)
ev = np.sqrt(np.diag(cv))

b, cb = np.polyfit(U_b, W_b, deg=1, cov=True)
eb = np.sqrt(np.diag(cb))

g, cg = np.polyfit(U_g, W_g, deg=1, cov=True)
eg = np.sqrt(np.diag(cg))

o, co = np.polyfit(U_o, W_o, deg=1, cov=True)
eo = np.sqrt(np.diag(co))

V=v[0]*U_v+v[1]

B=b[0]*U_b+b[1]

G=g[0]*U_g+g[1]

O=o[0]*U_o+o[1]

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,layout="constrained")
ax1.plot(U_v,W_v,"m.",label="Violet")
#ax1.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
#ax1.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax1.plot(U_v,V,"-",label="Ausgleichsgerade")
ax1.legend(loc="best")
ax2.plot(U_b,W_b,"b.",label="Blau")
#ax2.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
#ax2.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax2.plot(U_b,B,"-",label="Ausgleichsgerade")
ax2.legend(loc="best")
ax3.plot(U_g,W_g,"g.",label="Grün")
#ax3.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
#ax3.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax3.plot(U_g,G,"-",label="Ausgleichsgerade")
ax3.legend(loc="best")
ax4.plot(U_o,W_o,"y.",label="Orange")
#ax4.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
#ax4.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax4.plot(U_o,O,"-",label="Ausgleichsgerade")
ax4.legend(loc="best")

plt.show()
import matplotlib.pyplot as plt
import numpy as np

v,f= np.genfromtxt("data/data1.txt",unpack=True)

print(np.cos(90/360*2*np.pi))
print(v[0:5])

f_15=f[0:5]/np.cos(15)

a=15
c=1800
v

dv_cos=2*v0*v/c

fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained")
ax1.plot(x, y, label="Kurve")
ax1.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
ax1.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
ax1.legend(loc="best")

ax2.plot(x, y, label="Kurve")
ax2.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
ax2.set_ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
ax2.legend(loc="best")

fig.savefig("build/plot.pdf")

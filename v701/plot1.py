import matplotlib.pyplot as plt
import numpy as np

p,c,z=np.genfromtxt("data/data2.txt",unpack=True)

fig, (ax1, ax2) = plt.subplots(1, 2, layout="constrained")
ax1.plot(p, c, label="Kurve")
ax1.set_xlabel(r"$p \mathbin{/} \unit{\bar}$")
ax1.set_ylabel(r"channel ")
ax1.legend(loc="best")

ax2.plot(p, z, label="Kurve")
ax2.set_xlabel(r"$p \mathbin{/} \unit{\bar}$")
ax2.set_ylabel(r"Zählrate")
ax2.legend(loc="best")

fig.savefig("build/plot1.pdf")

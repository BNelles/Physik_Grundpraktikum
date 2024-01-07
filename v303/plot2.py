import matplotlib.pyplot as plt
import numpy as np

x,y=np.genfromtxt('data3.txt',unpack=True)

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, y,"o", label="Messwerte")

ax1.set_xlabel(r"$r \mathbin{/} \unit{\centi\meter}$")
ax1.set_ylabel(r"$U_{out} \mathbin{/} \unit{\volt}$")
ax1.legend(loc="best")



fig.savefig("build/plot2.pdf")

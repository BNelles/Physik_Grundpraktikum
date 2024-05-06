import matplotlib.pyplot as plt
import numpy as np

x=1
y=2

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

import matplotlib.pyplot as plt
import numpy as np

U,A=np.genfromtxt("data/blau.txt",unpack=True)
u,a=np.genfromtxt("data/grob.txt",unpack=True)
U=U*10**(-3)

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(U, A,".", label="I")
ax1.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
ax1.set_ylabel(r"$A \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

ax1.plot(u, a,".", label="I/2")
ax1.legend(loc="best")
142

fig.savefig("build/plot.pdf")

import matplotlib.pyplot as plt
import numpy as np

U,N=np.genfromtxt("data/data1.txt",unpack=True)
LN=np.log(N)

fig, ax1 = plt.subplots(1, 1, layout="constrained")
ax1.plot(U, LN, label="Kennlinie")
ax1.set_xlabel(r"$U \mathbin{/} \unit{\volt}$")
ax1.set_ylabel(r"$N$")
ax1.legend(loc="best")


fig.savefig("build/plot.pdf")

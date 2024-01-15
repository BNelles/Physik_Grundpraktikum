import matplotlib.pyplot as plt
import numpy as np

x,z=np.genfromtxt("data1.txt",unpack=True)
y=z+273,15

a,c=np.genfromtxt("data1.txt",unpack=True)
b=c+273,15


fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, y, "o", label="T1")
ax.plot(x, c, "o", label="T2")

ax.set_xlabel(r"$T \mathbin{/} \unit{\kelvin}$")
ax.set_ylabel(r"$t \mathbin{/} \unit{\second}$")
ax.legend(loc="best")



fig.savefig("build/plot.pdf")

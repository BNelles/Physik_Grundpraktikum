import matplotlib.pyplot as plt
import numpy as np

f,U = np.genfromtxt("Klirrfaktor.txt",unpack=True)
x=f/150
y=U*10**-3
fig, ax=plt.subplots()

ax.set(
    xlabel=r"$\Omega$",
    ylabel=r"$U/U_s$",
)
ax.plot(x,y,"o")
ax.set_xscale("log")

fig.savefig("frequenzplot.pdf")
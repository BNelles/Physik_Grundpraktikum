import numpy as np
import matplotlib.pyplot as plt

x,y = np.genfromtxt("Dampfwärme_daten.txt", unpack=True)
fig, ax=plt.subplot()

ax.set(
    xlabel=r"$T/°C$",
    ylabel=r"$p/bar$",
)
ax.plot(x,y,"o")
plt.show()
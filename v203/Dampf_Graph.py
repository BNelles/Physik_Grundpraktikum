import matplotlib.pyplot as plt
import numpy as np

T,p = np.genfromtxt("Dampfwärme_daten.txt", unpack=True)
fig, ax=plt.subplots()

ax.set(
    xlabel=r"$T/°C$",
    ylabel=r"$p/bar$",
)
ax.plot(T,p,"o")
plt.show()
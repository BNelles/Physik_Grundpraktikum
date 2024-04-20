import matplotlib.pyplot as plt
import numpy as np

I,x = np.genfromtxt("data/data3.txt",unpack=True)


fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I, label="Doppelspalt")
ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")


fig.savefig("build/plot2.pdf")
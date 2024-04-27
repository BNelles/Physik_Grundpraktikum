import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev


I,x = np.genfromtxt("data/data2.txt",unpack=True)


fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(x, I, label="Spalt 2")
ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")


#c = Chebyshev.fit(x, I, deg=10)
#
#
#ax1.plot(x, c(x), label="Fit")

fig.savefig("build/plot1.pdf")